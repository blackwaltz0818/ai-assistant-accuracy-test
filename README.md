# AI Assistant Accuracy Test (work in progress)

Can a paid AI assistant answer questions correctly from a small company's own files?

This repo tests ChatGPT, Claude and Gemini on the same set of files from a fictional online store, **Lantern Lane Goods**. The files have problems that are common in real shared folders: old versions, contradictions, answers only in spreadsheets, a scanned contract and a draft that looks like policy.

**Everything in this repo is fictional.** No real company, customer or person is in these files.

## Method

1. Load the 25 files in `documents/` into each assistant by direct upload.
2. Ask the 25 questions in `test/questions.md`. Each question runs twice, in a new chat each time.
3. Score each answer with `test/scoring-sheet.md`. Tag every miss with a cause.
4. Fix the files and add instructions. Ask the same questions again.

The questions and expected answers were locked before the first test.

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

- The problems were planted on purpose.
- Tests use personal paid plans. Business and Enterprise plans can behave differently.
- Answers change between runs and after model updates. Results hold for the test date only.
