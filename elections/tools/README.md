
# Election Tools

This directory contains tools that can help generate the Kata Containers eligible
electorate details.

## `generate_electorate.py`

The `generate_electorate.py` tool gathers data from GitHub and generates a `YAML`
dataset containing the details of the eligible electorate for a defined date range.

This tool needs the following python libraries:

* `pytz`
* `github3.py`
* `pyyaml`

To install them in a virtual environment do something like:

```bash
$ python3 -m venv .venv
$ .venv/bin/pip install pytz github3.py pyyaml
```

Before running the tool you will need to create a
[GitHub API token](https://github.blog/2013-05-16-personal-api-tokens/)

replace `__API_TOKEN__` in the script with your personal token.

Also update the election start and end times to cover the period being
examined for this election period. The lines to edit look like:

```python
start_time = datetime.datetime(2018, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
end_time = datetime.datetime(2018, 8, 1, 0, 0, 0, tzinfo=pytz.UTC)
```

Then run the tool with:

```bash
$ .venv/bin/python ./generate_electorate.py
```

The code looks at all commits in all Kata Containers repos *except*
`kata-containers/linux` and `kata-containers/qemu`. As both of these are forks
(in the GitHub sense) they'll have lots of contributors that may not be Kata
contributors.

For contributors that have more than one email address it picks one as default
but supplies all the others so  we can be smarter about where to send the
emails.

The sources for email addresses are:
* GitHub account
* Git commit data
* Look for a `Signed-Off-By` line in the commit message

The GitHub login is always stored so that is the primary identifier.

## Output results

As the script runs it prints a summary on `stdout`. When the script has completed it places the
generated data into a file called `electorate.yaml`. Use this file to send the bulk email notification
to the eligible electorate.
