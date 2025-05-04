import os
import streamlit as st

def download_file(file_path, file_label, mime_type, file_name, unique_key):
    """通用文件下載功能"""
    # 檢查文件是否存在
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            st.download_button(
                label=file_label,
                data=file.read(),
                file_name=file_name,
                mime=mime_type,
                key=unique_key  # 使用動態的唯一 key
            )
    else:
        st.error(f"找不到文件：{file_path}")
        st.text(f"當前工作目錄：{os.getcwd()}")  # 顯示當前工作目錄
        st.text(f"檢查的路徑：{file_path}")  # 顯示檢查的路徑

# 顯示相關資料下載部分
st.subheader("相關資料下載")

# 使用相對路徑設定文件路徑
base_path = "downloads"  # 假設所有的文件都放在此文件夾

# 下載文件1 (114年度下載資料)
download_file(os.path.join(base_path, "1301A_領隊_華外語_實務.pdf"), "下載 1301A_領隊_華外語_實務.pdf", "application/pdf", "1301A_領隊_華外語_實務.pdf", "key1")
download_file(os.path.join(base_path, "1301Q_領隊_華外語_實務.pdf"), "1301Q_領隊_華外語_實務.pdf", "application/pdf", "1301Q_領隊_華外語_實務.pdf", "key2")


