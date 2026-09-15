# Can your AI assistant answer from your own files?

**Test report — Lantern Lane Goods (fictional online store) — 2026-09-15**
Draft. Tool tested so far: ChatGPT Plus.

## Result

**ChatGPT answered 24.5 of 25 questions correctly from the store's own files.**

| Question type | Score |
|---|---|
| Direct lookup (payment terms, warranty) | 5 / 5 |
| Latest version, when old versions are still in the folder | 4.5 / 5 |
| Calculation from spreadsheets | 5 / 5 |
| Combining two documents | 5 / 5 |
| Answer not in the files (should say "not found") | 5 / 5 |

Each question ran twice in a new chat. A question counted as correct only if both answers were correct.

## What went well

- It used the current return policy, not the two older versions in the same folder.
- It did not treat a draft loyalty program as company policy.
- It said "not in the files" instead of inventing a CEO name or a revenue figure.
- It read a scanned lease that has no text layer.

## What did not go well

- **The folder did not fit.** The Plus plan takes 25 files per Project. The store's folder had 32 files, so 7 had to be removed or merged before testing. A real small business folder has hundreds of files.
- **One conflict was only half reported.** Asked which carrier the store uses, it gave the right answer both times. Only once did it warn that the website FAQ still names the old carrier.
- **Heavy use hit a limit.** About 50 new chats in an hour triggered a usage warning.

## What this means for a small business

The assistant is accurate **when the files are few, current and clearly dated**. The work is in getting the files to that state:

1. Decide which files the assistant should read. Remove old versions and duplicates.
2. Make the current version obvious: dates in the document, a clear file name, a list of current policies.
3. Fit the plan's limits, or choose a plan or connection that holds the folder.
4. Test with your own questions before staff rely on the answers.

## Limits of this test

- The company and all 25 files are fictional. The problems in them were planted on purpose.
- The files are short and each policy states its effective date. Real files are longer and often undated, which makes the job harder.
- Files were uploaded directly. Connecting a cloud drive with many files was not tested.
- Personal paid plan only. Business and Enterprise plans can behave differently.
- Results hold for the test date. Answers change after model updates.

Files, questions, expected answers and all 50 raw answers: `github.com/blackwaltz0818/ai-assistant-accuracy-test`
