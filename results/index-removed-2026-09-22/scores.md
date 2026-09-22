# Round A vs Round B — index removed (2026-09-22)

Tool: ChatGPT (Plus, web UI, Projects). One question per new chat, one run per question.
Round A project: "Lantern Lane Round A - no index (24 files)" — `documents-dirty/`
Round B project: "Lantern Lane Round B - with index (25 files)" — `documents/`
Only difference between rounds: `Policy Index - current versions.xlsx`.

| Result | Round A (no index) | Round B (with index) |
|---|---|---|
| **B group — version conflicts (5)** | **2.5** | **5** |
| **D group — across documents (5)** | **5** | **5** |
| **Total** | **7.5 / 10** | **10 / 10** |

The whole gap sits in the version-conflict group. The control group scored the same in
both rounds, so this is not the model performing worse overall — it is the model being
unable to tell which version is current.

## Question by question

| # | Q | Round A answer | A | Round B answer | B |
|---|---|---|---|---|---|
| 1 | Return window (45) | "The uploaded Employee Handbook 2023 does not specify a customer return policy…" — never found the return policy at all | 0 | "45 days from delivery… original packaging" (Return Policy v3 final2) | 1 |
| 2 | Free return label (>$100) | "$100… Canada always pays" (Return Policy v3 final2) | 1 | same, correct | 1 |
| 3 | Standard shipping ($7.95 / free $60) | correct (Shipping Rates 2026) | 1 | correct | 1 |
| 4 | PTO days (15) | **"12 days" (Employee Handbook 2023)** — took the superseded version | 0 | "15 days… 2026 handbook, effective Jan 1 2026, which explicitly replaces earlier versions" | 1 |
| 5 | Current carrier (ParcelPoint + FAQ still wrong) | "ParcelPoint… since July 1 2026" but **did not flag the outdated FAQ** | 0.5 | "ParcelPoint… **The Shipping FAQ still says SwiftShip, so that document appears to be outdated**" | 1 |
| 6 | Damaged $300 table | correct on both rules | 1 | correct | 1 |
| 7 | Canada return at 40 days | "Yes, 45 days… customer pays" | 1 | same, correct | 1 |
| 8 | Oak table care + warranty | correct | 1 | correct | 1 |
| 9 | Black Friday + price match | correct | 1 | correct | 1 |
| 10 | Marketplace seller price match | correct | 1 | correct | 1 |

## What the failures actually looked like

🔴 **The failure is not "it picked the older file". It is "it answered from whatever file it
happened to retrieve."** On Q1 it retrieved the Employee Handbook and reported that the
return period was not documented — with three copies of the return policy sitting in the
same folder. On Q7, same folder, same model, it found the right return policy and answered
correctly. Same question set, same run, different retrieval.

🟢 **Round B shows what the index buys.** In two answers the model explicitly reasoned about
currency: the 2026 handbook "explicitly replaces earlier versions", and the shipping FAQ
"appears to be outdated". Neither sentence appears anywhere in Round A.

## Limits (do not write past these)

- One fictional e-commerce company, 10 questions, one run per question. n is small.
- Round A's first question was asked ~30 seconds after upload and failed; it was re-asked
  about four minutes later, after confirming all 24 files were listed, and failed the same
  way. The failure is not upload lag.
- ChatGPT Plus web UI only. No API, no other tools, no second model.
- Scoring follows `test/questions.md` (locked 2026-09-15). Q5 is the only half-mark rule.
