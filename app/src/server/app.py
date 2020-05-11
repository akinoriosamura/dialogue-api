import os
import datetime
import json

from src.nlp.dialogue_manager import DialogueManager

from flask import Flask, abort, request, jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FlexSendMessage, MessageEvent, TextMessage, TextSendMessage, LocationMessage
)


#  initialize app db migrate
def create_app(test=False):
    app = Flask(__name__)

    return app

app = create_app()
dm = DialogueManager()

# LINE Access Token
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# LINE Channel Secret
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'callback OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    print("reply token: ", event.reply_token)
    if event.type == "message":
        input_t = event.message.text
        target_t = dm.get_reply(input_t)
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text=target_t),
            ]
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="話しかけてみてね！"))
