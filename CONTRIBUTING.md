# Contributing to the Kata Containers project

* [Code of Conduct](#code-of-conduct)
* [Golang Coding Style](#golang-coding-style)
* [Certificate of Origin](#certificate-of-origin)
* [Pull requests](#pull-requests)
    * [Before starting work on a PR](#before-starting-work-on-a-pr)
    * [Normal PR workflow](#normal-pr-workflow)
    * [Re-vendor PRs](#re-vendor-prs)
* [Patch format](#patch-format)
    * [General format](#general-format)
    * [Subsystem](#subsystem)
    * [Advice](#advice)
    * [Verification](#verification)
    * [Examples](#examples)
        * [Main patch](#main-patch)
        * [Supplementary patch](#supplementary-patch)
* [Reviews](#reviews)
    * [Examples](#examples)
* [Contact](#contact)
    * [Project maintainers](#project-maintainers)
* [Issue tracking](#issue-tracking)
* [Closing issues](#closing-issues)

The Kata Containers project is an open source project licensed under the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

It comprises a number of repositories under the [GitHub Kata
Containers organisation](https://github.com/kata-containers). Unless
explicitly stated otherwise, all the Kata Containers repositories follow the
process documented here.

## Code of Conduct

All contributors must agree to the project [code of conduct](CODE_OF_CONDUCT.md).

## Golang Coding Style

The usual Go style, enforced by `gofmt`, should be used. Additionally, the [Go
Code Review](https://github.com/golang/go/wiki/CodeReviewComments) document
contains a few common errors to be mindful of.

## Certificate of Origin

In order to get a clear contribution chain of trust we use the [signed-off-by
language](https://ltsi.linuxfoundation.org/software/signed-off-process/)
used by the Linux kernel project.

## Pull requests

All the repositories accept contributions by a GitHub Pull request (PR).

### Before starting work on a PR

We welcome all contributions but to minimize the chance of multiple people
working on the same feature or bug fixes (yes, it has happened), we recommend
strongly that you raise a GitHub issue **before** you start working on a PR.

If you are a new contributor, you cannot assign the issue to yourself. In this
case, raise the issue and add a comment stating that you intend to work on the
issue yourself. This gives the team visibility of the work you plan to do.

The other advantage to raising the issue at the outset is that our process requires an
issue to be associated with every PR (see [patch format](#patch-format)).

### Normal PR workflow

Github has a basic introduction to the PR process
[here](https://help.github.com/articles/using-pull-requests/).

When submitting your PR, treat the PR message the same
you would a patch message, including pre-fixing the title with a subsystem
name.

By default, GitHub copies the message from your first patch, which is often
appropriate. However, ensure your message is accurate and complete for the
entire PR because it ends up in the Git log as the merge message.

Your PR might get feedback and comments, and require rework. The recommended
procedure for reworking is to redo your branch to a clean state and "force
push" it to your GitHub branch. A "forced push" is adequate, which is
reflected in the online comment history. Do not pile patches on patches to
rework your branch. You should rework any relevant information from the GitHub
comment section into your patch set because your patches are documented in the
Git log, not the comment section.

For more information on GitHub "force push" workflows see "[Why and how to
correctly amend GitHub pull
requests](http://blog.adamspiers.org/2015/03/24/why-and-how-to-correctly-amend-github-pull-requests/)".

Your PR can contain more than one patch. Use as many patches as necessary to
implement the request. Each PR should only cover one topic. If you mix up
different items in your patches or PR, they will likely need to be reworked.

### Re-vendor PRs

If you raise a PR to update the vendored copy of one or more golang packages,
there are two critical pieces of information you need to add to the commit
body:

- A brief explanation why the re-vendor is required.

  For example, you should state if an important bug fix or new feature is
  required, or if a particular commit is needed.

- The range of commits being added for these third-party packages.

  It is possible that re-vendoring a particular package will also result in
  updates to other dependent packages. However, it is important to include the
  commit range (even if it is big) for the primary package(s) the re-vendor PR
  is raised for.

  These details allow for easier troubleshooting if the re-vendor PR
  introduces bug or behavioral changes.

  Generate the list of new commits added to the primary re-vendored
  package by comparing the previous and latest commits for the package being re-vendored.

  The following example lists the steps you should take if a new version of
  `libcontainer` (part of the `runc` repository) is required:

  1. Determine the previous and latest commits for the package by looking at
     the `diff` of the `Gopkg.toml` file in your branch.

  1. Run the commands below:

     ```
     $ cd $GOPATH/src/github.com/opencontainers/runc
     $ old_commit="..."
     $ new_commit="..."
     $ git log --no-merges --abbrev-commit --pretty=oneline "${old_commit}..${new_commit}") | sed 's/^/    /g'
     ```

  Paste the output of the previous command directly into the commit "as-is".
  Note that the four space indent added by the `sed` command is used to force
  GitHub to render the list in a fixed-width font, which makes it easier to
  read.

For additional information on using the `dep` tool, see
"[Performing vendoring for the Kata Containers project](https://github.com/kata-containers/community/blob/master/VENDORING.md)".

## Patch format

### General format

Beside the `Signed-off-by` footer, we expect each patch to comply with the
following format:

```
subsystem: One line change summary

More detailed explanation of your changes (why and how)
that spans as many lines as required.

A "Fixes #XXX" comment listing the GitHub issue this change resolves.
This comment is required for the main patch in a sequence. See the following examples.

Signed-off-by: <contributor@foo.com>
```

The body of the message is not a continuation of the subject line and is not used to extend the subject line beyond its character limit. The subject line is a complete sentence and the body is a complete, standalone paragraph.

### Subsystem

The "subsystem" describes the area of the code that the change applies to. It does not have to match a particular directory name in the source tree because it is a "hint" to the reader. The subsystem is generally a single word. Although the subsystem must be specified, it is not validated. The author decides what is a relevant subsystem for each patch.

Examples:

| Subsystem | Description |
|--|--|
| `build` | `Makefile` or configuration script change |
| `cli` | Change affecting command line options or commands |
| `docs` | Documentation change |
| `logging` | Logging change |
| `vendor` | [Re-vendoring](#re-vendor-prs) change |

To see the subsystem values chosen for existing commits:

```
$ git log --no-merges --pretty="%s" | cut -d: -f1 | sort -u
```

### Advice

It is recommended that each of your patches fixes one thing. Smaller patches
are easier to review, more likely accepted and merged, and problems are more
likely to be identified during review.

A PR can contain multiple patches. These patches should generally be related to the [main patch](#main-patch) and the overall goal of the PR. However, it is also acceptable to include additional or [supplementary patches](#supplementary-patch) for things such as:

- Formatting (or whitespace) fixes
- Comment improvements
- Tidy up work
- Refactoring to simplify the codebase

### Verification

Correct formatting of the PR patches is verified using the
[checkcommits](https://github.com/kata-containers/tests/tree/master/cmd/checkcommits)
tool.

### Examples

#### Main patch

The following is an example of a full patch description for the main change that shows the required "`Fixes #XXX`" comment, which references the GitHub issue this patch resolves:

```
pod: Remove token from Cmd structure

The token and pid data will be hold by the new Process structure and
they are related to a container.

Fixes: #123

Signed-off-by: Sebastien Boeuf <sebastien.boeuf@intel.com>
```

#### Supplementary patch

If a PR contains multiple patches, [only one of those patches](#main-patch) needs to specify the "`Fixes #XXX`" comment. Supplementary patches have an identical format to the main patch, but do not need to specify a "`Fixes #XXX`"
comment.

Example:

```
image-builder: Fix incorrect error message

Fixed an error message which was referring to an incorrect rootfs
variable name.

Signed-off-by: James O. D. Hunt <james.o.hunt@intel.com>
```


## Reviews

Before your PRs are merged into the main code base, they are reviewed. We
encourage anybody to review any PR and leave feedback.

See the [PR review guide](PR-Review-Guide.md) for tips on performing a careful review.

We use an "acknowledge" system for people to note if they agree or disagree
with a PR. We utilize some automated systems that can spot common acknowledge
patterns, which include placing any of these **at the beginning of a comment
line**:

 - LGTM
 - lgtm
 - +1
 - Approve

### Examples

The following is an example of a valid "ack":

```
Excellent work - thanks for your contribution.

lgtm
```

The following comment is *not* valid because the magic "lgtm" does not start
at the beginning of the line:

```
I love it! Very clean code and great tests. lgtm.
```

## Contact

The Kata Containers community can be reached through its dedicated IRC
channels, Slack channels, and mailing lists:

* IRC:
  * Development discussions: `#kata-dev @ freenode.net`.
  * General discussions: `#kata-general @ freenode.net`.

* [Slack channels](https://katacontainers.slack.com/) ([invite](http://bit.ly/KataSlack)).

* [Mailing lists](http://lists.katacontainers.io/).

### Project maintainers

The Kata Containers project maintainers are the people accepting or
rejecting any PR. They are listed in the `OWNERS` files. There can be one
`OWNERS` file per directory.

The `OWNERS` files split maintainership into 2 categories: reviewers and
approvers. All approvers also belong to the reviewers list. There must be at
least one approval from one member of each list for a PR to be merged.

Since approvers are also reviewers, they technically can approve a PR without
getting another reviewer's approval. However, it is their due diligence to
rely on reviewers and should use their approval power only in very specific
cases.

## Issue tracking

To report a bug that is not already documented, please open a GitHub issue for
the repository in question.

If it is unclear which repository to raise your query against, first try to
get in [contact](#contact) with us. If in doubt, raise the issue
[here](https://github.com/kata-containers/community/issues/new) and we will
help you to handle the query by routing it to the correct area for resolution.

## Closing issues

Our tooling requires adding a `Fixes` comment to at least one commit in the PR,
which triggers GitHub to automatically close the issue once the PR is merged:

```
pod: Remove token from Cmd structure

The token and pid data will be hold by the new Process structure and
they are related to a container.

Fixes #123

Signed-off-by: Sebastien Boeuf <sebastien.boeuf@intel.com>
```

The issue is automatically closed by GitHub when the [commit
message](https://help.github.com/articles/closing-issues-via-commit-messages/)
is parsed.
