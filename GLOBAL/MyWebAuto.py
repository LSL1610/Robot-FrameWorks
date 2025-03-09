import cv2
from robot.api.deco import keyword
from SeleniumLibrary import SeleniumLibrary
from robot.libraries.OperatingSystem import OperatingSystem
from robot.api import logger
import time
from selenium.webdriver.common.action_chains import ActionChains # Using action chain should be un-comment

myOs = OperatingSystem()

#chrome_path = r"G:\My Drive\Projects\drivers\chromedriver.exe"
my_img_store = r"D:\OutputThien\Report_Raw\image1"

myOs.create_directory(my_img_store)
#myOs.empty_directory(my_img_store)


class MyWebAuto(SeleniumLibrary):
    def __init__(
        self,
        timeout=30.0,
        implicit_wait=0.0,
        run_on_failure=None,
        screenshot_root_directory=my_img_store,
        plugins=None,
        event_firing_webdriver=None,
    ):

        super().__init__(
            timeout,
            implicit_wait,
            run_on_failure,
            screenshot_root_directory,
            plugins,
            event_firing_webdriver,
        )

    @keyword("Find Image OpenCV")
    def find_image_opencv(self, image_path: str) -> tuple:
        """Find image using Template Opencv

        Args:
            image_path (str): Image to compare with scr

        Returns:
            _type_: tuple (max_val, center_x, center_y)
        """
        # Get current screenshot of a web page
        scr = self.capture_page_screenshot()
        # print("Loading captured images...")
        scr = cv2.imread(scr)
        # Convert image from BGR to RGB format
        # perform template matching
        scr_gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
        try:
            template = cv2.imread(image_path, 0)
            width = template.shape[1]
            height = template.shape[0]
            assert not isinstance(image_path, type(None))  # check image path
        except Exception:
            print(f"Please check again the path of image at: {image_path}")
            
        else:
            """
            perform template matching
            print("Performing template matching...")
            change method TM_CCOEFF_NORMED detech multiple object
            For TM_CCOEFF_NORMED, larger values means good fit
            """
            res = cv2.matchTemplate(scr_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            x = max_loc[0]
            y = max_loc[1]
            # threshold = max_val
            # print(f"Threshold value: {threshold:.2f}")
            center_x = x + int(width / 2) if x and width else None
            center_y = y + int(height / 2) if y and height else None
            return (max_val, center_x, center_y)



    @keyword("Click Canvas By X Y")
    def Click_Canvas_By_X_Y(self, center_x, center_y):
        action = ActionChains(self.driver)
        action.move_by_offset(center_x, center_y)
        action.click()
        action.release()
        action.perform()
        action.reset_actions()
        print(f'Clicked on center image: {center_x, center_y}')

    @keyword("Wait for image OpenCV")
    def Wait_for_image_OpenCV(self, image_path: str, timeout=30):
        Stop_time = time.perf_counter() + timeout
        location = None
        while time.perf_counter() < Stop_time:
            try:
                location = self.find_image_opencv(image_path)
                if location[0] >= 0.8:
                    print("math image")
                    break
            except:
                pass
        if location==None:
            print(f"Image not visible in {timeout}")
            return False
        # if location[0] < 0.8:
        #     print(f"Image not visible in {timeout}")
        #     return False
        return location

    @keyword("Del folder image")
    def Del_Folder_Image(self, folderpath=my_img_store):
        myOs.empty_directory(folderpath)

