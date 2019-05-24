# Kata Containers security advisory (KCSA) template

The template used to construct the KCSA attached to a VMT Launchpad bug, and later
potentially published.

```
announcement-date: YYYY-MM-DD

id: KCSA-$NUM

title: '$TITLE'

description: '$DESCRIPTION_CONTENT'

affected-components:

  - components: $COMPONENTS
    version: $AFFECTED_VERSIONS

vulnerabilities:

  - cve-id: $CVE

reporters:

  - name: '$CREDIT'
    affiliation: $CREDIT_AFFILIATION
    reported:
      - $CVE

issues:

  links:
    - https://github.com/kata-containers/$COMPONENT/issues/$ISSUE_NR

 reviews:

  v1.2.3:
    - https://github.com/kata-containers/$COMPONENT/pull/$PR_NUMBER

  v2.3.4:
    - https://github.com/kata-containers/$COMPONENT/pull/$PR_NUMBER

  type: GitHub

reproduce:
  - 'Any information on how to reproduce or verify if a system is affected'

notes:
  - 'Optional note such as cross project version requirements,
    or details on how to reproduce and check for the vulnerability'
```

Once approved, the request will be added to the documentation repo and linked from the KCSA index page. It will then be emailed out.
We send two separate emails, to avoid off-topic replies to `oss-security` list:

```
-   To: <kata-dev@lists.katacontainers.io>
-   To: <oss-security@lists.openwall.com>
```

Subject and content for both emails is identical:

```
-   Subject: `\[KCSA-$NUM\] $TITLE ($CVE)`
-   Body: The KCSA markdown document
```

Notes:

-   Email must be GPG-signed.
-   $CVE must always be of the form CVE-YYYY-XXXX
-   $NUM is of the form YYYY-XX

