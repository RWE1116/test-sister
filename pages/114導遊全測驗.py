import streamlit as st

# 導入題庫
from streamlit_題庫 import question_pool

# 設定題目數
num_questions = min(50, len(question_pool))

# 頁面設定
st.set_page_config(page_title="114導遊實務", layout="wide")
st.title("🎯 114導遊實務：選擇題測驗")
st.write(f"作答完畢後點擊下方「✅ 提交答案」按鈕進行評分（共 {num_questions} 題，每題 2 分）。")

# 初始化 session 狀態
if "quiz" not in st.session_state:
    # 直接選擇題庫的前 num_questions 題
    st.session_state.quiz = question_pool[:num_questions]
    st.session_state.answers = {}

# 顯示每一題
for i, q in enumerate(st.session_state.quiz):
    st.subheader(f"第 {i+1} 題")
    st.write(q["question"])
    options_with_placeholder = ["請選擇"] + q["options"]
    selected = st.radio("請選擇一個答案：", options=options_with_placeholder, key=f"q{i}")
    st.session_state.answers[i] = selected.strip() if selected != "請選擇" else None

# 提交並評分
if st.button("✅ 提交答案並評分"):
    if any(ans is None for ans in st.session_state.answers.values()):
        st.warning("⚠️ 請完成所有題目後再提交。")
    else:
        score = 0
        st.subheader("🎓 評分結果")
        for i, q in enumerate(st.session_state.quiz):
            user_answer = st.session_state.answers[i]
            correct_answer = q["answer"].strip()
            if user_answer == correct_answer:
                st.success(f"第 {i+1} 題：答對了！✅（你的答案：{user_answer}）")
                score += 2
            else:
                st.error(f"第 {i+1} 題：答錯了 ❌（你的答案：{user_answer}，正確答案：{correct_answer}）")
        st.markdown(f"## 🎉 你的總分：{score} / {num_questions * 2}")

        if st.button("🔄 再來一次"):
            st.session_state.quiz = question_pool[:num_questions]
            st.session_state.answers = {}
            st.experimental_rerun()
