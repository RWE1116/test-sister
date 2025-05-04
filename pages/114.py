import streamlit as st
import random

# 題庫（選擇題，每題包含問題、選項與正確答案）
question_pool = [
    {
        "question": "Python 中用來定義函數的關鍵字是？",
        "options": ["def", "function", "define", "fun"],
        "answer": "def"
    },
    {
        "question": "HTTP 的預設通訊埠號是？",
        "options": ["21", "80", "443", "25"],
        "answer": "80"
    },
    {
        "question": "Excel 中哪一個函數可以查詢表格資料？",
        "options": ["SUM", "VLOOKUP", "AVERAGE", "IF"],
        "answer": "VLOOKUP"
    },
    {
        "question": "下列哪一項是區塊鏈的特性？",
        "options": ["可隨意修改資料", "中心化控制", "不可被追溯", "不可竄改"],
        "answer": "不可竄改"
    },
    {
        "question": "AWS 是什麼類型的服務平台？",
        "options": ["作業系統", "雲端平台", "資料庫", "瀏覽器"],
        "answer": "雲端平台"
    },
    {
        "question": "HTTPS 使用了什麼協定來加密傳輸？",
        "options": ["FTP", "TLS/SSL", "TCP", "UDP"],
        "answer": "TLS/SSL"
    },
    {
        "question": "Python 中，哪個符號用來建立註解？",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#"
    }
]

# 頁面設定
st.set_page_config(page_title="即時抽考測驗", layout="wide")
st.title("🎯 即時抽考：選擇題測驗")
st.write("每次隨機抽出 5 題，作答完畢後點擊下方「提交答案」按鈕進行評分。")

# 初始化 session 狀態
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(question_pool, 5)
    st.session_state.answers = {}

# 顯示每一題
for i, q in enumerate(st.session_state.quiz):
    st.subheader(f"第 {i+1} 題")
    st.write(q["question"])
    selected = st.radio(
        label="請選擇一個答案：",
        options=q["options"],
        key=f"q{i}"
    )
    st.session_state.answers[i] = selected

# 提交並評分
if st.button("✅ 提交答案並評分"):
    score = 0
    st.subheader("🎓 評分結果")
    for i, q in enumerate(st.session_state.quiz):
        user_answer = st.session_state.answers[i]
        correct = q["answer"]
        if user_answer == correct:
            st.success(f"第 {i+1} 題：答對了！✅（你的答案：{user_answer}）")
            score += 1
        else:
            st.error(f"第 {i+1} 題：答錯了 ❌（你的答案：{user_answer}，正確答案：{correct}）")

    st.markdown(f"## 🎉 你的總分：{score} / 5")

    # 重設按鈕
    if st.button("🔄 再來一次"):
        st.session_state.quiz = random.sample(question_pool, 5)
        st.session_state.answers = {}
        st.experimental_rerun()
