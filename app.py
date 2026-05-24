import streamlit as st
from scanner import scan_market
import pandas as pd

st.set_page_config(page_title="Swing Stock Scanner", layout="wide")

st.title("📊 Swing Trading Stock Scanner")

st.write("Scan US Stocks und erhalte Swing Scores (0–100)")

if st.button("🚀 SCAN MARKET"):

    with st.spinner("Scanning stocks..."):
        results = scan_market()

    df = pd.DataFrame(results)

    st.success("Scan completed!")

    st.dataframe(df, use_container_width=True)

    st.bar_chart(df.set_index("symbol")["score"])

st.markdown("---")
st.write("💡 Klick auf Scan, um Momentum Stocks zu finden")
