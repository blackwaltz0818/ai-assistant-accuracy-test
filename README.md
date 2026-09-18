# AI Assistant Accuracy Test

Can a paid AI assistant answer questions correctly from a small company's own files?

This repo tests ChatGPT on a set of files from an invented online store, **Lantern Lane Goods**. The files have problems that are common in real shared folders: old versions, contradictions, answers only in spreadsheets, a scanned contract and a draft that looks like policy.

**Everything in this repo is invented.** No real company data, customer record or person appears in these files, and no client work was used to build them.

Names were checked against public search before publishing. `Lantern Lane Goods` and `Oakridge Textiles` return no matching business. `Brightwood Furniture` is used by several real, unrelated businesses, so it is worth saying plainly: the supplier agreement in `documents/` is a made-up contract written for this test, it has nothing to do with any of them, and none of its terms describe a real agreement.

## Method

1. Load the 25 files in `documents/` into the assistant by direct upload.
2. Ask the 25 questions in `test/questions.md`. Each question runs twice, in a new chat each time.
3. Score each answer with `test/scoring-sheet.md`.
4. Tag every miss with a cause, so a wrong answer points at a file rather than at the tool.

The questions and expected answers were locked before the first test and were not changed afterwards.

**What this repo does not contain.** One tool, one round. Claude and Gemini were planned and then dropped: the point being tested is whether an assistant answers correctly from a company's own files, and that question is answered by one tool on one clean run. A second round on fixed files was dropped for the same reason. Both decisions are dated 2026-09-18.

## Layout

| Path | Content |
|---|---|
| `documents/` | The 25 test files |
| `test/company-and-documents.md` | The company, each file, and the problem planted in it |
| `test/questions.md` | 25 questions with expected answers |
| `test/scoring-sheet.md` | Test protocol, grades and cause codes |
| `results/` | Raw answers and scores (added after testing) |
| `scripts/generate_documents.py` | Rebuilds `documents/` |

## Limits

- The problems were planted on purpose. A real folder is bigger and messier.
- One result stands out and should be read carefully: on a small, tidy folder the assistant scored 24.5 out of 25. **The interesting finding is not that the tool is bad. It is that the folder decides the answer.**
- Tests use personal paid plans. Business and Enterprise plans can behave differently.
- Answers change between runs and after model updates. Results hold for the test date only.
- A project on the plan tested held 25 files; the folder started at 32. Seven files simply could not go in.

## Who wrote this

Jason Chuang. I sort out company documents, connect them to the AI a company already pays for, and test the answers before handover. The report a client receives looks like `report/sample-acceptance-report.md`. jasonchuang.com
