# Downstream stakeholders notification email (private issues) template

```txt
-   To: <embargo-notice@lists.katacontainers.io>
-   *Subject:* \[pre-GHSA\] Vulnerability in Kata Containers $COMPONENTS ($CVE)

This is an advance warning of a vulnerability discovered in
Kata Containers, to give you, as downstream stakeholders, a chance to
coordinate the release of fixes and reduce the vulnerability window.
Please treat the following information as confidential until the
proposed public disclosure date.

$DESCRIPTION

Proposed patch: See attached patches.
Unless a flaw is discovered in them, these patches will be merged to
the main branch on the public disclosure date.

CVE: $CVE

Proposed public disclosure date/time:
YYYY-MM-DD, XXXXUTC
Please do not make the issue public (or release public patches)
before this coordinated embargo date.

Original private report:
https://github.com/kata-containers/kata-containers/security/advisories/GHSA-xxxx-xxxx-xxxx
For access to read and comment on the security report, please reply to me
with your *GitHub* username and I will subscribe you.
-- 
$VMT_COORDINATOR_NAME on behalf of the Kata Containers VMT
```

Use `git` to produce attachment files for the candidate patches:

```sh
output_directory=/tmp/patches
mkdir -p ${output_directory}
git format-patch --no-signature -o ${output_directory} main
```
