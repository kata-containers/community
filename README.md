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
        * [Maintainer](#maintainer)
    * [Architecture Committee](#architecture-committee)
* [Vendoring code](#vendoring-code)
* [Vulnerability Handling](#vulnerability-handling)
    * [Reporting Vulnerabilities](#reporting-vulnerabilities)
    * [Vulnerability Disclosure Process](#vulnerability-disclosure-process)
* [Week in Review template](#week-in-review-template)

# About Kata Containers

Kata Containers is an open source project and community working to build a standard implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload isolation and security advantages of VMs.

The Kata Containers project will initially comprise six components, including the Agent, Runtime, Proxy, Shim, Kernel and packaging of QEMU 2.9. It is designed to be architecture agnostic, run on multiple hypervisors and be compatible with the OCI specification for Docker containers and CRI-O for Kubernetes.

Kata Containers combines technology from [Intel® Clear Containers](https://github.com/clearcontainers/runtime) and [Hyper runV](https://github.com/hyperhq/runv). The code is hosted on GitHub under the Apache 2 license and the project is managed by the OpenStack Foundation. To learn more about the project and organizations backing the launch, visit https://www.katacontainers.io.

# Community

Kata Containers is working to build a global, diverse and collaborative community. Anyone who is interested in supporting the technology is welcome to participate. Learn how to contribute on the [Community pages](https://katacontainers.io/community/). We are seeking different expertise and skills, ranging from development, operations, documentation, marketing, community organization and product management.

## Join Us

You can join our community on any of the following places:

* Join our [mailing list](http://lists.katacontainers.io/).

* Use the `irc.freenode.net` IRC server to join the discussions:
  * General discussions channel: [`#kata-general`](http://webchat.freenode.net/?channels=kata-general).
  * Development discussions channel: [`#kata-dev`](http://webchat.freenode.net/?channels=kata-dev).

* Get an [invite to our Slack channel](https://bit.ly/katacontainersslack),
  and then [join us on Slack](https://katacontainers.slack.com/).

* Follow us on [Twitter](https://twitter.com/KataContainers) or
  [Facebook](https://www.facebook.com/KataContainers).

## Users

See [Kata Containers installation user guides](https://github.com/kata-containers/documentation/blob/master/install/README.md) for details on how to install Kata Containers for your preferred 
distribution.

## Contributors

See the [contributing guide](CONTRIBUTING.md) for details on how to contribute to the project.

## Review Team

See the [rota documentation](Rota-Process.md).

## Resource Owners

Details of which Kata Containers project resources are owned, managed or controlled by whom
are detailed on the [Areas of Interest](https://github.com/kata-containers/community/wiki/Areas-of-interest) wiki page, under the [Resource Owners](https://github.com/kata-containers/community/wiki/Areas-of-interest#resource-owners) section.

# Governance

The Kata Containers project is governed according to the ["four opens"](https://governance.openstack.org/tc/reference/opens.html), which are open source, open design, open development, and open community. Technical decisions are made by technical contributors and a representative Architecture Committee. The community is committed to diversity, openness, and encouraging new contributors and leaders to rise up.

## Developers

For code contributors, there are currently two roles relevant to project governance:

### Contributor

A Contributor to the Kata Containers project is someone who has had code merged within the last 12 months. Contributors are eligible to vote in the Architecture Committee elections. Contributors have read only access to the Kata Containers repos on GitHub.

### Maintainer

A Maintainer has the ability to merge code into the Kata Containers project. Maintainers are active Contributors and participants in the projects. In order to become a Maintainer, you must be nominated and approved by the established Maintainers. Maintainers have write access to the Kata Containers repos on GitHub.

## Architecture Committee

The Architecture Committee is responsible for architectural decisions, including standardization, and making final decisions if Maintainers disagree. It is comprised of 5 members, who are elected by contributors.

The current Architecture Committee members are:

- `Eric Ernst` ([`egernst`](https://github.com/egernst)), [Apple](https://apple.com/).
- `Samuel Ortiz` ([`sameo`](https://github.com/sameo)), [Intel](https://www.intel.com).
- `Justin He` ([`justin-he`](https://github.com/justin-he)), [ARM](https://www.arm.com).
- `Xu Wang` ([`gnawux`](https://github.com/gnawux)), [Ant Financial](https://www.antfin.com/index.htm?locale=en_US).
- `Haomin Tsai` ([`jshachm`](https://github.com/jshachm)), [Huawei](http://www.huawei.com).

Architecture Committee elections take place in September (3 seats available) and February (2 seats available). Anyone who has made contributions to the project will be eligible to run, and anyone who has had code merged into the Kata Containers project in the 12 months (a Contributor) before the election will be eligible to vote. There are no term limits, but in order to encourage diversity, no more than 2 of the 5 seats can be filled by any one organization. The Architecture Committee will meet regularly in an open forum with times and locations published in community channels.

The exact size and model for the Architecture Committee may evolve over time based on the needs and growth of the project, but the governing body will always be committed to openness, diversity and the principle that technical decisions are made by technical contributors.

See [the elections documentation](elections) for further details.

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
