import streamlit as st

st.set_page_config(page_title="MBTI 도서+포켓몬 추천", page_icon="📚")

# 제목
st.markdown("<h1 style='text-align:center; color:#6C63FF;'>📖 MBTI 책 + 포켓몬 추천 🎈</h1>", unsafe_allow_html=True)
st.markdown("#### 나의 성격에 어울리는 책과 포켓몬을 찾아보세요! 🎯")

# MBTI 목록 및 설명
mbti_info = {
    "INTJ": ("전략가형: 계획 세우고 몰입하는 유형", "뮤츠", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png"),
    "INTP": ("논리적 사색가: 아이디어에 열정적인 분석가", "프테라", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/142.png"),
    "ENTJ": ("지도자형: 리더십이 뛰어나고 통솔력 강함", "갸라도스", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png"),
    "ENTP": ("토론가형: 아이디어와 말하기 좋아하는 발명가", "리자몽", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png"),
    "INFJ": ("선의의 옹호자: 이상주의자 + 조용한 추진력", "루기아", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png"),
    "INFP": ("중재자형: 감성적이고 상상력 풍부", "이브이", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png"),
    "ENFJ": ("정의로운 사회운동가: 타인을 이끄는 따뜻한 성격", "피죤투", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/018.png"),
    "ENFP": ("활동가형: 열정적이고 창의력 넘침", "피카츄", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png"),
    "ISTJ": ("논리주의자: 철저하고 실용적인 성격", "거북왕", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png"),
    "ISFJ": ("수호자형: 성실하고 조용한 도우미", "마자용", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/122.png"),
    "ESTJ": ("경영자형: 조직적이고 전통을 중시함", "코뿌리", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/112.png"),
    "ESFJ": ("사교적인 돌보미: 사람을 챙기고 친절함", "푸린", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png"),
    "ISTP": ("장인형: 실용적이고 논리적인 문제해결자", "다크펫", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/359.png"),
    "ISFP": ("예술가형: 조용하고 예술적 감각 뛰어남", "부스터", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/136.png"),
    "ESTP": ("모험가형: 에너지 넘치고 즉흥적", "딱구리", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/084.png"),
    "ESFP": ("연예인형: 사교적이고 유쾌한 성격", "토게피", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/175.png"),
}

mbti_choice = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_info.keys()))

if mbti_choice:
    st.markdown("---")
    desc, pokemon, img_url = mbti_info[mbti_choice]
    
    # MBTI 설명
    st.subheader(f"🔎 {mbti_choice} 성격 설명")
    st.markdown(f"**{desc}**")
    
    # 책 추천
    st.subheader("📚 책 추천 리스트")
    st.markdown("**고전 도서:**")
    classics = {
        "INTJ": ["1984 - 조지 오웰", "군주론 - 마키아벨리"],
        "INFP": ["연을 쫓는 아이 - 호세이니", "데미안 - 헤르만 헤세"],
        "ENTP": ["멋진 신세계 - 헉슬리", "프랭클린 자서전"],
        "ESFP": ["오만과 편견 - 제인 오스틴", "어린 왕자 - 생텍쥐페리"],
        # 기본 추천 (나머지 공통으로)
    }
    moderns = {
        "INTJ": ["생각에 관한 생각 - 대니얼 카너먼", "AI 2041 - 카이푸 리"],
        "INFP": ["아몬드 - 손원평", "82년생 김지영 - 조남주"],
        "ENTP": ["인간 본성에 대하여 - 리처드 도킨스", "사피엔스 - 유발 하라리"],
        "ESFP": ["내일은 없어 - 김영하", "모두 거짓말을 한다 - 세스 스티븐스"],
    }

    for book in classics.get(mbti_choice, ["노인과 바다 - 헤밍웨이", "변신 - 카프카"]):
        st.markdown(f"- {book}")

    st.markdown("**최신 도서:**")
    for book in moderns.get(mbti_choice, ["트렌드 코리아 2025", "파친코 - 이민진"]):
        st.markdown(f"- {book}")

    # 포켓몬 추천
    st.subheader("🧡 포켓몬 추천")
    st.markdown(f"**{pokemon}**와 잘 어울려요!")
    st.image(img_url, width=200)

    # 풍선 효과
    st.balloons()

# 푸터
st.markdown("---")
st.markdown("<div style='text-align:center; color:gray;'>📘 Made with ❤️ by 강 선생님과 ChatGPT</div>", unsafe_allow_html=True)
