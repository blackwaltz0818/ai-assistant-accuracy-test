# ChatGPT round 1 — scores

- **Tool:** ChatGPT Plus, model shown as GPT-6 Astra (default effort), Project with project-only memory
- **Files:** 25 files uploaded directly to the Project
- **Date:** 2026-09-15 (Taipei time)
- **Method:** each question asked twice, each time in a new chat. A question scores the lower of its two runs.
- **Raw answers:** `raw.jsonl` (50 runs)

| Q | Category | Run 1 | Run 2 | Score | Cause | Note |
|---|---|---|---|---|---|---|
| Q01 | A | Correct | Correct | 1 | | Net 45 |
| Q02 | A | Correct | Correct | 1 | | 90 days |
| Q03 | A | Correct | Correct | 1 | | CS lead |
| Q04 | A | Correct | Correct | 1 | | No expiry |
| Q05 | A | Correct | Correct | 1 | | $1,500 |
| Q06 | B | Correct | Correct | 1 | | 45 days; cited the current file, not v2 or the macros |
| Q07 | B | Correct | Correct | 1 | | $100, not the superseded $75 |
| Q08 | B | Correct | Correct | 1 | | $7.95, free from $60; did not use the 2025 rates |
| Q09 | B | Correct | Correct | 1 | | 15 days, not 12 |
| Q10 | B | Correct | Partial | 0.5 | C | Both named ParcelPoint. Only run 1 said the website FAQ still says SwiftShip |
| Q11 | C | Correct | Correct | 1 | | Furniture +$46,500 |
| Q12 | C | Correct | Correct | 1 | | $696,650 |
| Q13 | C | Correct | Correct | 1 | | $19.95, no free shipping to Hawaii |
| Q14 | C | Correct | Correct | 1 | | Brightwood, 25 days |
| Q15 | C | Correct | Correct | 1 | | Read the image-only scan: $8,200, ends 2027-06-30 |
| Q16 | D | Correct | Correct | 1 | | Both rules: return required over $40, CS lead approves over $250 |
| Q17 | D | Correct | Correct | 1 | | Yes; customer pays return shipping |
| Q18 | D | Correct | Correct | 1 | | Oil every 6 months; 1-year warranty |
| Q19 | D | Correct | Correct | 1 | | Cannot combine |
| Q20 | D | Correct | Correct | 1 | | Marketplace sellers excluded |
| Q21 | E | Correct | Correct | 1 | | Draft, not approved |
| Q22 | E | Correct | Correct | 1 | | US and Canada only |
| Q23 | E | Correct abstain | Correct abstain | 1 | | Said the files do not name a CEO |
| Q24 | E | Correct | Correct | 1 | | No 2026 extension; 2025 memo only |
| Q25 | E | Correct abstain | Correct abstain | 1 | | Said 2025 revenue is not in the files |
| **Total** | | | | **24.5 / 25** | | |

| Category | Score |
|---|---|
| A. Direct lookup | 5 / 5 |
| B. Latest version and conflicts | 4.5 / 5 |
| C. Calculation and comparison | 5 / 5 |
| D. Across two documents | 5 / 5 |
| E. Not in the files | 5 / 5 |

## Setup findings (not scored)

1. **File limit.** The Plus plan allows 25 files per Project ("Upgrade to Pro to add 40 files"). The original set of 32 files did not fit.
2. **Deleted files seemed to still count.** A Project that had files removed reported the limit at 19 files. A new Project accepted all 25. Cause not confirmed.
3. **Rate limit.** About 50 new chats in roughly an hour triggered a "too many conversations" warning. Testing stopped and resumed slowly.

## Scoring notes

- Q16 run 2: the captured text was cut off at the end by the capture tool. The part captured contains both required rules.
- Q08: the spreadsheet column is "Free shipping threshold (USD) = 60". Both "over $60" and "$60 or more" are accepted.
