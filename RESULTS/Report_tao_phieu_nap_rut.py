import sys
from os import path
from pathlib import Path

report_path = Path(__file__).resolve().parents[1]
print(report_path)
report_file = path.join(report_path, r"GLOBAL\BotTelegram")
print(report_file)
sys.path.append(report_file)

#Import file telegram:
from send_bot import *

report_internet = "Viettel"
print(report_file)
Check_nap = 'tao_check_nap.txt'
Check_rut = 'tao_check_rut.txt'
list_brand = ["789.png" , "SUN.png" , "MAN.png"]
img_checknap = "Check Phieu Nap"
img_checkrut = "Check Phieu Rut"

# def GetNameByNetwork():
#     # s = speedtest.Speedtest()
#     res = s.config
#     name = res["client"]["isp"]
#     if "Viettel" in name :
#         name = "Viettel"
#     elif "FPT" in name:
#         name = "FPT"
#     elif "VNPT" in name:
#         name = "VNPT"
#     else:
#         name = "MOBI"
#     return name

name_internet = "Viettel"
try:
    final = MyUtilsBotTelegram()
    final.Report_Check_File_And_Send_Img(Check_nap, 'tạo phiếu nạp SUN 789', list_brand,img_checknap, name_internet)
    final.Report_Check_File_And_Send_Img(Check_rut, 'tạo phiếu rút SUN 789 MAN', list_brand,img_checkrut, name_internet)
except Exception as e:
    print("debug rp tao phieu nap rut", e) 