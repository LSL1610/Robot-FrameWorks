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


    def Report_Check_File_And_Send_Img(self, report_file, name_event, name_img:list,img_path,report_internet, my_timeout=30):
        my_path = "D:\OutputThien\Report_Raw\img_failed"
        Check_file = path.join(my_path, img_path)
        tb = telebot.TeleBot(Token_Bot_txt)
        # "id":-674959623,"title":"Check file txt and report"
        chat_id = my_token.CHAT_ID_API_SUN_789_MAN
        Hai = f'[Arthur CG 2r](tg://user?id=5645566151)'
        Hau = f'[Elandorr](tg://user?id=6262999939)'
        msg = f'@dangvolca, @Akira54, @khaiars, @longlam88, ' + Hau + Hai + '\n\n' + f'{report_internet}, {name_event} failed:' + '\n'
        #msg= f"demo"
        msg_no_issue = f'{report_internet} {name_event} no issue.'
        if report_file not in listdir(Check_file):
            tb.send_message(chat_id, msg_no_issue, timeout=my_timeout)
            print("khong co file failed")
        else:
            with open(f"{Check_file}\\{report_file}", "r", encoding='utf-8') as f:
                contents = f.read()
                if 'FAILED' in contents:
                    tb.send_message(chat_id, text=msg + contents,parse_mode="Markdown", timeout=my_timeout)
                    for img_brand in name_img:
                        if img_brand not in listdir(Check_file):
                            print("nothing")
                        else:
                            print(img_brand)
                            tb.send_photo(chat_id, photo=open(f'{Check_file}\\{img_brand}', 'rb'))
                else:
                    tb.send_message(chat_id, msg_no_issue, timeout=my_timeout)
                    print("khong co file failed")