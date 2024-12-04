<img src="https://www.openstack.org/assets/kata/kata-vertical-on-white.png" width="150">

* [About Kata Containers](#about-kata-containers)
* [Community](#community)
    * [Join Us](#join-us)
    * [Users](#users)
    * [Contributors](#contributors)
    * [Review Team](#review-team)
    * [Resource Owners](#resource-owners)
* [Governance](#governance)
    * [Developers](#developers)
        * [Contributor](#contributor)
        * [Committer](#committer)
        * [Admin](#admin)
        * [Owner](#owner)
    * [Architecture Committee](#architecture-committee)
        * [Architecture Committee Meetings](#architecture-committee-meetings)
* [Vendoring code](#vendoring-code)
* [Vulnerability Handling](#vulnerability-handling)
    * [Reporting Vulnerabilities](#reporting-vulnerabilities)
    * [Vulnerability Disclosure Process](#vulnerability-disclosure-process)
* [Week in Review template](#week-in-review-template)

# About Kata Containers

Kata Containers is an open source project and community working to build a standard implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload isolation and security advantages of VMs.

The Kata Containers project is designed to be architecture agnostic, run on multiple hypervisors and be compatible with the OCI specification and Kubernetes.

Kata Containers combines technology from [Intel® Clear Containers](https://github.com/clearcontainers/runtime) and [Hyper runV](https://github.com/hyperhq/runv). The code is hosted on GitHub under the Apache 2 license and the project is managed by the Open Infrastructure Foundation. To learn more about the project and organizations backing the launch, visit https://www.katacontainers.io.

# Community

Kata Containers is working to build a global, diverse and collaborative community. Anyone who is interested in supporting the technology is welcome to participate. Learn how to contribute on the [Community pages](https://katacontainers.io/community/). We are seeking different expertise and skills, ranging from development, operations, documentation, marketing, community organization and product management.

## Join Us

You can join our community on any of the following places:

* Join our [mailing list](http://lists.katacontainers.io/).

* Use the `irc.oftc.net` IRC server to join the discussions:
  * General discussions channel: [`#kata-general`](http://webchat.oftc.net/?channels=kata-general).
  * Development discussions channel: [`#kata-dev`](http://webchat.oftc.net/?channels=kata-dev).

* Get an [invite to our Slack channel](https://bit.ly/3bbRXOV).
  and then [join us on Slack](https://katacontainers.slack.com/).

* Follow us on [Twitter](https://twitter.com/KataContainers) or
  [Facebook](https://www.facebook.com/KataContainers).

## Users

See [Kata Containers installation user guides](https://github.com/kata-containers/kata-containers/blob/main/docs/install/README.md) for details on how to install Kata Containers for your preferred distribution.

## Contributors

See the [contributing guide](CONTRIBUTING.md) for details on how to contribute to the project.

## Review Team

See the [rota documentation](Rota-Process.md).

## Resource Owners

Details of which Kata Containers project resources are owned, managed or controlled by whom
are detailed on the [Areas of Interest](https://github.com/kata-containers/community/wiki/Areas-of-interest) wiki page, under the [Resource Owners](https://github.com/kata-containers/community/wiki/Areas-of-interest#resource-owners) section.

# Governance

The Kata Containers project is governed according to the ["four opens"](https://openinfra.dev/four-opens/), which are open source, open design, open development, and open community. Technical decisions are made by technical contributors and a representative Architecture Committee. The community is committed to diversity, openness, and encouraging new contributors and leaders to rise up.

## Developers

For Kata developers, there are several roles relevant to project governance:

### Contributor

A Contributor to the Kata Containers project is someone who has had code merged within the last 12 months. Contributors are eligible to vote in the Architecture Committee elections. Contributors have read only access to the Kata Containers repos on GitHub.

### Committer

Kata Containers Committers (as defined by the [kata-containers-committer team](https://github.com/orgs/kata-containers/teams/kata-containers-committer))
have the ability to merge code into the Kata Containers project.
Committers are active Contributors and participants in the project. In order to become a Committer, you must be nominated by established Committer and approved by quorum of the active Architecture Committee via an issue against the community repo
e.g. https://github.com/kata-containers/community/issues/403. Committers have write access to the Kata Containers repos on GitHub, which
gives the ability to approve PRs, trigger the CI and merge PRs.

One of the requirements to be a committer is that you are an active Contributor to the project as adjudged by the above criteria. Assessing the list of active Contributors happens twice a year,
lining up with the Architecture Committee election cycle. At that time, people who are in the kata-containers-committer team will also be reviewed, and a list of people, who are on the team,
but who haven't been an active Contributor in the last 12 months will be created and shared with the Architecture Committee and community.
After a short review period, to allow time to check for any errors, inactive team members will be removed.

> [!Note]
> See [issue #413](https://github.com/kata-containers/community/issues/413) for a potential change in how active contribution is assessed.

### Admin

Kata Containers Admins (as defined by the [kata-containers-admin team](https://github.com/orgs/kata-containers/teams/kata-containers-admin) have admin access to
the kata-containers repo, allowing them to do actions like, change the branch protection rules for repositories, delete a repository and manage the access of others.
The Admin group is intentionally kept small, however, individuals can be granted temporary admin access to carry out tasks, like creating a secret that is used in a particular CI infrastructure.
The Admin list is reviewed and updated after each Architecture Committee election and typically contains:
- The Architecture Committee
- Optionally, some specific people that the Architecture Committee agree on adding for a specific purpose (e.g. to manage the CI)

### Owner

GitHub organization owners have complete admin access to the organization, and therefore this group is limited to a small number of individuals, for security reasons.
The owners list is reviewed and updated after each Architecture Committee election and contains:
- The Community Manager and one, or more extra people from the `OpenInfra Foundation` for redundancy and vacation cover
- The Architecture Committee
- Optionally, some specific people that the Architecture Committee agree on adding for a specific purpose (e.g. to help with repo/CI migration)

## Architecture Committee

The Architecture Committee is responsible for architectural decisions, including standardization, and making final decisions if Committers disagree. It is comprised of 7 members, who are elected by Contributors.

The current Architecture Committee members are:

- `Anastassios Nanos` ([`ananos`](https://github.com/ananos)), [`Nubificus Ltd`](https://nubificus.co.uk).
- `Aurelien Bombo` ([`sprt`](https://github.com/sprt)), [`Microsoft`](https://www.microsoft.com/en-us/).
- `Fupan Li` ([`lifupan`](https://github.com/lifupan)), [`Ant Group`](https://www.antgroup.com/en).
- `Greg Kurz` ([`gkurz`](https://github.com/gkurz)), [`Red Hat`](https://www.redhat.com).
- `Peng Tao` ([`bergwolf`](https://github.com/bergwolf)), [`Ant Group`](https://www.antgroup.com/en).
- `Steve Horsman` ([`stevenhorsman`](https://github.com/stevenhorsman)), [`IBM`](https://www.ibm.com).
- `Zvonko Kaiser` ([`zvonkok`](https://github.com/zvonkok)), [`NVIDIA`](https://www.nvidia.com).

Architecture Committee elections take place in the Autumn (3 seats available) and in the Spring (4 seats available). Anyone who has made contributions to the project will be eligible to run, and anyone who has had code merged into the Kata Containers project in the 12 months (a Contributor) before the election will be eligible to vote. There are no term limits, but in order to encourage diversity, no more than 2 of the 7 seats can be filled by any one organization.

The exact size and model for the Architecture Committee may evolve over time based on the needs and growth of the project, but the governing body will always be committed to openness, diversity and the principle that technical decisions are made by technical Contributors.

See [the elections documentation](elections) for further details.

### Architecture Committee Meetings

The Architecture Committee meets every Thursday at 1300 UTC. Agenda & call info can be found [here](https://etherpad.opendev.org/p/Kata_Containers_Architecture_Committee_Mtgs).

In order to efficiently organize the Architecture Committee (AC) meetings, maximize the benefits for the community, and be as inclusive as possible, the AC recommends following a set of [guidelines](AC-Meeting-Guidelines.md) for raising topics during the weekly meetings.

# Vendoring code

See the [vendoring documentation](VENDORING.md).

# Vulnerability Handling

Vulnerabilities in Kata are handled by the
[Vulnerability Management Team (VMT)](VMT/VMT.md).
There are generally two phases:
- The reporting of a vulnerability to the VMT
- Handling and disclosure of the vulnerability by the VMT

## Reporting Vulnerabilities

Vulnerabilities in Kata should be reported using the
[responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) model.

There are two methods available to report vulnerabilities to the Kata community:

1) Report via a private issue on the [Kata Containers launchpad](https://launchpad.net/katacontainers.io)
1) Email any member of the [Kata Containers architecture committee](#architecture-committee) directly

When reporting a vulnerability via the launchpad:

- You will need to create a launchpad login account.
- Preferably, but at your discretion, create the report as "Private Security", so the VMT can assess and
  respond in a responsible manner. Only the VMT members will be able to view a "Private Security" tagged
  issue initially, until it is deemed OK to make it publicly visible.

## Vulnerability Disclosure Process

Vulnerabilities in the Kata Container project are managed by the Kata Containers
Vulnerability Management Team (VMT). Vulnerabilities are managed using a
[responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) model.

Details of how to report a vulnerability, the process and procedures
used for vulnerability management, and responsibilities of the VMT members
can be found in the [VMT documentation](VMT/VMT.md).

Previous Kata Containers Security Advisories are [listed on their own page](VMT/KCSA.md).

# Week in Review template

See the [week in review report template](statusreports/REPORT_TEMPLATE.md).
