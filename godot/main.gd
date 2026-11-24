extends Control

const LEVELS := [
	{
		"title": "零用錢的第一個家", "desc": "每一枚硬幣，都可以替未來點亮一盞燈。", "icon": "☾",
		"questions": [
			{"q": "收到 100 元零用錢，你會怎麼開始？", "note": "想想看：把錢分一分，夢想才不會只停在想像裡。", "answers": ["全部買喜歡的零食", "先存下 30 元，再規劃剩下的錢", "全部藏在枕頭下"], "correct": 1, "ok": "很棒！先儲蓄，是讓夢想長大的第一步。"},
			{"q": "彩色筆要 120 元，目前有 70 元。最好的計畫是？", "note": "理財小偵探，請選出最有耐心的做法。", "answers": ["借錢買，之後再說", "放棄夢想", "每週存一點，存夠再買"], "correct": 2, "ok": "答對！為目標存錢，夢想會變得更踏實。"}
		]
	},
	{
		"title": "霧中的投資花園", "desc": "不同的種子，會長出不同的未來。學會分散，讓夢想更穩。", "icon": "✦",
		"questions": [
			{"q": "你有 100 元想讓它長大，哪種做法比較穩？", "note": "小提醒：不要把所有希望放在同一個地方。", "answers": ["全部押在一個看起來很酷的東西", "分成幾份，放在不同的投資籃子", "交給陌生人保管"], "correct": 1, "ok": "答對！分散投資，可以降低一次失去很多的風險。"},
			{"q": "有人說「保證一定賺很多」，你應該先做什麼？", "note": "遇到太好的承諾，先停一下、查證一下。", "answers": ["立刻把所有錢給他", "問清楚風險，和家人老師討論", "叫朋友也一起投資"], "correct": 1, "ok": "太好了！先查證、懂風險，再做決定。"}
		]
	}
]

var level := 0
var question_index := 0
var score := 0
var keys := 0
var selected := -1
var title_label: Label
var body: VBoxContainer

func _ready() -> void:
	show_start()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("advance"):
		var focused := get_viewport().gui_get_focus_owner()
		if focused is Button and focused.disabled == false:
			focused.emit_signal("pressed")

func base_screen() -> VBoxContainer:
	for child in get_children(): child.queue_free()
	var bg := ColorRect.new(); bg.color = Color("#080b1d"); bg.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT); add_child(bg)
	var margin := MarginContainer.new(); margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT); margin.add_theme_constant_override("margin_left", 90); margin.add_theme_constant_override("margin_right", 90); margin.add_theme_constant_override("margin_top", 70); margin.add_theme_constant_override("margin_bottom", 45); add_child(margin)
	body = VBoxContainer.new(); body.add_theme_constant_override("separation", 18); body.alignment = BoxContainer.ALIGNMENT_CENTER; margin.add_child(body)
	var hud := Label.new(); hud.text = "✦  小小夢魔｜理財投資夜航                                      ◆ 得分 %d      🔑 KEY %d / 2" % [score, keys]; hud.add_theme_color_override("font_color", Color("#c4d0ff")); hud.add_theme_font_size_override("font_size", 16); body.add_child(hud)
	return body

func label_text(text: String, size: int, color := Color("#eef4ff")) -> Label:
	var l := Label.new(); l.text = text; l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER; l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART; l.add_theme_font_size_override("font_size", size); l.add_theme_color_override("font_color", color); return l

func add_button(text: String, callback: Callable) -> Button:
	var b := Button.new(); b.text = text; b.custom_minimum_size = Vector2(0, 52); b.add_theme_font_size_override("font_size", 16); b.pressed.connect(callback); body.add_child(b); return b

func show_start() -> void:
	base_screen(); body.add_spacer(false); body.add_child(label_text("DREAMY FINANCE ACADEMY · 01", 13, Color("#aebcff"))); body.add_child(label_text("小小夢魔\n的理財夜航", 54)); body.add_child(label_text("今晚，夢魔要穿越兩座迷霧房間。\n學會讓零用錢去對的地方，找回兩把閃亮的 KEY！", 18, Color("#b6c0d9"))); add_button("開始夜航  →", show_level); body.add_spacer(false)

func show_level() -> void:
	base_screen(); var data: Dictionary = LEVELS[level]; body.add_spacer(false); body.add_child(label_text("DREAM ROOM · 0%d" % (level + 1), 13, Color("#aebcff"))); body.add_child(label_text(data.title, 42)); body.add_child(label_text(data.desc, 18, Color("#b6c0d9"))); add_button("進入互動單元  →", show_quiz); body.add_spacer(false)

func show_quiz() -> void:
	base_screen(); var data: Dictionary = LEVELS[level]; var q: Dictionary = data.questions[question_index]; body.add_child(label_text("互動單元 0%d / 02 · 題目 %d/2" % [level + 1, question_index + 1], 13, Color("#d3c681"))); body.add_child(label_text(data.icon, 34, Color("#e5cb78"))); body.add_child(label_text(q.q, 28)); body.add_child(label_text(q.note, 15, Color("#9eabcd"))); selected = -1
	for i in q.answers.size():
		var answer_button := add_button(q.answers[i], func(): choose_answer(i)); answer_button.name = "Answer%d" % i
	add_button("確認選擇  →", confirm_answer)

func choose_answer(index: int) -> void:
	selected = index
	for child in body.get_children():
		if child is Button and child.name.begins_with("Answer"): child.disabled = true

func confirm_answer() -> void:
	if selected < 0: return
	var q: Dictionary = LEVELS[level].questions[question_index]
	if selected == int(q.correct): score += 25
	if question_index < 1:
		question_index += 1; show_quiz()
	else:
		keys += 1; question_index = 0
		if level == 0: level = 1; show_level()
		else: show_result()

func show_result() -> void:
	base_screen(); body.add_spacer(false); body.add_child(label_text("✦", 50, Color("#e5cb78"))); body.add_child(label_text("你找回了所有 KEY！", 40)); body.add_child(label_text("本次得分：%d / 100\n理財進步成果：%s" % [score, "理財小星探" if score >= 90 else "理財練習生"], 22, Color("#d3c681"))); body.add_child(label_text("儲蓄讓夢想有起點，分散投資讓風險不迷路。", 15, Color("#9eabcd"))); add_button("再航行一次  ↻", restart); body.add_spacer(false)

func restart() -> void:
	level = 0; question_index = 0; score = 0; keys = 0; show_start()
