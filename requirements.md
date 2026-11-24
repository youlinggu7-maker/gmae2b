# Requirements baseline v0.2

| ID | Requirement | Acceptance evidence |
|---|---|---|
| FR-01 | 遊戲提供開始頁與兩個關卡 | 可由開始頁進入 L1、L2 |
| FR-02 | 每關至少一個理財互動單元 | 每關顯示題目、選項、回饋 |
| FR-03 | 未完成互動不能取得 KEY | KEY 只在該關最後一題確認後增加 |
| FR-04 | 顯示分數 | HUD 與結果頁顯示分數 |
| FR-05 | 顯示進步成果 | 結果頁顯示等級、進度條與文字回饋 |
| NFR-01 | 可輸出 Godot Web | `godot/project.godot` 可在 Godot 4.x 開啟，Web preset 可配置 |
| NFR-02 | 響應式與鍵盤可操作 | UI 使用 Control 節點；Space 可前進 |
| NFR-03 | 不依賴外部服務 | 遊戲邏輯與資產為本地檔案 |
| NFR-04 | 兒童安全 | 無帳號、個資、交易與投資推薦 |

## Traceability

FR-01/02/03/04/05 → `godot/main.gd` and existing `index.html`/`script.js` → manual flow test.
NFR-01/02/03/04 → `godot/project.godot`, `godot/main.gd`, local assets only → Godot open/export check when engine is available.
