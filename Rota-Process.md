# Kata Rota Process

* [Introduction](#introduction)
* [Kata Review Team](#kata-review-team)
* [The rota](#the-rota)
* [Who can join?](#who-can-join)
* [How can I participate?](#how-can-i-participate)
* [Preparation](#preparation)
    * [Reviewing documentation changes](#reviewing-documentation-changes)
* [Tasks](#tasks)
    * [Talk to each other](#talk-to-each-other)
    * [PRs](#prs)
        * [Review PR backlog](#review-pr-backlog)
            * [Triggering a CI run](#triggering-a-ci-run)
            * [CI results](#ci-results)
            * [Stale PRs](#stale-prs)
            * [Temporarily blocking a PR from landing](#temporarily-blocking-a-pr-from-landing)
            * [Stable branches](#stable-branches)
    * [Issues](#issues)
        * [Review issues](#review-issues)
            * [Issue labels](#issue-labels)
            * [Issue triage](#issue-triage)
            * [General process](#general-process)
    * [Test stability](#test-stability)
    * [Weekly Summary](#weekly-summary)

## Introduction

This document explains the structure and roles of the Kata Review Team.

## Kata Review Team

The Kata Containers project runs a [rolling rota of members and volunteers](#the-rota)
who donate their time to assess, review, move forward, and reduce any PR and
issue backlogs across the repositories.

Informally, this team is sometimes referred to as the "Kat Herding Team".

## The rota

The rota is maintained in the
[community wiki](https://github.com/kata-containers/community/wiki/Review-Team-Rota),
which is updated frequently.

## Who can join?

Anybody can participate. You do **not** have to be a subject matter expert or Kata
expert to help. All contributions are welcome.

Joining the team is a great way to expand your knowledge of the project and
your skill set. Sometimes all you need to move a PR forward is for a community
member to read the list of open PRs and ask the appropriate subject matter
expert to review or help with the relevant PR.

Note that you must agree to our [code of conduct](CODE_OF_CONDUCT.md)
if you want to become involved.

## How can I participate?

To participate and be added to the [the rota](#the-rota),
notify the Kata team through one of the contact methods listed on
https://katacontainers.io before you edit this page. Be sure to include your
contact details in the Rota table, preferably your GitHub name.

## Preparation

Before you join the team, we strongly recommend that you read the
[contribution guide](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md).
We suggest you also read the
[PR review guide](https://github.com/kata-containers/community/blob/master/PR-Review-Guide.md)
for tips to consider as you review [pull requests](#prs).

### Reviewing documentation changes

We suggest you read the
[documentation requirements](https://github.com/kata-containers/documentation/blob/master/Documentation-Requirements.md)
and
[documentation review process](https://github.com/kata-containers/community/blob/master/Documentation-Review-Process.md)
to help you review documentation changes.

## Tasks

This section lists which activities the team should focus on.

### Talk to each other

If you are on the review team, we suggest you hang out on
[Slack or IRC](README.md#join-us) in order to chat with each other. Nobody
knows everything so do not hesitate to ask other folks on the team if you need
help.

There is a useful wiki page that
[lists areas of interest for various members of the community](https://github.com/kata-containers/community/wiki/Areas-of-interest).

We also have a
[central GitHub `CODEOWNERS` file](https://github.com/kata-containers/.github/blob/master/CODEOWNERS).
This [file type](https://help.github.com/en/articles/about-code-owners)
defines individuals or teams that are responsible for code in a repository.
This can help identify the appropriate group of people to contact about
certain file changes.

### PRs

#### Review PR backlog

See [the GitHub reports](https://github.com/kata-containers/community/wiki/Review-Team-Rota#finding-the-open-prs)
for a list of open PRs.

Read
[the reviews section in the contributing guide](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md#reviews)
to learn how to "ack" a PR.

##### Triggering a CI run

See the [Controlling the CI](https://github.com/kata-containers/community/wiki/Controlling-the-CI) document.

##### CI results

When you review a PR, look at any CI failures shown at the bottom of the PR
page. If any CI tests fail, review the logs to see if there are obvious
issues.

Add a comment and a brief summary of the error message or issue to explain
which CIs failed.

##### Stale PRs

If a PR has not been touched for a while, add a comment to ask the author if
they intend to update the pull request.

If the author does not respond, we may decide to use the
[assisted PR workflow](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md#assisted-pr-workflow),
which you can also take part in.

##### Temporarily blocking a PR from landing

See [this section in the contributing guide](CONTRIBUTING.md#temporarily-blocking-a-pr).

##### Stable branches

If a PR is just a fix, add the `stable-candidate` label and ask the author to
backport the fix to the last two
[stable branches](https://github.com/kata-containers/documentation/blob/master/Stable-Branch-Strategy.md).

### Issues

#### Review issues

See [the GitHub report](https://github.com/kata-containers/community/wiki/Review-Team-Rota#finding-new-issues)
for a list of issues that need a review.

##### Issue labels

All the repositories use a
[standard set](https://github.com/kata-containers/tests/blob/master/cmd/github-labels/labels.yaml.in)
of GitHub labels. For example, here are the `runtime` repositories labels:

- https://github.com/kata-containers/runtime/issues/labels

Review the list and become familiar with the labels, and then read on.

> **Notes:**
>
> - All labels have a description to explain their use.
>
> - There *are* a lot of labels but only to cover as many scenarios as
>   possible. Most issues only need a small number of labels to be
>   applied to them.

##### Issue triage

Read each new issue carefully. Each issue is an arbitrary description of the
problem or request, so we want to add meaningful labels to each for easier
categorization and search.

If you are unsure of which labels to apply to an issue, talk to the rest of
the [Rota team](#talk-to-each-other) or just ask
[on Slack/IRC](https://github.com/kata-containers/community#join-us).

Here is some general advice:

- Security issue

  Use the
  [Vulnerability Management Process (VMP)](https://github.com/kata-containers/community/blob/master/VMT/VMT.md)
  to handle serious security issues.

  However, [immediately contact the team](https://github.com/kata-containers/community#join-us)
  for advice if you notice a user has raised a normal issue (i.e. does not
  follow the VMP) that appears to be a security issue. The `security` label
  should be added to the issue if it does not need to follow the VMP.

- "Crasher bug"

  If an issue reports a crash or catastrophic error scenario add one or more
  of the following relevant labels:

  - `crash`
  - `data-loss`
  - `hang`
  - `resource-leak`
  - `unreliable`

  If you add one of the previous labels,
  [contact the team](https://github.com/kata-containers/community#join-us)
  to make them aware of the issues as soon as possible.

- Top priority

  Add the `highest-priority` label to flag and alert the team of extremely
  urgent issues. This indicates to the team that the issue should be fixed as
  soon as possible.

- Release gating

  Add the `release-gating` label if you think the issue should be fixed before
  the next release.

- Important medium / long term task

  Add the `highest-severity` label if the issue is very important but not
  time-critical.

- Simple task for new contributors

  Add the `good-first-issue` label if you think the issue is simple with a
  quick resolution and "self-contained." This marks it as suitable for a new
  contributor.

- Invalid

  Add the `invalid` label if you think the issue is not appropriate.

- Duplicate

  Add the `duplicate` label along with a comment referencing the original
  issue if you find a duplicated issue.

- Limitation

  Add the `limitation` label if the issue describes a system limitation.

  If the issue is a
  [known limitation](https://github.com/kata-containers/documentation/blob/master/Limitations.md),
  close the issue with a comment referencing the original limitation issue
  number so the issue author understands why the issue was closed.

- Teams

  Add one of the `team/*` labels if you know which team the issue should be
  assigned to. Note, while some team names are the same as the
  [respective repository](https://github.com/kata-containers),
  some are general (e.g. `team/developer`).

  Add a comment to include the name of the team (use the `@team-name` syntax)
  if you know the GitHub team a particular label relates to. All teams are
  listed [here](https://github.com/orgs/kata-containers/teams).
  [Contact the team](README.md#join-us) if you do not have access to this list.
  They will either grant you access or tell you which team to specify.

- Related project

  Add one of the `related/*` labels if the issue relates to another project.

- Issue is lacking something

  Add one of the the `needs-*` labels if you think the issue is incomplete
  somehow.

##### General process

We use
[GitHub issue templates](https://github.com/kata-containers/.github/tree/master/.github/ISSUE_TEMPLATE)
to help guide users to raising the correct type of issue. All these templates
also automatically add a `needs-review` label to the issues.

The idea of this label is to highlight issues that have *not* yet been
reviewed by the team.

Therefore, after you review an issue with this label, which potentially
results in the application of additional labels, *remove* the `needs-review`
label to signal that the issue has been reviewed.

### Test stability

The more PRs you look at, the more likely you are to notice patterns or
anomalies of CI test failures.
[Raising issues in the `tests` repository](https://github.com/kata-containers/tests/issues/new)
helps us to identify "flaky" tests and prioritize the problematic bugs that
make review/merges slower.

Search for the key failure message in all issues (open and closed) before you
raise an issue. This allows you to see if the issue has been raised before:

- https://github.com/kata-containers

  Enter an error message in the search box and press enter.

If an issue has already been raised, add a comment on the PR to reference it.
If it has not, raise a new issue and provide details of the failure. Add a PR
comment to reference it.

### Weekly Summary

The Team should discuss amongst themselves and nominate someone to write a
brief summary of what the team accomplished in the week. Post the summary to
[the public mailing list](README.md#join-us).

Even if the week is quiet, a brief email is beneficial to show the community
that we continue to progress PRs.

While there is no strict format for the weekly summary, it should mention
significant PRs that have landed or been progressed. The summary does not need
to be highly detailed or particularly long but it does help to include PR URLs
to allow readers to find out further information.

The following link provides a template if you prefer to use one:

- https://github.com/kata-containers/community/blob/master/statusreports/REPORT_TEMPLATE.md

Other things to consider adding to the summary include:

- Were you particularly impressed with a piece of work (or team work)?
- Did you face any particular problems?
- Is there anything that can be done to make the process easier?

You can look at previous weekly reports on the mailing list for examples.
