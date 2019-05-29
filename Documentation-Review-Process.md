# Documentation review process

* [Introduction](#introduction)
* [The Documentation Team](#the-documentation-team)
* [Default document review process](#default-document-review-process)
* [Justification for different process](#justification-for-different-process)
    * [Users should always expect accurate Documentation](#users-should-always-expect-accurate-documentation)
    * [Some documentation PRs can be fast-tracked](#some-documentation-prs-can-be-fast-tracked)
    * [Formal doc reviews can be very time-intensive](#formal-doc-reviews-can-be-very-time-intensive)
* [Decision Authority](#decision-authority)
* [Determine if a full document review is required](#determine-if-a-full-document-review-is-required)
    * [Exempt](#exempt)
    * [Required](#required)
* [Requesting a formal document review](#requesting-a-formal-document-review)
* [Lightweight document review process](#lightweight-document-review-process)

## Introduction

The process for reviewing documentation PRs is slightly different from
[the general process for reviewing code PRs](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md#reviewsPR-Review-Guide.md).
This document explains the differences.

## The Documentation Team

The Documentation Team is responsible for carrying out a full documentation
review of a PRs containing documentation changes. Such a review includes
checking the grammar, structure, consistency, and typographical correctness of
the documentation changes.

The following GitHub team lists the users who are members of the Documentation Team:

- https://github.com/orgs/kata-containers/teams/documentation/members

## Default document review process

[Project maintainers](https://github.com/kata-containers/community/blob/master/CONTRIBUTING.md#project-maintainers)
have the power to approve or reject PRs.

If a Documentation Team review is required, the `CODEOWNERS` configuration will
apply and the PR will be blocked until the required number of acks are
obtained for the documentation changes.

Technical writers from the Documentation Team will review the document
changes and add comments explaining how the wording should be changed. It is
then up to the PR creator to apply these changes to their original PR,
rebasing as necessary to ensure a clean `git(1)` history. Once the creator has
applied the changes they need to re-push their branch and add a comment to the
PR asking for a re-review. This process continues indefinitely until the the
Documentation Team is happy with the final result.

## Justification for different process

The documentation review process is different than the code review process for
the following reasons:

### Users should always expect accurate Documentation

Just like code changes, some documentation changes have to be merged as soon
as possible to ensure users have current and accurate information.

Documentation changes tend to be more urgent though. For example, a "Priority
1" code issue needs to be fixed quickly. However it would also need to be
documented clearly (and quickly). If the P1 issue *cannot* be fixed quickly,
the documentation must still be updated as soon as possible to alert users of
the issue and to provide suitable workarounds.

If the documentation is *not* kept current, users have incorrect information
and might create problems for themselves or become disaffected with the
project entirely.

In summary, do not let documentation PRs sit in the PR backlog for any longer
than necessary.

### Some documentation PRs can be fast-tracked

If a PR makes a minor change to one or more documents, passing to the
Documentation Team for a formal review and approval might not be necessary.

### Formal doc reviews can be very time-intensive

Since a full document review can be a slow and pain-staking process, and since
the number of professional technical writers on the Documentation Team is
relatively small compared to the number of developers, it makes sense to only
perform such reviews on the documents that justify the effort.

## Decision Authority

If a Documentation Team member believes a full review is required, their
decision is final.

In most other cases, a project maintainer will decide whether a full review is
required or not.

If project maintainers cannot decide whether the lightweight process should be
followed, the full process should be used instead since the uncertainty
implies "more eyes" should see the changes.

## Determine if a full document review is required

### Exempt

If a PR contains documentation changes that **only** relate to one or more of
the following categories, it does not need to be formally reviewed and
approved by the Documentation Team:

- Changes to code blocks

   The PR only modifies code blocks embedded in the document.

- "Typo" fixes

  The PR only fixes spelling mistakes and whitespace issues.

- Formatting

  The PR only modifies the layout of the existing text. For example, you
  update words to render them in a ``fixed font`` or change a
  [Note](https://github.com/kata-containers/documentation/blob/master/Documentation-Requirements.md#notes)
  to fit the standard formatting conventions.

- URL fixes

   The PR only modifies URLs or updates the table of contents.

- The PR only *removes* documentation.

### Required

The following PR changes generally indicate a full document review is
necessary:

- A new document has been added by the PR.

  All documents should have an initial review unless they are extremely simple.

## Requesting a formal document review

If a PR needs a full document review, add a comment to the PR like the
following, which sends a mail to all members of the Documentation Team:

```
PTAL @kata-containers/documentation
```

## Lightweight document review process

1. Obtain general agreement that
   a Document Team review [is not required](#decision-authority).

1. Ensure all other approvals and CI checks have been met.

1. Ensure the PR contains a note explaining why the PR does not justify a full review.

1. Request a project maintainer force-merges the PR.

   This operation bypasses the check that normally stops a PR from
   landing until the Documentation Team acks the PR.

1. The maintainer should notify the Documentation Team out of courtesy that
   the PR has been merged.

   This allows a follow-on "recovery PR" to be raised should the Documentation
   Team disagree on using the lightweight process.
