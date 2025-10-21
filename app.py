import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Stock Prices", layout="wide")
st.title("Stock Prices Over Time")

df = px.data.stocks()
df["date"] = df["date"].astype("datetime64[ns]")

fig = px.line(df, x="date", y=["GOOG", "AAPL", "AMZN"], title="Stock Prices (with Range Slider & Selector)")
fig.update_layout(
    title_x=0.5,
    xaxis={
        "rangeselector": {"buttons": [
            {"count": 3, "label": "3M", "step": "month", "stepmode": "backward"},
            {"count": 6, "label": "6M", "step": "month", "stepmode": "backward"},
            {"count": 1, "label": "1Y", "step": "year", "stepmode": "backward"},
            {"step": "all", "label": "All"},
        ]},
        "rangeslider": {"visible": True},
        "type": "date",
    },
    hovermode="x unified",
    width=900,
    height=500,
)
st.plotly_chart(fig, use_container_width=True)
