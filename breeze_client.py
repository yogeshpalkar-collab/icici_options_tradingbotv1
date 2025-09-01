import streamlit as st
from breeze_connect import BreezeConnect

def init_breeze():
    try:
        breeze = BreezeConnect(api_key=st.secrets["BREEZE_API_KEY"])
        breeze.generate_session(
            api_secret=st.secrets["BREEZE_API_SECRET"],
            session_token=st.secrets["BREEZE_ACCESS_TOKEN"]
        )
        return breeze
    except Exception as e:
        st.error(f"❌ Breeze init failed: {e}")
        return None

def get_option_chain(breeze, symbol="NIFTY", expiry=None):
    try:
        data = breeze.get_option_chain_quotes(
            stock_code=symbol,
            exchange_code="NSE",
            product_type="options",
            expiry_date=expiry
        )
        return data.get("Success", [])
    except Exception as e:
        st.error(f"❌ Option chain fetch failed: {e}")
        return []

def place_order(breeze, tradingsymbol, side, qty, product_type="INTRADAY"):
    try:
        resp = breeze.place_order(
            stock_code=tradingsymbol,
            exchange_code="NFO",
            product=product_type,
            action=side,
            order_type="MARKET",
            stoploss="",
            quantity=str(qty)
        )
        return resp
    except Exception as e:
        st.error(f"❌ Order failed: {e}")
        return None
