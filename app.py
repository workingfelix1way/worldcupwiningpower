import streamlit as st
import pandas as pd
import numpy as np
from src.data_pipeline import DataPipeline
from src.ai_model import WorldCupPredictor

st.set_page_config(page_title="World Cup 2026 AI Predictor", page_icon="⚽", layout="wide")
st.title("⚽ Hệ Thống Trí Tuệ Nhân Tạo Dự Đoán Toàn Diện World Cup 2026")
st.markdown("### Contributed by: **Nguyễn Thế Anh(C), Phạm Thảo Nguyên, Phạm Quang Thái**")
st.write("---")

@st.cache_resource
def initialize_system():
    pipeline = DataPipeline()
    df_team_strength, df_ml = pipeline.process()
    predictor = WorldCupPredictor()
    predictor.train(df_ml)
    return df_team_strength, predictor

try:
    df_team_strength, predictor = initialize_system()
except Exception as e:
    st.error(f"⚠️ Thất bại khi khởi tạo hệ thống dữ liệu: {e}")
    st.info("💡 Mẹo: Hãy chắc chắn bạn đã chạy file download_data.py để có thư mục data/raw/")
    st.stop()

st.header("🔮 Trình Giả Lập Dự Đoán Kết Quả Trận Đấu")
all_teams = sorted(df_team_strength.index.tolist())

col1, col2 = st.columns(2)
with col1: 
    team_home = st.selectbox("Chọn Đội Nhà (Home Team):", all_teams, index=all_teams.index("Argentina") if "Argentina" in all_teams else 0)

with col2: 
    away_teams_options = [team for team in all_teams if team != team_home]
    team_away = st.selectbox("Chọn Đội Khách (Away Team):", away_teams_options, index=0)

m_type = st.radio("Tính chất vòng đấu:", ["Vòng bảng (Có xác suất Hòa)", "Vòng Loại Trực Tiếp (Knock-out)"])
is_ko = True if m_type == "Vòng Loại Trực Tiếp (Knock-out)" else False

if st.button("🔥 KÍCH HOẠT DỰ ĐOÁN KẾT QUẢ", use_container_width=True):
    h_stats = df_team_strength.loc[team_home]
    a_stats = df_team_strength.loc[team_away]
    
    proba = predictor.predict_proba(h_stats, a_stats)
    p_away, p_draw, p_home = proba[0], proba[1], proba[2]
    
    if is_ko:
        total = p_home + p_away if (p_home + p_away) > 0 else 1
        p_home, p_away, p_draw = p_home / total, p_away / total, 0.0

    st.write("### 📝 Kết quả phân tích phân phối xác suất:")
    st.text(f"• Tỷ lệ {team_home} Thắng: {p_home*100:.1f}%")
    if not is_ko:
        st.text(f"• Tỷ lệ Hai đội Hòa: {p_draw*100:.1f}%")
    st.text(f"• Tỷ lệ {team_away} Thắng: {p_away*100:.1f}%")
    
    st.write("### 💰 Tỷ lệ cược tham chiếu hệ thống (Decimal Odds):")
    st.text(f"• Cửa {team_home} Thắng: {1/p_home:.2f}" if p_home > 0 else f"• Cửa {team_home} Thắng: N/A")
    if not is_ko:
        st.text(f"• Cửa Hòa nhau: {1/p_draw:.2f}" if p_draw > 0 else "• Cửa Hòa nhau: N/A")
    st.text(f"• Cửa {team_away} Thắng: {1/p_away:.2f}" if p_away > 0 else f"• Cửa {team_away} Thắng: N/A")
    
    st.write("---")
    if p_home > p_away and p_home > p_draw:
        st.success(f"🏆 **KẾT LUẬN:** Mô hình dự đoán **{team_home}** chiếm ưu thế và có khả năng chiến thắng cao nhất!")
    elif p_away > p_home and p_away > p_draw:
        st.info(f"🏆 **KẾT LUẬN:** Mô hình dự đoán **{team_away}** chiếm ưu thế và có khả năng chiến thắng cao nhất!")
    else:
        st.warning("🤝 **KẾT LUẬN:** Trận đấu này có cục diện vô cùng cân bằng, xu hướng kết thúc với kết quả Hòa.")