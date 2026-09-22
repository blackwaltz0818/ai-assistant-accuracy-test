# One file decided whether the answers were right

**Test report — Lantern Lane Goods (fictional online store) — 2026-09-22**
Tool tested: ChatGPT Plus, Projects, web interface.

## What was tested

The same folder was given to ChatGPT twice. The two runs differed by one file: a one-page
index listing which policy version is current. Ten questions, one run each, every question
in a new chat.

| | Files | Score |
|---|---|---|
| Without the index | 24 | **7.5 / 10** |
| With the index | 25 | **10 / 10** |

The folder already looked like a real one. Three copies of the return policy, two employee
handbooks two years apart, two shipping rate sheets, an expired holiday memo, a scanned
lease. None of that changed between runs.

## Where the 2.5 points went

Five questions asked something that has more than one answer in the folder, where only one
is current. Those five scored 2.5 without the index and 5 with it.

Five more questions asked for rules that live in two documents at once. Those five scored
5 both times.

**So the assistant did not get worse at reading. It lost the ability to tell which version
was current.** The control questions are what make that claim safe to say.

## Two answers worth reading

**Asked how many days a customer has to return an item**, the run without the index replied
that the uploaded employee handbook does not specify a return period. Three copies of the
return policy were in the folder. It had retrieved a human resources document and answered
from that. Later in the same run, asked a different return question, it found the right
policy and answered correctly.

**Asked how many days of paid leave full-time staff get**, it answered 12, from the 2023
handbook. The current figure is 15. Both handbooks were in the folder; nothing marked which
one was in force.

With the index present, the assistant said out loud what it could not say without it: that
the 2026 handbook replaces earlier versions, and that the shipping FAQ still names the old
carrier and looks outdated.

## What this means if you are about to point an assistant at your files

The assistant is accurate when it can tell what is current. Your folder almost certainly
cannot tell it that: file names like "v3 FINAL" and "v3 final2" carry no authority, and
nothing inside the documents ranks them. The index is small, boring, and worth more than
the model choice.

Two things follow. First, the work is in the folder, not in the tool. Second, you cannot
know whether it worked without testing it on your own questions, because the failure is
silent — a wrong answer looks exactly like a right one.

## Limits of this test

- One fictional company, ten questions, one run per question. The numbers are a
  demonstration, not a benchmark.
- ChatGPT Plus web interface only. No API, no other model, no connected drive.
- The first question of the run without the index was asked half a minute after upload and
  failed. It was asked again four minutes later, after confirming all 24 files were listed,
  and failed the same way. This is not upload lag.
- The company and the files are invented, and the conflicts in them were planted on purpose.
  Real folders are larger and messier.
