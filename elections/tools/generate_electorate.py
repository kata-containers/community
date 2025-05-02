#!/usr/bin/env python3

#
# Copyright (c) 2023 Kata Contributors
# Copyright (c) 2025 IBM Corporation
#
# SPDX-License-Identifier: Apache-2.0
#
# Description: Generate a list of kata contributors by extracting contact
# information from GitHub

import argparse
import datetime
from datetime import timedelta
import os
import re
import yaml

from collections import OrderedDict
from github3 import login


class AuthorSet(set):
    pass


def _authorset_representer(dumper, data):
    return dumper.represent_list(sorted(list(data)))


class Author(object):
    def __init__(self, id, name=None, email=None):
        self.id = id
        self.name = name
        self._emails = set()
        if email:
            self._emails.add(email)
        self.commit_count = 0

    @property
    def email(self):
        emails = list(self._emails or [])
        if emails:
            # This is horrible simplistic and probably wont work long term.
            return sorted(emails)[0]
        return None

    @email.setter
    def email(self, email):
        self._emails.add(email)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __hash__(self):
        return hash(self.id)


def _author_representer(dumper, data):
    o_dict = OrderedDict(github_id=data.id,
                         name=data.name,
                         email=data.email,
                         # _emails is a private member and we probably
                         # shouldn't  do this but it might be needed for
                         # post-processing
                         emails=list(data._emails),
                         commit_count=data.commit_count)
    return dumper.represent_dict(o_dict.items())

def find_authors_by_project(start_time, end_time):
    dco_re = re.compile('signed.off.by[: ]*(?P<name>[^<]*)<(?P<email>.*)>$',
                        re.IGNORECASE | re.MULTILINE)
    # Get a token GitHub Personal API token see:
    #   https://blog.github.com/2013-05-16-personal-api-tokens/
    # for more information.
    try:
        personal_token=os.environ['GH_TOKEN']
    except KeyError:
        raise Exception("GH_TOKEN environment variable was not set")

    gh = login(token=personal_token)
    org = gh.organization('kata-containers')
    number = -1
    projects = []
    ignored_repos = [
        'agent',
        'ci',
        'dbs-snapshot',
        'documentation',
        'edk2',
        'govmm',
        'is-organization-member',
        'kata-containers-github-actions-tests',
        'ksm-throttler',
        'linux',
        'osbuilder',
        'packaging',
        'project-infra',
        'proxy',
        'qemu',
        'resolve-pr-refs',
        'runtime',
        'shim',
        'slash-command-action',
        'tests',
    ]


    author_cache = {}
    for repo in org.repositories():
        # Skip these repos as they are not a core part of the project, and are
        # forked/imported/archived so contain many contributors from outside the project.
        # Also skip the github security advisory repos for quicker processing
        if str(repo).split("/")[1] in ignored_repos or str(repo).split("/")[1].startswith('kata-containers-ghsa'):
            print('Skipping repo %s' % (repo))
            continue
        print('Looking for changes in %s between %s and %s' %
            (repo, start_time, end_time))

        authors = AuthorSet()
        for commit in repo.commits(since=start_time, until=end_time, number=number):
            # If a commit has >1 parents then it's a merge commit, so skip these
            if len(commit.parents) > 1:
                continue

            if commit.author is None:
                if commit.commit.author is None:
                    print('Skipping %s in %s as it has no author. Did this merge via GitHub?' %
                            (commit, repo))
                    continue

                author_id = commit.commit.author.get('email')
                print('%s in %s as has no author. Using email (%s) as the author id' %
                        (commit, repo, author_id))
            else:
                author_id = commit.author.login

            if author_id not in author_cache:
                if commit.author is None:
                    author = Author(author_id, email=author_id,
                                    name=commit.commit.author.get('name'))
                else:
                    _author = gh.user(commit.author.login)
                    author = Author(_author.login, email=_author.email,
                                    name=_author.name)

                author_cache[author_id] = author

            author = author_cache[author_id]
            author.commit_count += 1

            # If the GitHub account doesn't have a name or email address
            # the author *may* have included it in their git config.
            if author.email is None and commit.commit.author.get('email'):
                author.email = commit.commit.author.get('email')
            if author.name is None and commit.commit.author.get('name'):
                author.name = commit.commit.author.get('name')

            # last ditch effort did the author use a valid email address in the
            # DCO line?
            match = dco_re.search(commit.message)
            if match:
                if ((author.email is None or
                        'users.noreply.github.com' in author.email) and
                        match.group('email')):
                    author.email = match.group('email')
                if author.name is None and match.group('name'):
                    author.name = match.group('name')
            authors.add(author)
        projects.append({str(repo): authors})
    return projects

def main():

    parser = argparse.ArgumentParser(description='An electorate generation script')
    parser.add_argument("-end", required=True,help='the end date of the period to examine in format %%d/%%m/%%y.')
    parser.add_argument("-start",  help='the start date of the period to examine in format %%d/%%m/%%y.  If not set will default to' \
    '365 days before the end time')

    args = parser.parse_args()
    end_time = datetime.datetime.strptime(args.end, '%d/%m/%y')
    start_time = end_time - timedelta(days=365)
    if args.start != None:
        start_time = datetime.datetime.strptime(args.start, '%d/%m/%y')

    print("Getting committers from", start_time, " -> ", end_time)

    projects=find_authors_by_project(start_time, end_time)

    # Dark YAML voodoo
    yaml.Dumper.ignore_aliases = lambda *args: True
    yaml.Dumper.add_representer(AuthorSet, _authorset_representer)
    yaml.Dumper.add_representer(Author, _author_representer)
    with open('electorate.yaml', 'w') as f:
        yaml.dump(projects, f, default_flow_style=False, default_style='',
                explicit_start=True)

if __name__ == '__main__':
    main()
