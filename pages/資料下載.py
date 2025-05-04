import streamlit as st

def download_file(file_path, file_label, mime_type, file_name):
    """通用文件下載功能"""
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label=file_label,
                data=file.read(),
                file_name=file_name,
                mime=mime_type
            )
    except FileNotFoundError:
        st.error(f"找不到文件：{file_path}")

# 顯示相關資料下載部分
st.subheader("相關資料下載")

# 下載文件2 (114年度下載資料)
download_file(r"downloads/實驗2. 水衝擊實驗.pdf", "下載 實驗2. 水衝擊實驗.pdf", "application/pdf", "實驗2. 水衝擊實驗.pdf")
