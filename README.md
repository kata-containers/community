<img src="https://www.openstack.org/assets/kata/kata-vertical-on-white.png" width="150">

* [About Kata Containers](#about-kata-containers)
* [Community](#community)
    * [Join Us](#join-us)
    * [Users](#users)
    * [Contributors](#contributors)
* [Governance](#governance)
    * [Developers](#developers)
        * [Contributor](#contributor)
        * [Maintainer](#maintainer)
    * [Architecture Committee](#architecture-committee)
    * [Working Committee](#working-committee)

# About Kata Containers

Kata Containers is an open source project and community working to build a standard implementation of lightweight Virtual Machines (VMs) that feel and perform like containers, but provide the workload isolation and security advantages of VMs.

The Kata Containers project will initially comprise six components, including the Agent, Runtime, Proxy, Shim, Kernel and packaging of QEMU 2.9. It is designed to be architecture agnostic, run on multiple hypervisors and be compatible with the OCI specification for Docker containers and CRI-O for Kubernetes.

Kata Containers combines technology from [Intel® Clear Containers](https://github.com/clearcontainers/runtime) and [Hyper runV](https://github.com/hyperhq/runv). The code is hosted on Github under the Apache 2 license and the project is managed by the OpenStack Foundation. To learn more about the project and organizations backing the launch, visit https://www.katacontainers.io.

# Community

Kata Containers is working to build a global, diverse and collaborative community. Anyone who is interested in supporting the technology is welcome to participate. We are seeking different expertise and skills, ranging from development, operations, documentation, marketing, community organization and product management.

## Join Us

You can join our community on any of the following places:

* Join our [mailing list](http://lists.katacontainers.io/).
* Use IRC on IRC.freenode.net to join discussions on [#kata-dev](http://webchat.freenode.net/?channels=kata-dev) and [#kata-general](http://webchat.freenode.net/?channels=kata-general).
* Get an [invite to our Slack channel](http://bit.ly/KataSlack), and then [join us on Slack](https://katacontainers.slack.com/).
* Follow us on [Twitter](https://twitter.com/KataContainers) or [Facebook](https://www.facebook.com/KataContainers).

## Users

See [Kata Containers installation user guides](https://github.com/kata-containers/documentation/blob/master/install/README.md) for details on how to install Kata Containers for your preferred 
distribution.

## Contributors

See the [contributing guide](CONTRIBUTING.md) for details on how to contribute to the project.

# Governance

The Kata Containers project is governed according to the [“four opens"](https://governance.openstack.org/tc/reference/opens.html), which are open source, open design, open development, and open community. Technical decisions are made by technical contributors and a representative Architecture Committee. The community is committed to diversity, openness, and encouraging new contributors and leaders to rise up.

## Developers

For code contributors, there are currently two roles relevant to project governance:

### Contributor

A Contributor to the Kata Containers project is someone who has had code merged within the last 12 months. Contributors are eligible to vote in the Architecture Committee elections. Contributors have read only access to the Kata Containers repos on Github.

### Maintainer

A Maintainer has the ability to merge code into the Kata Containers project. Maintainers are active Contributors and participants in the projects. In order to become a Maintainer, you must be nominated and approved by the established Maintainers. Maintainers have write access to the Kata Containers repos on Github.

## Architecture Committee

The Architecture Committee is responsible for architectural decisions, including standardization, and making final decisions if Maintainers disagree. It will be comprised of 5 members, who are appointed by the Maintainers at launch but fully elected by Contributors within the first year.

The initial Architecture Committee members are:

- Jess Frazelle ([`jessfraz`](https://github.com/jessfraz)), [Microsoft](https://www.microsoft.com/).
- Samuel Ortiz ([`sameo`](https://github.com/sameo)), [Intel](https://www.intel.com).
- Tim AllClair ([`tallclair`](https://github.com/tallclair)), [Google](https://www.google.com).
- Xu Wang ([`gnawux`](https://github.com/gnawux)), [HyperHQ](https://hyper.sh).
- Zhang Wei ([`WeiZhang555`](https://github.com/WeiZhang555)), [Huawei](http://www.huawei.com).

In September 2018, 3 of the 5 seats will be up for election by the project Contributors. Anyone who has made contributions to the project will be eligible to run, and anyone who has had code merged into the Kata Containers project in the last 12 months (a Contributor) will be eligible to vote. In February 2019, the remaining 2 seats of the Architecture Committee will be up for election. The elections will continue on this staggered cycle (3 seats and 2 seats) every six months in order to allow new leaders to rise up, but also ensure some consistency across the terms. There are no term limits, but in order to encourage diversity, no more than 2 of the 5 seats can be filled by any one organization. The Architecture Committee will meet regularly in an open forum with times and locations published in community channels.

The exact size and model for the Architecture Committee may evolve over time based on the needs and growth of the project, but the governing body will always be committed to openness, diversity and the principle that technical decisions are made by technical contributors.

## Working Committee

The Working Committee is intended to make non-technical decisions and help influence the project strategy, including marketing and communications, product management and ecosystem support. Representatives are expected to be active contributors who are committed to the health and success of the project.

Recognizing the project will grow and change quickly in the first six months, and in order to encourage diversity and participation, the Working Committee will be forming up and finalizing its structure after the project launch.

Initial appointed members include:

- Amy Leeland ([`amyleeland`](https://github.com/amyleeland)), [Intel](https://www.intel.com).
- James Kulina ([`jmknyc06`](https://github.com/jmknyc06)), [HyperHQ](https://hyper.sh).

During this initial period, the participants will appoint a leader to help organize and run regular meetings, coordinate the various workstreams and help define the long-term structure. The initial task will be to determine 2018 plans and appropriate work streams, working groups and funding to execute on those plans.

The estimated size of the Working Committee is 7 members, but there is opportunity for more contributors to get involved in various sub-teams working on specific topics, such as product management or conformance. The Working Committee will meet regularly in an open forum with times and locations published in community channels.
