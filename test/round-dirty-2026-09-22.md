# Round: index removed vs index present (locked 2026-09-22)

> 目的：證明 $500 入門方案在賣什麼。2026-09-15 第一輪 ChatGPT 考 24.5/25，
> 那一輪的資料夾裡有 `Policy Index - current versions.xlsx`——它直接告訴模型哪個版本現行，
> 版本衝突題因此全變成查表題。**客戶的資料夾沒有那份索引，那份索引正是交付物。**
>
> 兩輪之間**只差一份檔案**，題目、標準答案、評分規則都不動（沿用 `questions.md`，2026-09-15 鎖定）。

## 兩輪設定

| | 資料夾 | 份數 | 說明 |
|---|---|---|---|
| **Round A（髒版）** | `documents-dirty/` | 24 | 拿掉 `Policy Index - current versions.xlsx`，其餘完全不動 |
| **Round B（整理後）** | `documents/` | 25 | 含索引＝最小整理；等同「我幫你建了一份現行版本索引」 |

**跑法**：各開一個新的 ChatGPT Project，上傳該資料夾全部檔案，10 題**每題一次**、每題開新對話。
（9/15 那輪 25 題×2 次＝50 次撞到頻率限制；這次 10 題×1 次，兩輪共 20 次。）

## 要跑的 10 題（B 組 5 題＋D 組 5 題）

**B 組是實驗組**：答案取決於「哪個版本是現行的」，拿掉索引後理應變難。
**D 組是對照組**：Q17 也吃版本，其餘三題是跨文件的規則題，理論上不受索引影響——
如果 D 組後三題兩輪都對，就證明落差是**版本判讀**造成的，不是模型整體變差。

貼給 ChatGPT 的題目（不要貼標準答案）：

1. How many days does a customer have to return an unused item?
2. Above what order value do we give a free return label?
3. What does standard shipping cost, and when is it free?
4. How many PTO days do full-time staff get?
5. Which carrier do we ship with now?
6. A $300 oak table arrived damaged. The customer sent photos on day 5. What do we do, and who approves the refund?
7. A customer in Canada wants to return an unused item after 40 days. Can they, and who pays return shipping?
8. How should a customer care for an oak table, and how long is it under warranty?
9. During Black Friday, can a customer use the 25% sale and a price match together?
10. A customer bought an item 10 days ago and found it cheaper on a marketplace seller. Do we match?

## 評分表（自己看，不要貼進 ChatGPT）

| # | 原編號 | 標準答案 | 陷阱答案（代表它讀到舊版） | Round A | Round B |
|---|---|---|---|---|---|
| 1 | Q06 | 45 days | 30 days | | |
| 2 | Q07 | $100 | $75 | | |
| 3 | Q08 | $7.95；滿 $60 免運 | $6.95／$50 | | |
| 4 | Q09 | 15 天 | 12 天 | | |
| 5 | Q10 | ParcelPoint（2026-07-01 起）；**要同時指出網站 FAQ 還寫著 SwiftShip 才算滿分** | SwiftShip | | |
| 6 | Q16 | 符合資格（7 天內附照片）；換或退；超過 $40 要退回商品；退款超過 $250 要 CS lead 核准 | 只講到其中一條規則 | | |
| 7 | Q17 | 可以（45 天內）；退貨運費客戶自付 | 「不行，只有 30 天」／「免運標籤」 | | |
| 8 | Q18 | 每 6 個月上油；保固 1 年 | — | | |
| 9 | Q19 | 不行，價格保證不能與其他促銷合併 | 「可以」 | | |
| 10 | Q20 | 不行，價格保證只涵蓋授權經銷商，不含平台賣家 | 「可以，14 天內」 | | |

**計分**：每題 1 分，半對 0.5（例如第 5 題答對承運商但沒指出 FAQ 過期）。

## 結果（跑完填這裡）

- Round A（24 份、無索引）：__ / 10
- Round B（25 份、有索引）：__ / 10
- 差異出現在哪幾題：
- 一句話結論：

🔴 **報告只能寫這兩輪實際量到的東西。** 不要寫成「AI 沒有整理就會答錯」這種全稱句——
這是一個虛構電商、10 題、每題一次的單次測試，樣本就這麼大。
