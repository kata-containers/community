# Kata Containers stable backport workflow

* [Backport Workflow](#backport-workflow)

This document provides a short guide on how to perform a stable backport of a
PR or patchset in the Kata Containers repositories.

It does not cover all eventualities that might be encountered while performing
a backport, and only documents one potential Git based workflow. It does
serve as a short introduction and reminder of the basic stable backport process.

## Backport Workflow

The basic workflow involves creating a new local branch from the stable tree you
are targeting, then cherry picking the commits from your master branch PR
onto that branch. You then submit your branch to GitHub as a PR against the
stable branch (and not the `master` branch).

The following example shows a pseudo-backport of a PR from the `master` branch
into the `stable-1.2` branch of the `runtime` repo.

- Ensure your local repo is up to date:

    ```bash
    $ cd ${GOPATH}/src/github.com/kata-containers/runtime
    $ git fetch origin
    ```

    And check the list of current stable branches:

    ```bash
    $ cd ${GOPATH}/src/github.com/kata-containers/runtime
    $ git branch -r | grep origin/stable
    ```

- Create your branch to work on:

    ```bash
    $ git checkout -b my_1.2_pr_backport origin/stable-1.2
    ```

- Locate the commits you want to pull in:

    Here we look in the `master` branch, presuming the PR has been merged.
    If you have the PR in a local branch you can substitute `master` for the name
    of that branch.

    ```bash
    $ git log --oneline master
    # And search for the SHA of the commits you wish to backport.
    ```

- Pull in your commits:

    If you are pulling the commits in from the `master` branch, you can add the `-x`
    argument to `git cherry-pick` to automatically add a reference in the
    commit to the original commits. This is strongly recommended to aid traceability.
    If you pick the commits from your local branch do *not* use `-x`. This
    potentially adds references to SHAs that only exist in your user branches, which
    is not be useful for future tracability.

    It is also required that you add the `-s` signoff to the commits, if you did not
    create the original commits.

    ```bash
    $ git cherry-pick -x <commit>...
    ```

    You can cherry pick ranges of commits, etc. Please see the `git-cherry-pick(1)`
    man page for more information.

    > *Note:* You do not need to open a new `Issue` for or add an extra `Fixes: nnn` item
    > to the commits. They should re-use the `Fixes:` entry from the original commits,
    > so all related commits refer back to the common Issue. It does not matter that
    > the original `Issue` is closed, the references still work correctly.

- Resolve any conflicts, etc.:

    You might encounter conflicts during your cherry pick, which need to be resolved
    before you continue. Follow standard practices for Git conflict resolution, and see
    the guidance printed by `git cherry-pick` on processing and applying those fixes.

    If you hit a conflict, any effects of `-x` to `cherry-pick` might not be
    applied. In this case, consider hand-adding the `master` SHA references and a note
    that you resolved a conflict to the commit message.

- Test your changes:

    Before you push your changes, you should test that they work and nothing has been
    broken. No matter how small the change, running the test suite is always recommended.

- Push your branch to your GitHub repo:

    ```bash
    $ git push my_remote my_1.2_pr_backport
    ```

- Submit a PR from your branch to *the stable branch*:

    When you submit your PR on GitHub, make sure to choose the stable branch that you
    based your branch on and are submitting to. This *should* be the same as the
    base branch for the PR.
