# 小小夢魔｜理財投資夜航

一個零依賴的 HTML5 教育小遊戲，適合直接部署到 GitHub Pages、Netlify 或任何靜態網站主機。

## 本機預覽

直接開啟 `index.html` 即可；也可以在此資料夾啟動任一靜態伺服器。

## 遊戲內容

- 2 個夢境關卡，每關 2 題互動選擇題
- 答對可累積分數，完成關卡即可取得 KEY
- 結尾顯示得分、KEY 收集數與理財進步成果
- 響應式設計，支援桌面與手機
- 無外部圖片、框架或後端依賴

## 部署

將本資料夾內容推送到 GitHub Pages，或把資料夾拖到 Netlify Drop 即可。

## Godot Web 版本

`godot/` 已包含 Godot 4 專案原始碼。請以 Godot 4.x 開啟 `godot/project.godot`，加入 Web export preset 後輸出到 `web/`。目前環境沒有 Godot executable，因此尚未產生 Godot 的 `.wasm`／`.pck` 匯出檔；根目錄 HTML 版本仍可直接遊玩。

設計與流程文件：

- `project-state.yaml`
- `project-brief.md`
- `game-design-tournament.md`
- `requirements.md`
- `decision-log.md`
- `change-log.md`
