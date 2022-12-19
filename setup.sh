mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false

[theme]
primaryColor="#f50ca0"
backgroundColor="#191015"
secondaryBackgroundColor="#26161f"
textColor="#d4f7f9"
font="sans serif"
" > ~/.streamlit/config.toml
