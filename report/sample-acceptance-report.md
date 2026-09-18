# Acceptance report — sample

**Client:** Lantern Lane Goods (fictional, 14-person online home goods store)
**Work:** Document Starter — sort the company's files, load them into the AI the company already pays for, then test the answers
**Tool tested:** ChatGPT Plus — **2026-09-15**

> This is a sample of the report every Document Starter client gets at handover. The company and its files are invented for this demo. The method and the report format are the real ones.
>
> A Document Starter runs one week from the day I have your files, and the test uses about thirty questions your own staff already ask. This demo folder was small, so it ran twenty-five.

---

## 1. Result

**The assistant answered 24.5 of 25 questions correctly.**

| Question type | Score | What it proves |
|---|---|---|
| Direct lookup | 5 / 5 | Supplier terms, warranty periods, approval limits |
| Latest version, with old versions still in the folder | 4.5 / 5 | It used the current return policy, not the two older ones |
| Calculation from spreadsheets | 5 / 5 | Revenue totals, growth by category, shipping for one order |
| Answers that need two documents | 5 / 5 | A damage claim that needs both the SOP and the refund limit |
| Questions the files cannot answer | 5 / 5 | It said "not in the files" instead of inventing an answer |

Every question ran twice, each time in a new chat. A question counted as correct only if both answers were correct.

## 2. What the test caught

| # | Finding | What it means for the client | Fix |
|---|---|---|---|
| 1 | The folder did not fit. The plan takes 25 files per project; the folder had 32 | Staff would have been asking a tool that could not see 7 of their files, without being told | Decide which files the assistant needs, archive the rest, or move to a plan that holds the folder |
| 2 | Three return policies sat in the same folder, two of them out of date | The assistant answered correctly here, but a person searching the folder would not | Archive old versions; keep one current file with its date in the name |
| 3 | The website FAQ still named the old shipping carrier | Asked which carrier, the assistant gave the right answer once and warned about the outdated FAQ only once out of two runs | Update the FAQ; the assistant repeats whatever the files say |
| 4 | A draft loyalty program sat next to approved policies | The assistant did not present the draft as policy, but the risk stays while the file is unmarked | Put "DRAFT" in the file name, not only in the text |

## 3. What the client received

1. The cleaned file set, in plain files the company owns
2. The assistant set up on those files, in the tool the company already pays for
3. This report: 25 questions, expected answers, both runs, and the cause of every miss
4. The question set itself, so the test can be run again after the files change

## 4. How to read the score

A score is only as good as the questions. These 25 were written from what staff actually ask, fixed before the first test, and not changed afterwards. They deliberately include five questions the files cannot answer, because an assistant that invents an answer is worse than one that says "I don't know".

## 5. Limits stated for the client

- The test covers these 25 questions on this file set, on the test date. Model updates change answers.
- The problems in this demo folder were planted on purpose. A real folder is bigger and messier.
- Tested on a personal paid plan. Business and Enterprise plans have different file limits and connectors.

## 6. What happens after this report

The file set is yours and it will drift. Two things keep the answers correct:

1. **One owner for the folder.** When a policy changes, the old file gets archived the same day. The assistant repeats whatever is in the folder, so a stale file is a wrong answer waiting to happen.
2. **The question set stays.** Run the same questions after the next batch of changes. If the score drops, the folder moved, not the tool.

If your folder outgrows the plan's file limit, or you need answers across years of files rather than a working set, that is a different build with its own quote and a monthly fee. I would rather say that here than after you have paid for the starter.

---

Full test set, all 50 raw answers and the scoring sheet: `github.com/blackwaltz0818/ai-assistant-accuracy-test`
