# Kata Containers Security Advisories

* [Kata Containers Security Advisories](#kata-containers-security-advisories)
    * [KCSA summary](#kcsa-summary)
    * [Determine Kata Containers version](#determine-kata-containers-version)
    * [Upgrade](#upgrade)

## KCSA summary

This table lists all previously published Kata Containers Security Advisories ([KCSA]'s), newest first:

| Date       | [KCSA]                                             | Affected Versions  | Description                                         |
| ---------- | -------------------------------------------------- | ------------------ | --------------------------------------------------- |
| 2020-11-17 | [KCSA-CVE-2020-28914](KCSA/KCSA-CVE-2020-28914.md) | < 1.11.5           | Improper file permissions for read-only volumes     |
| 2020-06-12 | [KCSA-CVE-2020-2026](KCSA/KCSA-CVE-2020-2026.md)   | < 1.10.5, < 1.11.1 | Improper link resolution before file access         |
| 2020-06-12 | [KCSA-CVE-2020-2023](KCSA/KCSA-CVE-2020-2023.md)   | < 1.11.1           | Execution with unnecessary privileges               |
| 2020-05-28 | [KCSA-CVE-2020-2025](KCSA/KCSA-CVE-2020-2025.md)   | < 1.11.0           | Cloud Hypervisor guest image persists vulnerability |
| 2020-05-28 | [KCSA-CVE-2020-2024](KCSA/KCSA-CVE-2020-2024.md)   | < 1.11.0           | Improper link resolution vulnerability              |
| 2019-02-22 | [KCSA-CVE-2019-5736](KCSA/KCSA-CVE-2019-5736.md)   | *not applicable*   | `runc` container breakout                           |

## Determine Kata Containers version

To determine which version of Kata Containers you are running, see the
[upgrading document](https://github.com/kata-containers/kata-containers/blob/2.0-dev/docs/Upgrading.md#determine-current-version).

## Upgrade

If you are running a version of Kata Containers affected by one or more [KCSA]'s,
you are strongly encouraged to upgrade as soon as possible:

- [Kata 1.x upgrading document](https://github.com/kata-containers/documentation/blob/master/Upgrading.md)
- [Kata 2.x upgrading document](https://github.com/kata-containers/kata-containers/blob/2.0-dev/docs/Upgrading.md)


[KCSA]: https://github.com/kata-containers/community/blob/master/VMT/VMT.md#acronyms
