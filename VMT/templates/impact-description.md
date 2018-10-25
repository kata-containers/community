# Impact description ($DESCRIPTION) template

```
Title: $TITLE
Reporter: $CREDIT
Projects: $COMPONENTS
Affects: $AFFECTED_VERSIONS

Description:
$CREDIT reported a vulnerability in [project feature name].
By doing [action] a [actor] may [impact] resulting in [consequence].
Only [project deployment mode] are affected.
```

The AFFECTED_VERSIONS needs to stay valid after the fix is released.
For example, when v1.2.1 and v1.3.2 are still security supported, the AFFECTED_VERSIONS of should read like this:

```
Affects: >=v1.2.0 <=v1.2.1, >=v1.3.2 <=v1.3.2
```

Once v1.2.x reaches end of life, that line becomes:

```
Affects: >=v1.3.2 <=v.1.3.2
```

If the oldest version affected is not easily identified, leave it open-ended:

```
Affects: <=v1.2.1 and ==v1.3.2
```
