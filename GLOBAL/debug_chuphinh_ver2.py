import cv2
import numpy as np
import time
from PIL import Image
from appium import webdriver
from selenium import webdriver
from ppadb.client import Client
from io import BytesIO
from robot.api import logger

# driver:
def Driver_mobile(url):
    "Setup for the test"
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = '901KPDT2061490'
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
    driver = webdriver.Remote('http://127.0.0.1:8210/wd/hub', desired_caps)
    driver.get(url)
    return driver

#return url:


def find_image(device_name,img_path, timeout=120):
    adb = Client(host='127.0.0.1', port=5037)
    #devices = adb.devices()
    device = adb.device(device_name)
    start = time.time()
    while True:
        result = device.screencap()
        with open("D:\Tai_Report_Raw\Download_Apps\Img_screencap\screen.png", "wb") as fp:
             fp.write(result)
        # new = result
        logger.info("[INFO] Loading captured images...")
        # Convert img to BytesIO
        scr = Image.open(BytesIO(result))
        #scr = Image.open(img)
        # Convert to format accepted by OpenCV
        #scr = np.asarray(scr, dtype=np.float32).astype(np.uint8)
        scr = np.array(scr)
        # ---------- fix new code Nov-4-2021
        # Convert image from BGR to RGB format
        scr = cv2.cvtColor(scr, cv2.COLOR_BGR2RGB)

        # perform template matching
        #scr_gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
        try:
            template = cv2.imread(img_path)
            width = template.shape[1]
            #logger.info(width)
            height = template.shape[0]
            assert not isinstance(img_path, type(None))  # 'image found
        except:
            logger.info(f'Image not found in path: {img_path}')
            return False

        # perform template matching
        logger.info("Performing template matching...")
        # change method TM_CCOEFF_NORMED detech multiple object
        # For TM_CCOEFF_NORMED, larger values means good fit
        res = cv2.matchTemplate(scr, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        #logger.info(max_loc)
        x = max_loc[0]
        y = max_loc[1]
        threshold = max_val
        logger.info(f"Threshold value: {threshold:.2f}")
        center_x = x + \
                   int(width / 2) if x and width else None
        center_y = y + \
                   int(height / 2) if y and height else None
        logger.info(f'Center image coordinates (x = {center_x}, y = {center_y})')

        ##---------------- End fix Code

        #logger.info('shape lan nnnnnnnnnnnnnnnnnnnn', scr.shape)
        end = time.time() - start
        logger.info("time end", end)
        if threshold >= 0.7 or round(end, 2) >= int(timeout):
            logger.info(f'End time > {end}')
            break

    return threshold, center_x, center_y
    #return threshold

#if __name__ == '__main__':
    #adb = Client(host='127.0.0.1', port=5037)
    #devices = adb.devices()
    #device = devices[2]
    #target_img = r'D:\PythonAutomation\PROJECT_AR\Image_game\test.mp4'
    #source_img = 'sdcard/Download/test.mp4'
    # img_path = r"D:\\PythonAutomation\\PROJECT_AR\\Image_game\\901KPDT2061490\\1_nut.png"
    # #driver = Driver_mobile("https://google.com")
    # device.shell(f'screencap -p {source_img}')
    # #result = device.screencap()
    #device.pull(source_img, target_img)
    # abc = find_image(img_path)
    # # cv2.imshow("winname", abc[1])
    # # cv2.waitKey()
    # # cv2.destroyAllWindows()
    # adb = Client(host='127.0.0.1', port=5037)
    # devices = adb.devices()
    # device = devices[2]
    # result = device.screencap()
    # with open("D:\Tai_Report_Raw\Download_Apps\Img_screencap\sc123reen.png", "wb") as fp:
    #     fp.write(result)
    # old_path = "D:\\File_apk\\screen.png"
    # img_path = "D:\\File_apk\\screen2.png"
    # A, B, C= find_image('901KPDT2061490',img_path,5)
    # print(A, B, C)
