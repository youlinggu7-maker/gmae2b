# AI Game Design Tournament

## Brief and hard gates

- Audience: 小學生
- Purpose: 生活理財投資概念教學
- Platform/session: Godot 4 HTML5，3–6 分鐘
- Decision owner: 使用者／課程教師
- Hard gates: 2 關、每關互動與 KEY、分數與成果頁、可網頁部署、無真實交易、兒童可讀性
- Evidence date: 2026-11-24；以下均為 `AI pre-score`，不是玩家證據

## Locked educational reward profile

- Priority: Learning first（由使用者要求全部套用且明確指定教學用途；此為可修訂假設）
- L/E/M/A: 50% / 15% / 10% / 25%
- Maximum G/C penalties: G 15%，C 10%
- G/C hard gate: G < 60，C < 70
- Evidence plan: 正確率與解釋題（L）、完成率與重玩率（E）、自我效能短量表（M）、錯誤可恢復與困難度回饋（A）、快速亂點／跳過紀錄（G）、重讀指令與困惑回報（C）

## Candidates

| ID | Concept / core loop | G | R/Purpose | D | R_edu | Evidence | Main risk |
|---|---|---:|---:|---:|---:|---|---|
| A | KEY 夜航：探索房間→選擇理財行動→看因果回饋→取得 KEY | 84 | 82 | 94 | 80.8 | AI pre-score / medium | 題目過少可能只測記憶 |
| B | 零用錢分配工坊：拖曳錢幣到儲蓄、需要、夢想三籃 | 86 | 80 | 88 | 81.7 | AI pre-score / medium | 拖曳操作造成裝置與動作混淆 |
| C | 風險花園：選種子並分散到多個花圃，觀察隨機天氣 | 88 | 84 | 76 | 83.1 | AI pre-score / medium | 隨機性可能掩蓋因果，需固定種子 |
| D | 理財偵探：找出承諾中的風險線索，再向角色提問 | 91 | 87 | 73 | 82.8 | AI pre-score / medium | 閱讀量偏高，兒童需要語音或圖示支援 |
| E | 夢想時間線：安排現在花費、短期目標與長期目標 | 82 | 86 | 84 | 79.9 | AI pre-score / medium | 時間概念抽象，需示範 |
| F | 小小市集：交換物品與延遲滿足，累積資源解鎖結局 | 89 | 78 | 80 | 78.6 | AI pre-score / medium | 交換規則可能被最佳化成猜答案 |

## Independent review summary

- Game designer: A、B 的第一個有效行動最快；C 的回饋最有深度但需控制隨機性。
- First-time player: A 只需按鈕，最容易發現；B 需加入鍵盤替代操作。
- Domain lens: A、B 直接對應儲蓄與目標；C、D 對風險與查證較完整。
- Research lens: C 的固定事件與事件紀錄最適合重現；A 可用固定題庫降低混淆。
- Production lens: A 最快完成 Godot Web vertical slice，並可日後吸收 B／C 的機制。

## Recommendation and human decision

推薦 A 作為 MVP：它通過所有硬門檻、開發成本最低，且現有網頁原型已能觀察完整流程。B 的「分籃」與 C 的「分散風險」可作為後續第二代互動。

目前已依使用者「全部套用」將 A 視為選定方向，並建立 Godot Web 原始碼；正式兒童測試前仍需教師／使用者確認內容與學習指標。

## Three visual directions for later comparison

1. Moonlit silhouette：深藍霧境、月光、剪影；最貼近現有原型，文字區高對比。
2. Paper dream atlas：紙張地圖、蠟筆色錢幣與手繪圖示；兒童辨識度高，3D 感較弱。
3. Soft 3D diorama：低多邊形房間、立體 KEY、柔和燈光；需 Blender 資產與較高製作成本。

Current visual choice: 1 as deployable fallback; 3 deferred until Blender is available.
