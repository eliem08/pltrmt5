import requests
from flask import Flask, request, jsonify

# ✅ Replace with your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "8189283095:AAGO3ofh_F4lJlRil04AmKA8cyawq-zezYw"
TELEGRAM_CHAT_ID = "700424020"

app = Flask(__name__)

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json  # Receive JSON from TradingView webhook

    if not data or "action" not in data:
        return jsonify({"status": "error", "message": "Invalid request"}), 400

    # Format trade message
    trade_msg = f"📈 Trade Alert: {data['action']} {data['symbol']}\n"
    trade_msg += f"🔹 Size: {data['size']}\n"
    trade_msg += f"🛑 Stop Loss: {data['stop_loss']}\n"
    trade_msg += f"🎯 Take Profit: {data['take_profit']}"

    # Send message to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(telegram_url, json={"chat_id": TELEGRAM_CHAT_ID, "text": trade_msg})

    return jsonify({"status": "sent"}), 200

# Vercel requires this
def handler(request):
    return app(request)
