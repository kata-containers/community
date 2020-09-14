# Kata Containers stable backport workflow

* [Introduction](#introduction)
* [Assumptions](#assumptions)
* [Graphical overview of backporting](#graphical-overview-of-backporting)
    * [Before the backport](#before-the-backport)
    * [After the backport](#after-the-backport)
* [Backport Workflow](#backport-workflow)
    * [Setup](#setup)
    * [Locate commits to cherry pick](#locate-commits-to-cherry-pick)
    * [Apply the commits](#apply-the-commits)
    * [Check the result](#check-the-result)
    * [Raise a PR](#raise-a-pr)

## Introduction

This document provides a short guide explaining how to perform a backport.
Backporting refers to applying changes to a stable branch from a newer branch.
The changes comprise one or more commits in the form of a PR and the newer
branch is generally the `master` branch.

Since new features are not added to stable branches, backported changes are
generally bug fixes and security fixes. See the
[stable branch strategy](https://github.com/kata-containers/documentation/blob/master/Stable-Branch-Strategy.md)
document for further details.

> **Note:** This guide does not cover all eventualities that might be
> encountered while performing a backport, and only documents one potential
> Git based workflow. It does serve as a short introduction and reminder of
> the basic stable backport process.

The two branches used in the examples in this guide are:

- The `master` branch (which contains all commits).
- A `stable-1.2` branch which will be the target of the backport: commits will
  be selectively "copied" ("cherry-picked") into this branch from the `master` branch.

## Assumptions

This document assumes an understanding of:

- The `git(1)` tool.
- The [standard PR workflow](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md#pull-requests).
- The [stable branch strategy](https://github.com/kata-containers/documentation/blob/master/Stable-Branch-Strategy.md).

## Graphical overview of backporting

### Before the backport

Imagine that initially both the `master` branch and the stable branch
(`stable-1.2`) contain only the commits `A`, `B` and `C`:

```
          + (stable-1.2 branch)
         /
A---B---C (master branch)
```

New commits (`D`, `E`, `F` and `G`) are added to the `master` branch:

```
          + (stable-1.2 branch)
         /
A---B---C---D---E---F---G (master branch)
```

Imagine that:

- Commits `E` and `G` are bug or security fixes which need to be backported.
- Commits `D` and `F` are new features which must *not* be backported.

### After the backport

After the backporting:

```
          +-----E-------G (stable-1.2 branch)
         /      ^       ^
A---B---C---D---E---F---G (master branch)
```

After the backport, the `stable-1.2` branch contains commits  `A`, `B` and
`C`, `E` and `G`.

## Backport Workflow

The basic workflow involves:

- Creating a new local branch from the stable tree you are targeting.
- Selecting (or "cherry picking") the commits from your master branch PR into the stable branch.
- Submitting your branch to GitHub as a PR against the stable branch (not to the `master` branch).

### Setup

- Ensure your local repo is up to date:

    ```bash
    $ cd ${GOPATH}/src/github.com/kata-containers/runtime
    $ git fetch origin
    ```

    Check the list of stable branches:

    ```bash
    $ git branch -r | grep origin/stable
    ```

- Create your branch to work on, based on the `stable-1.2` branch:

    ```bash
    $ git checkout -b my_1.2_pr_backport origin/stable-1.2
    ```

### Locate commits to cherry pick

To list all commits in the `master` branch which are not in the `stable-1.2`
branch:

```bash
$ git log --oneline --no-merges ..master
```

Make a note of the SHA values for the commits in the PR to backport.

> **Note:** If your PR is in a local branch, substitute `master` for the name
> of that branch.

### Apply the commits

- Pull in your commits:

  If you are pulling the commits in from the `master` branch, you can add the `-x`
  argument to `git cherry-pick` to automatically add a reference in the
  commit to the original commits. This is strongly recommended to aid traceability.
  If you pick the commits from your local branch do *not* use `-x`; this
  potentially adds references to SHAs that only exist in your local branch, which
  is not useful for future tracability.

  It is also required that you add the `-s` signoff to the commits, if you did not
  create the original commits.

  ```bash
  $ git cherry-pick -x <commit>...
  ```

  > **Note:** You should only cherry pick the original commits - do **not**
  > cherry pick merge commits
  > (see [Locate commits to cherry pick](#locate-commits-to-cherry-pick)).

  You can cherry pick ranges of commits. Please see the `git-cherry-pick(1)`
  man page for more information.

  > **Note:** You do not need to open a new `Issue` or add an extra `Fixes: nnn` item
  > to the commits. They should re-use the `Fixes:` entry from the original commits,
  > so all related commits refer back to the common Issue. It does not matter that
  > the original `Issue` is closed, the references still work correctly.

- Resolve any conflicts:

  You might encounter conflicts during your cherry pick, which need to be resolved
  before you continue. Follow standard practices for Git conflict resolution, and see
  the guidance printed by `git cherry-pick` on processing and applying those fixes.

  If you hit a conflict, any effects of `-x` to `cherry-pick` might not be
  applied. In this case, consider hand-adding the `master` SHA references and a note
  that you resolved a conflict to the commit message.

### Check the result

- Test your changes:

  Before you push your changes, you should test that they work and nothing has been
  broken. No matter how small the change, running the test suite is always recommended.

### Raise a PR

- Push your branch to your GitHub repo:

  ```bash
  $ git push my_remote my_1.2_pr_backport
  ```

- Submit a PR from your branch to *the stable branch*:

  When you submit your PR on GitHub, make sure to choose the stable branch that you
  based your branch on and are submitting to. This *should* be the same as the
  base branch for the PR.
