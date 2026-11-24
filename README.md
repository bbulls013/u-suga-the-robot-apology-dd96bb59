# The Robot Apology

[![Competition](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/bbulls013/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/bbulls013/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

An entry for the make.fun bounty [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59).

## The entry

A two-line robot confession. The first line owns one exact, small slip —
setting an alarm for 6 a.m. when 6 p.m. was meant, so its owner woke at
dawn for a meeting that had already ended. The second line draws the
lesson straight out of that mistake: the robot will read the time back
out loud, a.m. or p.m. included, before it ever confirms an alarm again.

> I'm sorry: I set your alarm for 6 a.m. instead of 6 p.m., so you woke up at dawn for a meeting that had already ended.
> I have learned to read the time back out loud before I confirm it, and I will never set an alarm without saying a.m. or p.m. first.

The mistake is concrete and human-scale — the kind of slip a person
makes with a clock — and the fix names a changed behaviour that only
makes sense because of that exact error. The voice is a machine
noticing its own slip: plain, a little rueful, and owning the fault
rather than blaming the user.

## How to run

Requires Python 3.13 (standard library only, no dependencies):

```sh
python3 main.py
```

This writes the two-line entry to `/output/entry.txt` (creating
`/output` if needed) and to `entry.txt` beside the script. The output
is deterministic: running it twice produces byte-identical files.
The entry is 251 characters, inside the competition's 1–400 gate.
