import streamlit as st
import pandas as pd
import altair as alt
import os

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 시각화", page_icon="🌍")
st.markdown("<h1 style='text-align:center;'>🌍 국가별 MBTI Top 3 시각화</h1>", unsafe_allow_html=True)

# CSV 파일 경로
DATA_FILE = "countriesMBTI_16types.csv"

# 파일 존재 여부 확인
if not os.path.exists(DATA_FILE):
    st.error("❗ 데이터 파일이 누락되었습니다. 'countriesMBTI_16types.csv' 파일이 현재 폴더에 있어야 합니다.")
else:
    # 데이터 불러오기
    @st.cache_data
    def load_data():
        return pd.read_csv(DATA_FILE)

    df = load_data()

    # 국가 목록
    countries = df["Country"].tolist()
    selected_country = st.selectbox("국가를 선택하세요:", countries)

    if selected_country:
        # 해당 국가의 MBTI 데이터
        row = df[df["Country"] == selected_country].iloc[0]
        mbti_scores = row.drop("Country")
        top3 = mbti_scores.sort_values(ascending=False).head(3)

        top3_df = pd.DataFrame({
            "MBTI": top3.index,
            "비율": top3.values
        })

        # 결과 출력
        st.subheader(f"📊 {selected_country}에서 가장 많은 MBTI Top 3")
        chart = alt.Chart(top3_df).mark_bar(color="#6C63FF").encode(
            x=alt.X("MBTI", sort="-y"),
            y=alt.Y("비율", title="비율 (%)", scale=alt.Scale(domain=[0, top3_df["비율"].max() * 1.2])),
            tooltip=["MBTI", alt.Tooltip("비율", format=".2%")]
        ).properties(
            width=500,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)

        # 표로도 출력
        st.dataframe(top3_df.style.format({"비율": "{:.2%}"}))

    st.markdown("---")
    st.markdown("<div style='text-align:center; color:gray;'>📘 Made with ❤️ by 강 선생님</div>", unsafe_allow_html=True)
