import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tính lãi tiết kiệm", page_icon="🏦", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #e0f7fa 0%, #fff8e1 100%); }
h1 { color: #00695c; text-align: center; }
div.stButton > button {
    background-color: #00897b; color: white; font-size: 18px;
    border-radius: 10px; width: 100%; height: 3em; border: none;
}
div.stButton > button:hover { background-color: #00695c; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("🏦 Tính lãi tiền gửi tiết kiệm")
st.caption("Mini App Tài chính - Ngân hàng | Nhóm N05")

col1, col2 = st.columns(2)
with col1:
    von = st.number_input("💵 Số tiền gửi (VNĐ)", min_value=0, value=100_000_000, step=1_000_000)
    thang = st.selectbox("📅 Kỳ hạn (tháng)", [1, 3, 6, 9, 12, 18, 24, 36], index=4)
with col2:
    lai = st.number_input("📈 Lãi suất (%/năm)", min_value=0.0, value=5.0, step=0.1)
    kieu = st.radio("🔁 Loại lãi", ["Lãi đơn", "Lãi kép"])

if st.button("💰 Tính lãi"):
    r = lai / 100
    lai_don = von * r * thang / 12
    lai_kep = von * ((1 + r / 12) ** thang - 1)
    tien_lai = lai_don if kieu == "Lãi đơn" else lai_kep

    c1, c2, c3 = st.columns(3)
    c1.metric("Tiền gửi", f"{von:,.0f}")
    c2.metric("Tiền lãi", f"{tien_lai:,.0f}")
    c3.metric("Tổng nhận", f"{von + tien_lai:,.0f}")
    st.balloons()

    st.subheader("📊 So sánh lãi đơn và lãi kép")
    ds_thang = list(range(0, thang + 1))
    df = pd.DataFrame({
        "Tháng": ds_thang,
        "Lãi đơn": [von + von * r * t / 12 for t in ds_thang],
        "Lãi kép": [von * (1 + r / 12) ** t for t in ds_thang],
    }).set_index("Tháng")
    st.line_chart(df)

    st.info(
        f"Lãi đơn: {lai_don:,.0f} VNĐ | Lãi kép: {lai_kep:,.0f} VNĐ | "
        f"Chênh lệch: {lai_kep - lai_don:,.0f} VNĐ"
    )
