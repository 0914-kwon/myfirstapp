import streamlit as st

st.set_page_config(page_title="MBTI 클래식 추천", page_icon="📚")

# 헤더
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>📚 MBTI 고전책 + 포켓몬 추천 💬</h1>", unsafe_allow_html=True)
st.markdown("### 당신의 MBTI를 선택하면, 맞춤 추천을 해드려요! 😊")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("MBTI를 선택하세요:", mbti_list)

# 추천 데이터
recommendations = {
    "INTJ": {
        "books": ["1984 - 조지 오웰", "군주론 - 마키아벨리", "이기적 유전자 - 리처드 도킨스"],
        "pokemon": "뮤츠 🧠"
    },
    "ENFP": {
        "books": ["작은 아씨들 - 루이자 메이 올콧", "어린 왕자 - 생텍쥐페리", "데미안 - 헤르만 헤세"],
        "pokemon": "피카츄 ⚡"
    },
    "ISTJ": {
        "books": ["변신 - 프란츠 카프카", "죄와 벌 - 도스토옙스키", "월든 - 헨리 데이비드 소로"],
        "pokemon": "거북왕 🛡️"
    },
    "INFP": {
        "books": ["연을 쫓는 아이 - 할레드 호세이니", "안나 카레니나 - 톨스토이", "보바리 부인 - 플로베르"],
        "pokemon": "이브이 🌸"
    },
    "ENTP": {
        "books": ["화폐 전쟁 - 쑹훙빙", "멋진 신세계 - 올더스 헉슬리", "프랭클린 자서전 - 벤저민 프랭클린"],
        "pokemon": "리자몽 🔥"
    },
    # 나머지도 원하면 추가 가능!
}

if selected_mbti in recommendations:
    st.markdown("---")
    st.subheader(f"📖 {selected_mbti}에게 어울리는 고전책 3권:")
    for book in recommendations[selected_mbti]["books"]:
        st.markdown(f"- {book}")

    st.subheader(f"🧡 추천 포켓몬:")
    st.markdown(f"### {recommendations[selected_mbti]['pokemon']}")
else:
    st.info("선택한 MBTI에 대한 추천이 준비 중이에요!")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Made with 🥰 by 강</div>", unsafe_allow_html=True)
