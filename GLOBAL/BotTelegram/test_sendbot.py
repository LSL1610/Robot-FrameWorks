import datetime
import re
import telebot
import sys
import os
from os import path , listdir
from pathlib import Path
from my_token import MyToken
import datetime
from PIL import Image

#H:\My Drive\Projects\bot_telegram\Tai

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


my_token = MyToken()
Token_Bot_txt = my_token.txt_bot
Token_Bot_excel = my_token.excel_bot


class MyUtilsBotTelegram:
    def __init__(self) -> None:
        pass

    def Report_Check_Link_Apps(self):
        tb = telebot.TeleBot(Token_Bot_txt)
        chat_id = my_token.CHAT_ID_INT_AUTO_CHECK_APP_STORE
        msg_no_issue = f'INT_No issue download links.'
        msg_issue = '@SonCG2003\nTest2\n'
        tb.send_message(chat_id, text=msg_issue)
                
#test:
abc = MyUtilsBotTelegram()
abc.Report_Check_Link_Apps()