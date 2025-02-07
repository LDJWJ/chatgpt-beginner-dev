# 데이터 캐싱, 인터랙티브 차트, 레이아웃 구성, 파일 업로드/다운로드
# 이 코드의 전체 구조는 사용자에게 데이터를 로드하고, 시각화하며, 
# 업로드 및 다운로드할 수 있는 기능을 제공하는 인터랙티브 대시보드를 만드는 것

import streamlit as st
import pandas as pd
import plotly.express as px

#
# streamlit: 웹 애플리케이션을 쉽게 만들 수 있는 라이브러리입니다.
# pandas: 데이터 처리를 위한 라이브러리입니다.
# plotly.express: 데이터 시각화를 위한 라이브러리입니다.

# 매번 애플리케이션이 재실행될때마다 연산이 다시 수행되면 성능이 저하됨.
# 캐싱을 사용하면 첫번째 실행 시 결과를 저장해 두고, 
# 이후 동일한 요청이 들어올때마다 저장된 결과를 반환하여 시간을 절약.

# @st.cache_data 데코레이터는 Streamlit에서 데이터를 캐싱하여 
# 성능을 최적화하는 데 사용됩니다. 캐싱은 시간이 오래 걸리는 
# 연산(예: 데이터 로딩, 복잡한 계산 등)의 결과를 저장해 두고, 
# 동일한 연산이 다시 호출될 때 저장된 결과를 재사용하여 시간을 절약하는 기법입니다. 
# Streamlit에서는 주로 데이터 로딩이나 처리 단계에서 많이 사용됩니다.
@st.cache_data
def load_data():
    return pd.DataFrame({
        '날짜': pd.date_range(start='2023-01-01', periods=100),
        '판매량': [100 + i * 2 + (i % 7) * 10 for i in range(100)]
    })

st.title("인터랙티브 대시보드")

data = load_data()

st.write("데이터 미리보기:")
st.dataframe(data.head())

# 데이터를 요약하는 통계 정보를 보여줍니다. 
# 이 정보는 st.expander를 사용하여 클릭하여 확장할 수 있는 형태로 제공됩니다.
with st.expander("데이터 통계"):
    st.write(data.describe())

# 시계열 차트 
st.subheader("시계열 차트")
fig = px.line(data, x='날짜', y='판매량', title='일별 판매량')
st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("파일 업로더")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
    if uploaded_file is not None:
        st.success("파일이 성공적으로 업로드되었습니다!")

with col2:
    st.subheader("다운로드 버튼")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="CSV 다운로드",
        data=csv,
        file_name="sales_data.csv",
        mime="text/csv",
    )

# 체크박스를 사용하여 원본 데이터를 표시하거나 숨길 수 있습니다.
if st.checkbox("원본 데이터 보기"):
    st.write(data)
