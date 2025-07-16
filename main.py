import streamlit as st
import pandas as pd
import altair as alt

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 시각화", page_icon="🌍")
st.markdown("<h1 style='text-align:center;'>🌍 국가별 MBTI Top 3 시각화</h1>", unsafe_allow_html=True)

# CSV 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 국가 목록
countries = df["Country"].tolist()
selected_country = st.selectbox("국가를 선택하세요:", countries)

if selected_country:
    # 해당 국가의 데이터 가져오기
    row = df[df["Country"] == selected_country].iloc[0]
    mbti_data = row.drop("Country")

    # 상위 3개 MBTI 추출
    top3 = mbti_data.sort_values(ascending=False).head(3)
    top3_df = pd.DataFrame({
        "MBTI": top3.index,
        "비율": top3.values
    })

    st.subheader(f"📊 {selected_country}에서 가장 많은 MBTI Top 3")

    # Altair 차트 생성
    chart = alt.Chart(top3_df).mark_bar(color="#6C63FF").encode(
        x=alt.X("MBTI", sort="-y"),
        y=alt.Y("비율", title="비율 (%)", scale=alt.Scale(domain=[0, top3_df["비율"].max() * 1.2])),
        tooltip=["MBTI", alt.Tooltip("비율", format=".2%")]
    ).properties(
        width=500,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 표도 함께 출력
    st.dataframe(top3_df.style.format({"비율": "{:.2%}"}))

# 푸터
st.markdown("---")
st.markdown("<div style='text-align:center; color:gray;'>📘 Made with ❤️ by 강 선생님</div>", unsafe_allow_html=True)
