import streamlit as st
import random

# 題庫（選擇題，每題包含問題、選項與正確答案）
question_pool = [
    {
        "question": "「金氏世界紀錄中最重的南瓜為1,247公斤，大概是30位國小生的重量。」以上描述屬於何種解說技巧？",
        "options": ["提問法", "濃縮法", "演算法", "對比法"],
        "answer": "對比法"
    },
    {
        "question": "下列那種解說告示牌的背景顏色與文字顏色搭配最不適當？",
        "options": ["白底黑字", "藍底白字", "綠底紅字", "黃底黑字"],
        "answer": "綠底紅字"
    },
    {
        "question": "下列何者不是針對年長遊客導覽解說時須注意的事項？",
        "options": ["以安全為首要條件", "解說內容多融合年長遊客的生活經驗", "解說時須留意行進速度", "考量年長者記性差，解說片段內容即可"],
        "answer": "考量年長者記性差，解說片段內容即可"
    },
    {
        "question": "相較於人員解說，「非人員解說」方式具有下列何種優勢？",
        "options": ["可以即時提供解說服務", "容易處理緊急狀況", "能激發深度討論", "能根據遊客狀況調整解說內容"],
        "answer": "可以即時提供解說服務"
    },
    {
        "question": "下列有關解說的描述何者錯誤？",
        "options": ["解說方式即興發揮即可", "專業知識是解說的基礎", "解說重點在於啟發受眾者", "解說過程應從整體面說明"],
        "answer": "解說方式即興發揮即可"
    },
    {
        "question": "下列何種解說方式不適合運用在規劃自導式步道解說？",
        "options": ["解說摺頁", "解說牌", "錄音解說", "影片解說"],
        "answer": "影片解說"
    },
    {
        "question": "一般在旅遊景點聆聽導覽解說的遊客多是所謂的非受制聽眾（Non-captive audiences），有關非受制聽眾的特徵，下列敘述何者錯誤？",
        "options": ["不需對時間做承諾", "自願前來聆聽", "必定專注學習", "額外獎勵不重要"],
        "answer": "必定專注學習"
    }
]

# 頁面設定
st.set_page_config(page_title="即時抽考測驗", layout="wide")
st.title("🎯 即時抽考：選擇題測驗")
st.write("每次隨機抽出 5 題，作答完畢後點擊下方「✅ 提交答案」按鈕進行評分。")

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
        key=f"q{i}",
        index=-1  # 預設不選
    )
    st.session_state.answers[i] = selected

# 提交並評分
if st.button("✅ 提交答案並評分"):
    incomplete = any(ans == "" or ans is None for ans in st.session_state.answers.values())

    if incomplete:
        st.warning("⚠️ 請完成所有題目後再提交。")
    else:
        score = 0
        st.subheader("🎓 評分結果")
        for i, q in enumerate(st.session_state.quiz):
            user_answer = st.session_state.answers[i].strip()
            correct = q["answer"].strip()
            if user_answer == correct:
                st.success(f"第 {i+1} 題：答對了！✅（你的答案：{user_answer}）")
                score += 1
            else:
                st.error(f"第 {i+1} 題：答錯了 ❌（你的答案：{user_answer}，正確答案：{correct}）")

        st.markdown(f"## 🎉 你的總分：{score} / 5")

        # 提供重新測驗按鈕
        if st.button("🔄 再來一次"):
            st.session_state.quiz = random.sample(question_pool, 5)
            st.session_state.answers = {}
            st.experimental_rerun()
