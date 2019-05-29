# Contributing to the Kata Containers project

* [Code of Conduct](#code-of-conduct)
* [Golang Coding Style](#golang-coding-style)
* [Certificate of Origin](#certificate-of-origin)
* [Pull requests](#pull-requests)
    * [Before starting work on a PR](#before-starting-work-on-a-pr)
    * [Before submitting a PR](#before-submitting-a-pr)
    * [Normal PR workflow](#normal-pr-workflow)
        * [First PR example](#first-pr-example)
            * [Updating your PR based on review comments](#updating-your-pr-based-on-review-comments)
    * [Temporarily blocking a PR](#temporarily-blocking-a-pr)
    * [Assisted PR workflow](#assisted-pr-workflow)
    * [Re-vendor PRs](#re-vendor-prs)
    * [Stable branch backports](#stable-branch-backports)
* [Patch format](#patch-format)
    * [General format](#general-format)
    * [Subsystem](#subsystem)
    * [Advice](#advice)
    * [Verification](#verification)
    * [Examples](#examples)
        * [Main patch](#main-patch)
        * [Supplementary patch](#supplementary-patch)
* [Reviews](#reviews)
    * [Review Examples](#review-examples)
* [Continuous Integration](#continuous-integration)
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

### Before submitting a PR

Kata Containers utilizes a number of [CI systems](https://en.wikipedia.org/wiki/Continuous_integration)
to automatically check every PR. As well as performing execution tests locally on
your PR before submission, you are strongly encouraged to also run the same suite of
[static checks](https://github.com/kata-containers/tests/blob/master/.ci/static-checks.sh)
the CI will execute.

> **Note:** If working on `kata-runtime`, first ensure `make` and `make install` has been run in the `virtcontainers` subdirectory. (See [virtcontainers](https://github.com/kata-containers/runtime/blob/master/virtcontainers/documentation/Developers.md#testing) documentation for more information.)
> 
> ```sh
> $ pushd runtime/virtcontainers
> $ make
> $ sudo -E PATH=$PATH make install
> $ popd
> ```
>
> The final `popd` is required to return to the top-level directory from where other build rules can be executed.

The easiest way to execute static checks in most of the repositories is to invoke the `Makefile` `check` and `test` rules, while developer mode is enabled.

```sh
$ export KATA_DEV_MODE=true
$ make check
$ make test
```

These should execute without errors. If errors are reported, fix them
before submitting your PR.

> **Note:** To ensure you replicate the static checks performed by the CI system, it is
recommended that you:
> * Ensure you have a "clean" source tree, as the checks will check all files present, and
might fail if you have extra files or your files are out of date in your tree.
> * Ensure that [`golangci-lint`](https://github.com/golangci/golangci-lint) is current or
has not been installed (the static check scripts will install it if necessary). Changes
in either the linters used or the Kata Containers code base can produce spurious errors
that do not fail inside the CI systems.


### Normal PR workflow

GitHub has a basic introduction to the PR process
[here](https://help.github.com/articles/using-pull-requests/).

When submitting your PR, treat the PR message the same
you would a patch message, including pre-fixing the title with a subsystem
name.

By default, GitHub copies the message from your first patch, which is often
appropriate. However, ensure your message is accurate and complete for the
entire PR because it ends up in the Git log as the merge message.

You should also assign any appropriate GitHub labels to your PR. This
is particularly relevant to maintain stable backports. See the
[Stable branch backports](#stable-branch-backports) section for more details.

Your PR might get feedback and comments, and require rework. The recommended
procedure for reworking is to redo your branch to a clean state and "force
push" it to your GitHub branch. A "forced push" is adequate, which is
reflected in the online comment history. Do not pile patches on patches to
rework your branch. You should rework any relevant information from the GitHub
comment section into your patch set because your patches are documented in the
Git log, not the comment section.

Your PR can contain more than one patch. Use as many patches as necessary to
implement the request. Each PR should only cover one topic. If you mix up
different items in your patches or PR, they will likely need to be reworked.

#### First PR example

This section guides you through the process to create your first PR. We will
create a branch and in that branch we will change *this document*, which lives
in the Kata Containers community repository:

- https://github.com/kata-containers/community

This is the official location for this repository and is referred to as the
"upstream" repository.

> **Note:** This section assumes no previous `git(1)` setup or knowledge.

- Create a free GitHub account

  To raise PRs and create issues, you must have a GitHub account.

- Basic Git setup

  First, install the `git` package for your distribution. Second, tell Git
  your name and email address, if you haven't already, so they can be recorded
  in your commits.

  ```sh
  $ git config --global user.email "you@example.com"
  $ git config --global user.name "Your Name"
  ```

  > **Note:** The email address you specify here must match your primary GitHub email address.

- Create your own copy of the repository

  Click "fork" to create "your copy" of the repository you want to change on
  https://github.com/kata-containers/community. This is an exact copy of the
  upstream repository located at
  `https://github.com/${your-github-username}/community` on the GitHub server. You
  can make changes on this copy as we move through the example.

- Prepare your environment

  > **Note:**: Most of the
  > [Kata Containers repositories](https://github.com/kata-containers)
  > contain code written in the
  > [Go language (golang)](https://golang.org/). Go requires all code to be put
  > inside the directory specified by the `$GOPATH` variable. Since this example PR
  > is not using golang you do not need to
  > [install golang](https://github.com/kata-containers/documentation/blob/master/Developer-Guide.md#requirements-to-build-individual-components).
  > However it still makes sense to put the code in the standard location.

  ```sh
  $ export GOPATH=${GOPATH:-$HOME/go}
  $ mkdir -p "$GOPATH"
  ```

  > **Note:** The code above is safe to run whether you have golang installed
  > or not.
  > For further details on golang, refer to the
  > [requirements section of the Kata Developer Guide](https://github.com/kata-containers/documentation/blob/master/Developer-Guide.md#requirements-to-build-individual-components).


- [Clone the upstream repository](https://help.github.com/articles/cloning-a-repository):

  "Cloning" is a term that means to create a *local copy* of a Git repository
  that generally lives on a remote server.

  ```sh
  $ dir="$GOPATH/src/github.com/kata-containers"
  $ mkdir -p "$dir"
  $ cd "$dir"
  $ git clone https://github.com/kata-containers/community
  $ cd community
  ```

  > **Note:** The previous Git command:
  >
  > - Creates a *local copy* of the upstream repository and switches to the
  >   `master` *branch*.
  > - Creates an "alias" (name) for the upstream repository URL called `origin`.

  There are now *three* copies of the repository (all *exactly* the same):

  - The original upstream one (https://github.com/kata-containers/community)

    You do not (and cannot) make changes to this repository. PRs are a way of
    allowing the project developers and administrators to review your work and
    decide if they want to add your work to the upstream branch.

    > **Note:** Don't worry - even if you make a mistake,
    > you *cannot* do any damage to this repository.

  - Your fork (`https://github.com/${your-github-username}/community`) on GitHub

    This is where you send or upload (`git push`) your PR branches.

  - Your *local copy* of the upstream repository
    (https://github.com/kata-containers/community)

    This is where you actually make changes to your private copy of the
    repository.

- [Setup a "git remote"](https://help.github.com/articles/configuring-a-remote-for-a-fork):

  "What happened to my fork?". The following demonstrates where your fork is
  and how you use it.

  Recall that your fork on the GitHub server is an *exact copy* of the
  upstream repository that also lives on the GitHub server. That might not be
  true moving forward because PRs are constantly merged into the upstream
  repository. This means your fork will be out of date because it will not
  contain the latest changes in the upstream repository. The same
  problem also affects your local copy of the upstream repository.

  The way you keep your local copy up to date is to run `git pull`
  periodically. This command downloads all the latest changes from "another
  repository" into your local repository.

  You might ask how Git knows which repository to pull changes from. Simply,
  it defaults to pull from the repository in which you ran `git clone`
  previously. In Git terminology that default repository is given two names:

  - The URL for the default upstream repository is called the `origin`.

  - The local branch that Git puts the copy of the upstream repository into is
    called `master`.

  If you run `git push`, Git will try to upload any of your local changes
  into the default repository (i.e. the `origin`). This will not work because
  the `origin` is the upstream repository that you do not have permission to
  change.

  You need to tell Git that your changes should be uploaded to your fork on
  the GitHub server when you `git push` This is done by adding what is called
  a "remote":

  ```sh
  $ user="your-github-username"
  $ git remote add github https://github.com/${user}/community
  ```

  > **Note:** The previous command adds an alias (name) for the URL of the
  > fork you created on the GitHub server. This makes using the fork easier.

- Create a new "topic branch" to do your work on:

  ```sh
  $ git checkout -b fix-doc-bugs
  ```

  > **Warning:** *Never* make changes directly to the `master` branch -
  > *always* create a new "topic branch" for PR work.

- Make some changes

  In this example we modify the file you are reading:

  ```sh
  $ $EDITOR CONTRIBUTING.md
  ```

- Commit your changes to the current (`fix-doc-bugs`) branch and make sure you
  use the correct [patch format](#patch-format):

  ```sh
  $ git commit -as
  ```

- Push your local `fix-doc-bugs` branch to your remote fork:

  The following command uploads your changes to *your fork on the GitHub server*:

  ```sh
  $ git push -u github
  ```
  > **Note:** The `-u` option tells `git` to "link" your local clone with your
  > remote fork so that it will know from now on that the local repository and
  > the remote fork refer to "the same" upstream repository. Strictly, you
  > only need to use this option the first time you call `git push` for a new
  > clone.

- Create the PR:
  - Browse to https://github.com/kata-containers/community.
  - Click the "Compare & pull request" button that appears.
  - Click the "Create pull request" button.

    > **Note:** You do not need to change any of the defaults on this page.

The following is a summary of the components and terms we covered in this section:

| Thing | Description | Summary |
|-|-|-|
| https://github.com/kata-containers/community | Official repository URL. | upstream |
| `https://github.com/${your-github-username}/community` | URL of your remote copy of the official repository. | fork |
| `$GOPATH/src/github.com/kata-containers/community` | Location of your local copy of the repository. | checkout or clone |
| `master` | Local *branch* containing a copy of the upstream. | `master` branch |
| `origin` | The "remote" name for the official repository. | `origin` remote |
| `github` | The "remote" name for your remote fork. | `github` remote |
| `fix-doc-bugs` | Local *branch* containing your PR changes. | `fix-doc-bugs` branch |

You have setup your Git environment to do the following:

| Branch | Operation | Description |
|-|-|-|
| `master` | `git pull` | Downloads changes from the `origin` remote (upstream repository) into the local `master` branch |
| `fix-doc-bugs` | `git push` | Uploads changes from your local PR branch to your fork on the GitHub server |

##### Updating your PR based on review comments

Let's say you received some review feedback that asked you to make some
changes to your PR. You have updated your local branch and committed those
review changes by creating three commits. There are now four commits in your
local branch: the original commit you created for the PR and three other
commits you created to apply the review changes to your branch. Your branch
now looks something like this:

```sh
$ git log master.. --oneline --decorate=no
4928d57 docs: Fix typos and fold long lines
829c6c8 apply review feedback changes
7c9b1b2 remove blank lines
60e2b2b doh - missed one
```

> **Note:** The `git log` command compares your current branch (`fix-doc-bugs`)
> with the `master` branch and lists all the commits, one per line.

Since all four commits are related to *the same change* to fix spelling mistakes
and break long lines up into shorter lines, it makes sense to combine all four
commits into a *single commit* on your PR. To do this, complete the following
steps:

- Update your branch

  You need to ensure your local copy of the upstream branch contains the
  latest changes.

- Rebase your changes against the `master` branch

  This operation might seem scary, but it is the way Git allows you to merge
  all of your changes together.

- Squash all the commits together

  "Squashing" means to combine all your commits into a single commit. All the
  changes you made are saved and associated with a single commit, rather than
  being spread across four commits.

- Force-push the newly updated branch to your fork on GitHub

  This updates your PR with your new (*single*) commit.

Taking each step in turn:

- Update your branch

  First, update the `master` branch in your local copy of the upstream
  repository:

  ```sh
  $ cd $GOPATH/src/github.com/kata-containers/community
  $ git checkout master
  $ git pull
  ```

  The previous command downloads all the latest changes from the upstream
  repository and adds them to your *local copy*.

  Now, switch back to your PR branch:

  ```sh
  $ git checkout fix-doc-bugs
  ```

- Start the rebase operation

  ```sh
  $ git rebase -i master
  ```

  As an example, your editor window could appear as follows:

  ```
  pick 2e335ac docs: Fix typos and fold long lines
  pick 6d6deb0 apply review feedback changes
  pick 23bc01d remove blank lines
  pick 3a4ba3f doh - missed one
  ```

- In your editor, read the comments at the bottom of the screen. Next, without
  modifying the first line (`pick 2e335ac docs: Fix typos and fold long lines`),
  change the "`pick`" at the start of all the other lines to "`squash`".

  As an example, your editor window could appear as follows:

  ```
  pick 2e335ac docs: Fix typos and fold long lines
  squash 6d6deb0 apply review feedback changes
  squash 23bc01d remove blank lines
  squash 3a4ba3f doh - missed one
  ```

  Next, save and quit the editor window and Git puts you *back* into your
  editor. Now, instead of showing you all the one line commit summaries, you
  will see all the commit *messages*. These messages are descriptions for all the
  commits you created. At this point you can modify the file as you wish. Once
  you save and exit the editor, Git uses whatever is left in the file as the
  commit message for your "squashed" commit.

  If you followed the example [first PR](#first-pr-example),
  your first commit ("`2e335ac docs: Fix typos and fold long lines`")
  is already in the [correct format](#patch-format). You keep the text for
  your first commit and delete everything else in the editor window and update
  if appropriate based on the review feedback.

  Save the file and quit the editor. Once this operation completes, the four
  commits will have been converted into a single new commit. Check this by
  running the `git log` command again:

  ```sh
  $ git log master.. --oneline --decorate=no
  3ea3aef docs: Fix typo
  ```

- Force push your updated local `fix-doc-bugs` branch to your remote fork:

  ```sh
  $ git push -f github
  ```

  > **Notes:**
  >
  > - Not only does this command upload your changes to your fork, it also
  >   includes the *latest upstream changes* to your fork since you
  >   ran `git pull` in the master branch and then merged those changes into
  >   your PR branch. This is exactly what you want as your fork is now "up to
  >   date" with the upstream repository.
  >
  > - The `-f` option is a "force push". Since you created a new commit using
  >   `git rebase`, you must "overwrite" the old copy of your branch in your
  >   fork on GitHub. This is similar to saving a file in your editor because
  >   you are overwriting the old version you no longer want. GitHub
  >   recommends a force push to handle an update to your PR. This also means
  >   you do not have to create a new PR on GitHub because a force push
  >   effectively re-uses the initial PR you raised and includes your latest
  >   changes.
  >
  >   For more information on GitHub "force push" workflows see "[Why and how to
  >   correctly amend GitHub pull
  >   requests](http://blog.adamspiers.org/2015/03/24/why-and-how-to-correctly-amend-github-pull-requests/)".

Your PR is now updated on GitHub. To ensure team member are aware of this,
leave a message on the PR stating something like, "review feedback applied".
Then, the team is notified and able to re-review your PR more quickly.

### Temporarily blocking a PR

Kata Containers CI systems have two methods that allow marking
PRs to prevent them being merged. The methods are
[GitHub labels](https://help.github.com/articles/about-labels/)
or keywords in the PR subject line. The keywords can appear anywhere
in the subject line.

The following table summarises some common scenarios and appropriate use
of labels or keywords:

| Scenario | GitHub label | PR description contains |
| -------- | ------------ | ----------------------- |
| PR created "as an idea" and feedback sought | `rfc` | RFC |
| PR incomplete - needs more work or rework | `do-not-merge` `wip` | WIP |
| PR should not be merged (has all required "acks", but needs more reviewer input) | `do-not-merge` | |
| PR is a "work In progress", raised to get early feedback | `wip` | WIP |
| PR is complete but depends on another so should not be merged (yet) | `do-not-merge` | |

If any of the values in the table above are set on a PR, it will be
automatically blocked from merging.

> **Note:** Often during discussions the abbreviated and full terms are
> used interchangeably. For instance, often `DNM` is used
> in discussions as shorthand for `do-not-merge`. The CI systems only
> recognise the above phrases as shown.

### Assisted PR workflow

If your PR is deemed useful but you are struggling to update it based on
review feedback, or your PR appears to have been abandoned, the project
maintainers might suggest (or decide in your absence) that an assisted PR
workflow be employed. In that case, a new PR is created using your PR as a
base and applying fixes to it.

The following steps outline the full Assisted PR workflow:

1. A team member is assigned to handling the assisted PR.

1. The team member adds a comment on the original PR explaining what is
   about to happen:

   > Thank you for your contribution but we are unable to merge it until all
   > review feedback has been applied and all CI checks have passed.
   >
   > Since we have not heard from you for a while, we assume you are unable to
   > progress this PR. As such, we intend to create a new PR based on this
   > one, and resolve the identified issues on the new PR. The new PR will
   > reference this PR for tracking purposes.
   >
   > This PR will be marked `do-not-merge` and will be closed when our new PR
   > has been merged. We will credit all authors of this PR on the new PR.

1. The team member applies the `do-not-merge` label to the original PR.

1. The team member creates a new PR based on the contents of the original
   PR.

   The commits from the original PR should be retained where possible.

   At least one commit in the new PR should reference the old PR or its
   associated issue.

   All authors of the new PR, which includes all authors of the original PR,
   should be credited using a `Signed-off-by` comment for each author.

1. The team updates the new PR to resolve the issues with the original PR.

   They might decide to collaborate on this work if it makes sense to do so.
   In this scenario, multiple people push commits to the same PR branch.

   This approach might be adopted in the following scenarios:

   - The number of changes required is high.
   - The changes can be split into logical and discrete groups.
   - The PR requires input from multiple team members.
   - The PR is urgent and needs to be resolved as soon as possible. For
     example, with [documentation PRs](Documentation-Review-Process.md)
     it is essential the documentation is correct.

1. Once the creator of the new PR believes that all issues are resolved in the
   original PR, they request a review of the new PR by the team
   *and the original PR creator*.

   Once all the standard approvals are obtained, the new PR is merged.

   The original PR creator's approval is recommended, but optional. If they do
   not respond in a timely fashion (generally a week, but this might be a much
   shorter period for urgent PRs) the PR is merged regardless.

   If the original PR creator disagrees with the contents of the new PR after
   it is merged, they can raise a PR to resolve the issues.

1. When the new PR is merged, the team member closes the original PR.

### Re-vendor PRs

If you raise a PR to update the vendored copy of one or more golang packages,
after running the
[`dep`](https://github.com/kata-containers/community/blob/master/VENDORING.md)
command ensure you add any modified files under the `vendor/` directory to Git
before committing the changes:

```sh
$ git add vendor/
```

There are two critical pieces of information you need to add to the commit
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
     $ go get -d -u github.com/opencontainers/runc
     $ cd $GOPATH/src/github.com/opencontainers/runc
     $ old_commit="..."
     $ new_commit="..."
     $ git log --no-merges --abbrev-commit --pretty=oneline "${old_commit}..${new_commit}" | sed 's/^/    /g'
     ```

  Paste the output of the previous command directly into the commit "as-is".
  Note that the four space indent added by the `sed` command is used to force
  GitHub to render the list in a fixed-width font, which makes it easier to
  read.

For additional information on using the `dep` tool, see
"[Performing vendoring for the Kata Containers project](https://github.com/kata-containers/community/blob/master/VENDORING.md)".

### Stable branch backports

Kata Containers maintains a number of stable branch releases. Bug fixes to the
master branch are selectively applied to (or "backported") these stable branches.

In order to aid identification of commits that potentially should be backported to
the stable branches, all PRs submitted must be labelled with one or more of the
following labels. At least one label that is *not* `stable-candidate` must
be included.

| Label              | Meaning |
| -----              | ------- |
| `bug`              | A bug fix, which will potentially be a backport candidate |
| `cleanup`          | A cleanup, which will likely not be backported                 |
| `feature`          | A new feature/enhancement, that will likely not be backported  |
| `stable-candidate` | A PR selected for backporting - very likely a bug fix          |
| `vendor`           | A golang vendor update. Might be considered for backport if the vendor update includes critical bug fixes |

In the event that a bug fix PR is selected for backporting to the stable branches,
the `stable-candidate` label is added if not already present, and the original author
of the PR is asked if they will submit the relevant backport PRs. For a quick guide
on how to perform and submit a backport, see the [Backport Guide](Backport-Guide.md)
in this repository.

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
[`checkcommits`](https://github.com/kata-containers/tests/tree/master/cmd/checkcommits)
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

We use the GitHub [Required Reviews](https://help.github.com/articles/approving-a-pull-request-with-required-reviews/)
system for reviewers to note if they agree or disagree with a PR. To have
an acknowledgement or "nack" registered with GitHub, you **must** use the
GitHub "Review changes" dialog to leave feedback. Notes left only in the
comments fields, whilst sometimes useful, will not get registered
in the acknowledgement counting system.

Documentation PRs can sometimes use a modified process explained in the
[Documentation Review Process](Documentation-Review-Process.md) guide.

### Review Examples

The following is an example of a valid "ack", as long as
the "Approve" box is ticked in the Review changes dialog:

```
Excellent work - thanks for your contribution.

lgtm
```

## Continuous Integration

The Kata Containers project has a gating process to prevent introducing
regressions. When your PR is submitted, a Continuous Integration (CI) system
will run different checks on different platforms upon your changes. Currently
Kata uses [Jenkins](http://jenkins.katacontainers.io) and
[Travis CI](https://travis-ci.org/kata-containers/) for testing your changes.

Some of the checks are:

- Static analysis checks.
- Unit tests.
- Functional tests.
- Integretation tests.

The Travis job will be executed right after the PR is opened, while the Jenkins
jobs will wait to be triggered. A maintainer must add a `/test` comment
on the PR to let the CI jobs run.

All CI jobs must pass in order to merge your PR.

## Contact

The Kata Containers community can be reached
[through various channels](README.md#join-us).

## Project maintainers

The Kata Containers project maintainers are the people accepting or
rejecting any PR. Although [anyone can review PRs](#reviews), only the
acknowledgement (or "ack") from an Approver counts towards the approval of a PR.

Approvers are listed in GitHub teams, one for each repository. The project
uses the
[GitHub required status checks](https://help.github.com/en/articles/enabling-required-status-checks)
along with the [GitHub `CODEOWNERS`
file](https://help.github.com/en/articles/about-code-owners) to specify who
can approve PRs. All repositories are configured to require:

- Two approvals from the repository-specific approval team.

- One [documentation team](https://github.com/orgs/kata-containers/teams/documentation/members)
  approval if the PR modifies documentation.

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
