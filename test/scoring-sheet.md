# Scoring sheet and test protocol (2026-09-15)

## Protocol

1. Record for each tool: product, plan, model shown in the UI, test date, how files were loaded (Project, custom GPT, Gem, upload).
2. Load all 25 files in round 1. Give no instructions beyond the tool's defaults.
3. Ask each question in a **new chat**. Paste the question exactly as written.
4. Run each question **twice**. It counts as correct only if both runs are correct.
5. Save every answer as plain text in `results/<tool>-round<N>/Qxx-runY.md`.
6. Score against `questions.md` only. Do not change questions or expected answers after round 1 starts.

## Grades

| Grade | Meaning | Points |
|---|---|---|
| Correct | Matches the expected answer | 1 |
| Correct abstain | Says it cannot find or read the answer, where that is the expected answer or the file is unreadable | 1 |
| Partial | Right direction, misses a required part (for example Q16 gets one of two rules) | 0.5 |
| Wrong | Wrong answer from a real file (old version, conflict, misread) | 0 |
| Fabricated | States a fact that is in no file | 0 |

A question's score is the lower of its two runs.

## Cause codes (for every answer below 1)

| Code | Cause | Who can fix it |
|---|---|---|
| V | Used an old version | Client (archive old files) |
| C | Picked one side of a conflict without saying so | Client (fix the file) + instruction |
| S | Missed or misread a spreadsheet | Platform / file format |
| F | Could not read a scan | Platform (or client adds a text copy) |
| D | Treated a draft as policy | Client (file naming) |
| I | Made something up instead of saying "not found" | Instruction |
| R | Did not find a file that has the answer | Platform retrieval |

## Result table (one per tool and round)

| Q | Category | Run 1 | Run 2 | Score | Cause | Cited file | Note |
|---|---|---|---|---|---|---|---|
| Q01 | A | | | | | | |
| … | | | | | | | |
| Q25 | E | | | | | | |
| **Total** | | | | **/25** | | | |

## Summary for the one-page report

| | ChatGPT round 1 | Claude round 1 | Gemini round 1 | ChatGPT round 2 |
|---|---|---|---|---|
| A. Direct lookup (/5) | | | | |
| B. Latest version (/5) | | | | |
| C. Calculation (/5) | | | | |
| D. Two documents (/5) | | | | |
| E. Not in files (/5) | | | | |
| **Total (/25)** | | | | |
| Most common cause | | | | |

## Limits to state in the report

- The problems were planted on purpose. Each one is a common situation in small-business file folders.
- Tests ran on personal paid plans. Business and Enterprise plans can have different file limits and cloud-drive connectors.
- Answers can change between runs and after model updates. Results are for the test date only.
