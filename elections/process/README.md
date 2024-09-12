# Election Process

The election process is administered and guided by
the Election Officials.

This group is responsible for working with the
Architecture Committee (AC) on the election timeline,
performing the preparation steps and carrying out all
required communications.

## Pick election officials
Election officials should not run in the election themselves.
Ideally they should also have no interest in the election
outcome (to preserve neutrality) but that is generally
harder to achieve.

Election officials should be identified by no later than a
week prior to the start of the election.

# Selecting Election Dates
Things to keep in mind when selecting election dates:

- Try to avoid overlapping with big in-person events
  in the interest for the community or major public holidays
- Allow enough time for the contributors to decide if they
  are planning to run, and fulfill all the requirements to be
  able to participate
- Allow at least a week for nomination and campaign periods
- The current AC needs to approve the timeline once there
  is a proposal
  
# Preparation
As early as possible but at least a month before election
starts:

- Edit elections details (timeline, elected positions, deadlines)
  in the [community repo](https://github.com/kata-containers/community/tree/main/elections)
- Create the PR to update the information on GitHub

A couple of weeks before election starts:

- Post information about the upcoming election on the
  kata-dev mailing list and on Slack
- Generate an initial electorate list and share it with the
  AC and community to ensure that the list contains all active
  contributors

# During the election
## AC Nomination Round
When AC nomination period starts:

- Send Kata AC Nomination period started email to kata-dev
- Announce the start of the nomination period on Slack
- Generate the final electorate list

Email and Slack announcement tips:
- Introduce yourself as election official
- Announce start of process
- List seats up for reelection
- Provide timeline overview
- Describe candidacy process
- Describe voting eligibility
- Link to references from kata-containers/community
- Example email from an earlier cycle: [draft Etherpad](https://etherpad.opendev.org/p/r.256a531373da9595cf4c3af45bd58782)

During the AC Candidacy round:
- Election officials review the nominations on GitHub
- A couple of days before the candidacy submission ends send
  reminders to the mailing list and Slack
  - Mention this is the last call for candidate nomination
  - Mention specifically the nomination deadline, and the
    full timeline
  - Example email from an earlier cycle:
  	[September 2020 Kata Containers Architecture Committee elections candidate nomination reminder](https://lists.katacontainers.io/pipermail/kata-dev/2020-September/001512.html)

When AC Candidacy submission ends:

- Send Kata AC election - Nomination period ended email

Once the email deadline is reached:

- Check if there are enough candidate to run the election
  - If yes, generate the electorate rolls and move forward with
    the next steps of the process
  - If not, reach out to the AC and have the active members
    (whose seats are not up for re-election) officiate the results
    before the last steps of administration

# AC Campaigning
The AC election includes a period after the candidates are defined
but before the election, for candidates to answer questions from
the community.

Open this with Kata AC election - Campaign period started email, and
also announce it on Slack.

# AC Election Round
Before AC Election begins:

- Create CIVS page
  - Title the poll: <Year> <H1/H2> Kata Architecture Committee Election Poll
  - Enable detailed ballot reporting
  - Send to other officials to verify
  - Check number of seats
  - Check closing date


When AC Election begins:

- Upload rolls
- CIVS has a maximum number of electorate emails you can upload at a time without
  crashing, limit to 500 at a time
- Send Kata AC election - Voting period started email, and announce the start
  of the voting period on Slack

A couple of days before the AC Election ends:

- Send Kata AC election - Voting period started reminder email and Slack
  note
  
Ending the Kata AC Election:

- Close the election and send Kata AC election - Voting period ended email, and
  announcement on Slack
- Update the list of AC members and their terms on GitHub and create a PR
- Send Kata AC Election Results email and Slack update
