**Important:**

Do **not** follow this process if you think you have discovered a vulnerability.
Instead, please use the [VMT](https://github.com/kata-containers/community/blob/master/VMT/VMT.md)
process.

# Architecture Committee Meeting Guidelines

The Architecture Committee (AC) recommends following a set of guidelines for
raising issues and adding topics to the meeting agenda.

## Use a GitHub issue first

For a project like Kata Containers, with contributors spanning across so many
different time zones, asynchronous discussions and reviews are the preferred
communication media.

Directly starting a proposal or trying to resolve new technical issues through
the AC meeting has many drawbacks:
* It potentially leaves a large part of the community out of the initial
  discussion.
* It does not give the AC meeting audience enough time to think through
  the proposal and give constructive and well thought feedback.
* It makes it hard to track and share the discussion outcome.

As a consequence, the AC recommends using [GitHub issues](https://github.com/kata-containers/kata-containers/issues)
at first before adding new items to the AC meetings agenda, especially
if you think the topic could be discussed and resolved in less than two weeks.

## AC Agenda topics must be supported by a GitHub issue or a PR

Except for a few cases listed in the next section, any topic brought to the AC
meeting must be linked to a GitHub issue or a PR that should contain a
`cc @kata-containers/architecture-committee` in order to notify AC members of
the creation of a new AC meeting proposal.

Unless the topic must be urgently discussed, the AC recommends waiting for one
or two weeks before bringing the discussion to the AC meeting. That will give
enough time for interested contributors to digest the issue or proposal before
having a live discussion in the AC meeting.

### Exceptions

* Announcements
* Presentations
* Call for reviews of articles, blog posts, etc.

## AC agenda topics should have well defined expectations

When adding a topic to the agenda, one should have clearly defined expectations:
**"What do I want to get from the community and the AC with that discussion?"**.

For instance:
* Are you looking for a possible **solution** to a problem exposed through
  GitHub or the mailing list?
* Are you looking for a **resolution** of a conflict in a pull request?
* Are you looking for a [**"go/no go"**](./CONTRIBUTING.md#submit-issues-before-prs)
  from the community in order to start working on something?
* Are you looking for technical **feedback and guidelines** on a pending
  technical proposal?

Answering those questions and clearly stating the expectations upfront will
help with steering the AC meeting discussions in the right direction.
