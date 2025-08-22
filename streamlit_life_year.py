# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date

# ---------- 功能函數 ----------
def sum_digits(n):
    """將數字每位相加"""
    return sum(int(d) for d in str(n))

def calculate_life_number(year, month, day, query_year):
    # 判斷查詢年份是否在生日之前
    birthday_this_year = date(query_year, month, day)
    today = date(query_year, 1, 1)  # 只比較當年1/1與生日
    if birthday_this_year > today:
        base_year = query_year - 1
    else:
        base_year = query_year

    # 流年總和
    total_sum = base_year + month + day
    mid_sum = sum_digits(total_sum)
    main_number = sum_digits(mid_sum)

    return total_sum, mid_sum, main_number

def get_year_advice(main_number):
    advice_dict = {
        1: ("自主與突破之年", "容易衝動、單打獨鬥", "聆聽他人意見，決策前先審慎評估", "⭐⭐⭐⭐", "紅色/橙色", "虎眼石"),
        2: ("協作與關係之年", "容易過於迎合他人，忽略自我需求", "明確表達需求，建立健康邊界", "⭐⭐⭐", "綠色/粉色", "粉晶"),
        3: ("創意與表達之年", "情緒波動、分心或過度社交", "專注核心目標，規劃時間給創意發想", "⭐⭐⭐⭐", "黃色/紫色", "紫水晶"),
        4: ("穩定與基礎之年", "感到壓力沉重或拘泥形式", "建立有彈性的計畫，避免過度追求完美", "⭐⭐⭐", "棕色/大地色", "舒俱徠"),
        5: ("變動與自由之年", "易焦慮、缺乏耐心", "保持靈活心態，善用變化帶來的學習機會", "⭐⭐⭐⭐", "藍色/灰色", "拉長石"),
        6: ("關懷與責任之年", "承擔過多，容易忽略自我", "設定合理界限，兼顧自我與關懷他人", "⭐⭐⭐", "粉色/綠色", "綠幽靈"),
        7: ("內省與學習之年", "容易孤立自己或陷入過度思考", "定期與信任的人分享想法，保持平衡", "⭐⭐⭐", "藍色/紫色", "青金石"),
        8: ("事業與財務之年", "忙於追求成就，忽略情感或健康", "調整節奏，均衡物質與內在需求", "⭐⭐⭐⭐", "金色/黃色", "黃水晶"),
        9: ("收尾與釋放之年", "抵抗改變，容易陷入情緒回顧", "練習放手與感恩，為新階段留出空間", "⭐⭐⭐", "白色/銀色", "月光石"),
    }
    return advice_dict.get(main_number, ("未知年份", "", "", "⭐", "白色", "白水晶"))

# ---------- Streamlit 介面 ----------
st.set_page_config(page_title="流年生命靈數計算器", layout="centered")
st.title("🌟 生命靈數流年計算器")
st.markdown("輸入你的生日與查詢年份，即可獲得個人化流年指引與建議。")

# 輸入
birth_input = st.text_input("請輸入生日 (YYYY/MM/DD)", "1979/12/03")
query_year = st.number_input("請輸入查詢年份", min_value=1900, max_value=2100, value=2025)

if st.button("計算流年"):
    try:
        year, month, day = map(int, birth_input.split("/"))
        total_sum, mid_sum, main_number = calculate_life_number(year, month, day, query_year)
        year_title, challenge, action, stars, lucky_color, crystal = get_year_advice(main_number)

        st.markdown("### 📊 流年結果")
        st.write(f"**流年組合數：** {total_sum} / {mid_sum} / {main_number}")
        st.write(f"**主數流年主題：** {year_title}")
        st.write(f"**年度運勢指數：** {stars}")
        st.write(f"**可能挑戰：** {challenge}")
        st.write(f"**建議行動：** {action}")
        st.write(f"**幸運顏色：** {lucky_color}")
        st.write(f"**建議水晶：** {crystal}")

    except Exception as e:
        st.error("請確認生日格式正確，例如：1979/12/03")
