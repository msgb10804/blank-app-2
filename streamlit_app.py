import streamlit as st

# 앱 제목 설정
st.title("🍿 영화관 세트 메뉴 조합기")
st.subheader("가능한 모든 세트 메뉴 조합을 확인해보세요!")

# 기존 데이터 옵션
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 기존의 이중 for문 로직을 활용한 화면 출력
st.markdown("### 📋 전체 세트 메뉴 리스트")

for popcorn in popcorn_options:
    for drink in drink_options:
        # print() 대신 st.write()를 사용하여 스트림릿 화면에 출력합니다.
        st.write(f"🎬 **세트 메뉴:** {popcorn} 팝콘 + {drink}")
    