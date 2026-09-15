# Test questions and expected answers (locked 2026-09-15)

> Locked before round 1. Do not change questions or answers after testing starts.
> "Trap" = the wrong answer a tool gives if it reads an old or conflicting file.

## A. Direct lookup

| # | Question | Expected answer | Source | Trap |
|---|---|---|---|---|
| Q01 | What are our payment terms with Oakridge Textiles? | Net 45 | D16 | — |
| Q02 | How long is the warranty on textiles? | 90 days | D07 | — |
| Q03 | Who has to approve a refund over $250? | The CS lead | D14 | — |
| Q04 | Do our gift cards expire? | No | D27 | — |
| Q05 | What is the minimum order for wholesale? | $1,500 (20% discount) | D25 | — |

## B. Latest version and conflicts

| # | Question | Expected answer | Source | Trap |
|---|---|---|---|---|
| Q06 | How many days does a customer have to return an unused item? | 45 days | D03 (per D30) | 30 days (D01, D15) |
| Q07 | Above what order value do we give a free return label? | $100 | D03 | $75 (D02) |
| Q08 | What does standard shipping cost, and when is it free? | $7.95; free over $60 | D05 | $6.95 / $50 (D04) |
| Q09 | How many PTO days do full-time staff get? | 15 | D10 | 12 (D11) |
| Q10 | Which carrier do we ship with now? | ParcelPoint, since 2026-07-01. Full marks only if it also notes the website FAQ still says SwiftShip | D23 | SwiftShip (D24) |

## C. Calculation and comparison

| # | Question | Expected answer | Source | Trap |
|---|---|---|---|---|
| Q11 | Which product category grew the most from Q1 to Q2 2026, in dollars? | Furniture, +$46,500 (decor +$9,350; textiles −$14,300) | D19 (both sheets) | — |
| Q12 | What was total revenue in Q2 2026? | $696,650 | D19 | — |
| Q13 | A customer in Hawaii orders $75 of decor. What is the shipping cost? | $19.95 (no free shipping to Alaska/Hawaii) | D05 | Free (over $60 rule) |
| Q14 | Which supplier has the longer lead time, and by how many days? | Brightwood Furniture, 25 days longer (60 vs 35) | D16, D17 | — |
| Q15 | What is the monthly rent for the warehouse, and when does the lease end? | $8,200; 2027-06-30 | D22 (scan) | Made-up figure. "Cannot read the file" counts as correct abstain |

## D. Across two documents

| # | Question | Expected answer | Source | Trap |
|---|---|---|---|---|
| Q16 | A $300 oak table arrived damaged. The customer sent photos on day 5. What do we do, and who approves the refund? | Eligible (photos within 7 days); replace or refund; item must come back (value over $40); a refund needs CS lead approval (over $250) | D13, D14 | Misses one of the two rules |
| Q17 | A customer in Canada wants to return an unused item after 40 days. Can they, and who pays return shipping? | Yes (within 45 days); the customer pays return shipping | D03, D24 | "No, 30 days"; "free label" |
| Q18 | How should a customer care for an oak table, and how long is it under warranty? | Oil every 6 months; 1-year warranty | D21, D07 | — |
| Q19 | During Black Friday, can a customer use the 25% sale and a price match together? | No. Price match cannot be combined with other promotions | D26, D08 | "Yes" |
| Q20 | A customer bought an item 10 days ago and found it cheaper on a marketplace seller. Do we match? | No. Price match covers authorized retailers only, not marketplace sellers | D08 | "Yes, within 14 days" |

## E. Not in the files (should say it does not know)

| # | Question | Expected answer | Source | Trap |
|---|---|---|---|---|
| Q21 | Do we have a loyalty points program? | No approved program; there is only a draft proposal | D31 | "Yes, 5% back" |
| Q22 | Can customers in Mexico order from us? | No. We ship to the US and Canada only | D24 | Invents a Mexico policy |
| Q23 | Who is the CEO of Brightwood Furniture? | Not in the files | — | Invents a name |
| Q24 | Is there a holiday return extension for 2026? | No 2026 decision in the files; the only memo is for 2025 and has expired | D09 | Applies the 2025 dates to 2026 |
| Q25 | What was our total revenue for 2025? | Not in the files (only the Q1 and Q2 2026 sheets exist) | — | Invents a figure or sums Q1+Q2 2026 |
