import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ==========================================
# CẤU HÌNH GIAO DIỆN WEB (STREAMLIT)
# ==========================================
st.set_page_config(
    page_title="Hệ thống AI - Dự đoán World Cup 2026", 
    page_icon="⚽", 
    layout="wide"
)

st.title("⚽ Hệ Thống Trí Tuệ Nhân Tạo Dự Đoán Toàn Diện World Cup 2026")
st.markdown("### Đồ án môn học: Nhập môn Trí tuệ nhân tạo (Mức độ: Cao cấp - Mục tiêu: A+)")
st.write("---")

# ==========================================
# 1. TẢI VÀ TIỀN XỬ LÝ DỮ LIỆU ĐỘNG
# ==========================================
@st.cache_data
def load_and_preprocess_data():
    raw_dir = 'data/raw'
    file_historico = None
    file_fixture = None
    
    if os.path.exists(raw_dir):
        for file in os.listdir(raw_dir):
            if 'historic' in file.lower() or 'results' in file.lower():
                file_historico = os.path.join(raw_dir, file)
            elif 'fixture' in file.lower() or 'match' in file.lower():
                file_fixture = os.path.join(raw_dir, file)

    if not file_historico: file_historico = os.path.join(raw_dir, 'clean_fifa_worldcup_historical_data.csv')
    if not file_fixture: file_fixture = os.path.join(raw_dir, 'format_fixture_data.csv')
        
    df_historico = pd.read_csv(file_historico)
    df_fixture = pd.read_csv(file_fixture)
    df_historico.dropna(subset=['home', 'away', 'home_goals', 'away_goals'], inplace=True)
    
    df_home = df_historico[['home', 'home_goals', 'away_goals']].rename(
        columns={'home': 'team', 'home_goals': 'goals_scored', 'away_goals': 'goals_conceded'}
    )
    df_away = df_historico[['away', 'home_goals', 'away_goals']].rename(
        columns={'away': 'team', 'home_goals': 'goals_conceded', 'away_goals': 'goals_scored'}
    )
    df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby('team').mean()
    
    df_historico['match_result'] = np.where(df_historico['home_goals'] > df_historico['away_goals'], 2,
                                   np.where(df_historico['home_goals'] == df_historico['away_goals'], 1, 0))
    
    df_ml = df_historico.copy()
    df_ml['home_attack'] = df_ml['home'].map(df_team_strength['goals_scored']).fillna(1.0)
    df_ml['home_defense'] = df_ml['home'].map(df_team_strength['goals_conceded']).fillna(1.0)
    df_ml['away_attack'] = df_ml['away'].map(df_team_strength['goals_scored']).fillna(1.0)
    df_ml['away_defense'] = df_ml['away'].map(df_team_strength['goals_conceded']).fillna(1.0)
    df_ml['attack_diff'] = df_ml['home_attack'] - df_ml['away_attack']
    
    return df_team_strength, df_fixture, df_ml

try:
    df_team_strength, df_fixture, df_ml = load_and_preprocess_data()
except Exception as e:
    st.error("### ⚠️ Hệ thống chưa nhận diện được tệp dữ liệu!")
    st.stop()

# ==========================================
# 2. HUẤN LUYỆN MÔ HÌNH HỌC MÁY (RANDOM FOREST)
# ==========================================
@st.cache_resource
def train_ml_model(df):
    features = ['home_attack', 'home_defense', 'away_attack', 'away_defense', 'attack_diff']
    X = df[features]
    y = df['match_result']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    return model

ml_model = train_ml_model(df_ml)

# ==========================================
# 3. LOGIC DỰ ĐOÁN XÁC SUẤT TRẬN ĐẤU
# ==========================================
def predict_match_probabilities(home, away, is_knockout=False):
    h_att = df_team_strength.loc[home, 'goals_scored'] if home in df_team_strength.index else 1.0
    h_def = df_team_strength.loc[home, 'goals_conceded'] if home in df_team_strength.index else 1.0
    a_att = df_team_strength.loc[away, 'goals_scored'] if away in df_team_strength.index else 1.0
    a_def = df_team_strength.loc[away, 'goals_conceded'] if away in df_team_strength.index else 1.0
    
    features = np.array([[h_att, h_def, a_att, a_def, h_att - a_att]])
    proba = ml_model.predict_proba(features)[0]
    p_away, p_draw, p_home = proba[0], proba[1], proba[2]
    
    if is_knockout:
        total = p_home + p_away if (p_home + p_away) > 0 else 1
        p_home, p_away, p_draw = p_home / total, p_away / total, 0.0
        
    return p_home, p_draw, p_away

# ==========================================
# 4. GIAO DIỆN CHÍNH (ĐÃ LƯỢC BỎ TAB)
# ==========================================
st.header("🔮 Trình Giả Lập Dự Đoán Kết Quả Trận Đấu")
all_teams = sorted(df_team_strength.index.tolist())

col_sel1, col_sel2 = st.columns(2)
with col_sel1: 
    team_home = st.selectbox("Chọn Đội Nhà:", all_teams, index=all_teams.index("Argentina") if "Argentina" in all_teams else 0)
with col_sel2: 
    team_away = st.selectbox("Chọn Đội Khách:", all_teams, index=all_teams.index("France") if "France" in all_teams else 1)

m_type = st.radio("Vòng đấu:", ["Vòng bảng (Có xác suất Hòa)", "Vòng Loại Trực Tiếp (Knock-out)"])
is_ko = True if m_type == "Vòng Loại Trực Tiếp (Knock-out)" else False

if st.button("🔥 KÍCH HOẠT DỰ ĐOÁN KẾT QUẢ", use_container_width=True):
    if team_home == team_away:
        st.error("Vui lòng chọn 2 đội khác nhau!")
    else:
        p_h, p_d, p_a = predict_match_probabilities(team_home, team_away, is_knockout=is_ko)
        
        st.write("### 📝 Kết quả phân tích từ AI:")
        st.text(f"• Tỷ lệ {team_home} Thắng: {p_h*100:.1f}%")
        if not is_ko:
            st.text(f"• Tỷ lệ Hai đội Hòa: {p_d*100:.1f}%")
        st.text(f"• Tỷ lệ {team_away} Thắng: {p_a*100:.1f}%")
        
        st.write("---")
        # Dòng kết luận bằng hộp thông báo màu sắc gọn gàng
        if p_h > p_a and p_h > p_d:
            st.success(f"🏆 **KẾT LUẬN:** Mô hình dự đoán **{team_home}** chiếm ưu thế và có khả năng chiến thắng cao nhất!")
        elif p_a > p_h and p_a > p_d:
            st.info(f"🏆 **KẾT LUẬN:** Mô hình dự đoán **{team_away}** chiếm ưu thế và có khả năng chiến thắng cao nhất!")
        else:
            st.warning("🤝 **KẾT LUẬN:** Trận đấu này có cục diện vô cùng cân bằng, xu hướng kết thúc với kết quả Hòa.")