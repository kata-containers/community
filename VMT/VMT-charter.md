# Kata Containers Vulnerability Management Team (VMT)

Authors:

- Fabiano Fidêncio ([@fidencio](https://github.com/fidencio))
- Markus Rudy ([@burgerdev](https://github.com/burgerdev))

This document defines the responsibilities, membership criteria, and removal criteria for the Kata Containers Vulnerability Management Team (VMT).

The VMT supports the security posture of the Kata Containers project by coordinating the intake, triage, and timely remediation of reported vulnerabilities across releases.
VMT members act as coordinators and facilitators; they do not own vulnerability fixes themselves.

## Goals of a VMT

Historically, security reports for the Kata project were infrequent enough to not require a dedicated team.
Instead, some AC members who got notified by a report would triage it and loop in people as they saw fit, often resorting to fixing the issue themselves to avoid expanding the circle in-the-know.

This mode of operation has become unsustainable.
The amount of reports has grown dramatically with the advent of AI-assisted security reviews, while the workload for AC members did not change.
Many reports go unanswered for weeks.
At the same time, triage gets more difficult due to verbose or false reports.

The Kata project needs a dedicated VMT to make responsibilities crystal clear and offload work from the AC.

## Non-goals

- Reduction of the circle of people aware of embargoed reports.
  - The AC members are GitHub admins, which comes with the permission to view security reports.
    This is the historic explanation for why triage was an AC responsibility.

## Responsibilities

VMT members are expected to perform the duties outlined in the section below.
They are expected to work individually, sharing work based on time and/or area of interest, based on an informal agreement between the VMT members.

### 1. Initial triage of vulnerabilities

Perform a first-pass review of newly reported vulnerabilities, preferably on a daily basis but at least once a week.
For each report, they perform an initial assessment to the best of their ability to determine whether it is valid and relevant to Kata Containers.

If you are uncertain whether a report makes sense, lean towards accepting the report but convey the uncertainty of the assessment in the next steps.

The outcome of this step should either be a closed report, or an accepted report.

### 2. Judge severity and decide on next steps

If the report was accepted as valid, the VMT assigns a rough severity and decides whether the vulnerability needs coordinated disclosure or can be fixed with a regular PR (guidance for this is outside the scope of the VMT document).
The VMT communicates this decision as a comment on the report.

### 3. Assignment of responsible maintainer

After initial triage, the VMT needs to assign a responder to the report.
The responder is responsible for working on the remediation, pulling in additional experts as they see fit, until a fix is either ready on a private GHSA fork or merged into main from a regular PR.

Naturally, the VMT needs to take familiarity with the vulnerable code, availability and other circumstances into account when choosing a responder.

If a remediation takes longer than a few days, the availability of the involved persons may become critical.
VMT members and responders should timely report expected absence to each other, and to VMT peers or the AC if necessary.
Involve more maintainers if necessary.

### 4. Follow up on stale vulnerabilities

Identify vulnerabilities that have not received timely action.
Ping the relevant maintainers to request updates and drive progress toward resolution.
Pay special attention to reports with embargo expiration dates, as those may not be negotiable.
If responders become unavailable, start looking for new volunteers.

The VMT should do periodic reviews of report states.
If the amount of stale reports becomes too high, the situation should be discussed at least between the VMT members, but possibly also with the AC.
Naturally, this discussion should happen in a closed meeting, but the AC may decide to inform the community about the load and ask for help.

### 5. Ensure fixes land within a release

Once a maintainer proposes a fix and other maintainers agree on the approach:

1. Coordinate with the release manager for the target release.
1. Send embargo communications as needed.
1. Ensure the fix is included in the agreed release.

The exact process of merging embargoed fixes is out of scope for this document.

### 6. Escalation

In case an individual VMT member can't make progress, they first escalate to their VMT peers to ask for help.
If the VMT in total can't help with progress, they escalate the situation to the AC (in the VMT Slack channel, or as a last resort by mentioning it in the community call, obviously without disclosing details).

## Not a responsibility

**Fixing reported vulnerabilities is not a VMT responsibility.**

VMT members coordinate triage, communication, and release alignment.
Implementation and review of fixes remain with the maintainers of the affected components.
Notwithstanding the above, a VMT member handling a report may elect to fix a vulnerability as a fellow maintainer.

## Criteria for VMT membership

Candidates must meet all of the following criteria:

### Familiarity with the project

Members must be familiar with Kata Containers, its architecture, and its development workflows.

Because this is difficult to measure directly, one proposed requirement is a minimum number of code reviews per month.
Active review participation helps ensure ongoing familiarity with the codebase and project practices.

### Neutrality

People from any company, or no company at all, are welcome on the VMT.
However, members must handle vulnerability information responsibly and must not allow any organization to gain an unfair advantage, for example, by exploiting knowledge of a vulnerability that has not been fixed yet, or by fixing it privately before the coordinated public release.
You can inform your employer, significant other etc. that you are working on a vulnerability, but you must not disclose the vulnerability itself!

### Acceptance by the Architecture Committee

Membership requires approval by the Architecture Committee (AC).
The AC may accept or deny a candidate after internal discussion, at its discretion.
The current members of the VMT are listed on a kata-containers/community page.

### Term limit

A VMT member is appointed for 6 months.
There is no limit on the number of appointments for a given individual.

## Criteria for removal from the VMT

A member may be removed from the VMT by AC decision.
The AC decision to remove a member comes with a public justification.
A natural reason for removal could be failure to perform the required duties described in the **Responsibilities** section, but the AC can remove a VMT member for any reason.

## Request to Downstream Stakeholders

If your company relies on Kata Containers, consider nominating or assigning someone to participate in the VMT.

Broad participation from downstream users and vendors strengthens coverage, neutrality, and the project's ability to respond to security issues in a timely and coordinated manner.
