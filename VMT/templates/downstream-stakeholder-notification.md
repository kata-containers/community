# Downstream stakeholders notification email (private issues) template

We send two separate emails, to avoid off-topic replies to Linux-distros:

```
-   To: <embargo-notice@lists.katacontainers.io>
-   To: <linux-distros@vs.openwall.org>
```

Subject and content for both emails is identical:

```
-   *Subject:* \[pre-KCSA\] Vulnerability in Kata Containers $COMPONENTS ($CVE)

This is an advance warning of a vulnerability discovered in
Kata Containers, to give you, as downstream stakeholders, a chance to
coordinate the release of fixes and reduce the vulnerability window.
Please treat the following information as confidential until the
proposed public disclosure date.

$DESCRIPTION

Proposed patch: See attached patches.
Unless a flaw is discovered in them, these patches will be merged to
their corresponding branches on the public disclosure date.

CVE: $CVE

Proposed public disclosure date/time:
YYYY-MM-DD, 0000UTC
Please do not make the issue public (or release public patches)
before this coordinated embargo date.

Original private report:
https://bugs.launchpad.net/katacontainers.io/+bug/$NNNNNN
For access to read and comment on this report, please reply to me
with your Launchpad username and I will subscribe you.
-- 
$VMT_COORDINATOR_NAME
Kata Containers Vulnerability Management Team
```

Proposed patches are attached, email must be GPG-signed.
Use something unique and descriptive for the patch attachment file names, for example `cve-2013-4183-master-agent.patch` or `cve-2013-4183-stable-1.2.1-agent.patch`.
