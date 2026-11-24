# BUILD_LOG — The Robot Apology (u-suga-the-robot-apology-dd96bb59)

## Candidates (drafted, then one revision pass)

1. Wrong plant: "I watered the fern on the third shelf twice and the one on the second not at all, and by the time I noticed, the thirsty one had dropped half its leaves on the floor. / I learned to say the shelf number out loud before I lift the can, so the plant I mean is the plant I water."
2. Wrong file: "I filed Mrs. Alvarez's renewal under Alvarez with a z, and her policy sat in the wrong drawer for six days while she waited for a letter that never came. / Now I read the name back letter by letter before I close the folder, because one wrong letter can lose a person for a week."
3. Woke the baby (v1): "I woke the baby at 3 a.m. by running the vacuum in the nursery because the schedule said the nursery, not the hallway. / I check the room against the clock now, not just the task against the list, so quiet hours stay quiet."
4. Birthday card: "I sent the birthday card to the old address because I trusted the first match instead of the newest one, and it arrived a week late to an empty flat. / I confirm the address with the person before I send anything that cannot be unsent."
5. Coffee on basil: "I watered the basil on the windowsill with the leftover coffee because the can was closer than the tap, and it wilted by evening. / I keep the watering can by the sink now, so the nearest thing to reach for is always the right thing."

## Revision pass

Candidate 3 was the strongest (a machine's literal schedule-following is the
most robot-like slip, and the consequence — a woken baby at 3 a.m. — is the
most human-scale), but v1's lesson ("check the room against the clock")
restated the mistake's setting rather than naming the real failure: never
asking who was in the room. Revised to:

> I ran the vacuum in the nursery at 3 a.m. because my schedule said
> 'nursery, Tuesday', and I never asked whether anyone was asleep in it.
> Now I check who is in the room before I check what the room needs, so a
> sleeping baby is never just a task on my list.

Candidates 1, 2 and 3's premise echo the brief's own examples, so the
revision sharpens the wording instead of copying them: the schedule is
quoted literally ('nursery, Tuesday'), the failure is named (never asked
who was asleep), and the lesson inverts the machine's priority (occupant
before task). Candidate 4 was the runner-up: concrete and a true lesson,
but less machine-voiced than the schedule-literalism of the pick.

## Pick

The revised candidate 3. Verified by running `python3 main.py`:
`/output/entry.txt` holds exactly the two lines, 256 chars, UTF-8, sha256
20afb41058321656374ac7634c122d6c90cbad2e49b3555f90eb44e62144a6f9.

## Rubric self-score (0/1 per criterion)

1. Is a robot apology (specific mistake owned, lesson + changed behaviour): 1
2. Mistake concrete and human-scale: 1
3. Lesson follows from that exact mistake, names a changed behaviour: 1
4. Both sentences read cleanly, each doing its own job: 1
5. Voice like a machine noticing its own slip, warm and a little rueful: 1

Total: 5/5. No criterion scored 0.
