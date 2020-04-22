import base64
import contextlib
from PIL import Image
from io import BytesIO
from selenium.common.exceptions import WebDriverException
from utils import js_get_element_by_xpath, wait_for


class Qrcode:
    def __init__(self, driver):
        self.__driver = driver

        print("Loading QRCODE")

        with contextlib.suppress(WebDriverException):
            self.__get_qrcode_canvas()
            return

        with contextlib.suppress(WebDriverException):
            self.__get_qrcode_img()
            return

        raise Exception("Error in get QRCODE")

    def __get_qrcode_img(self):
        qrcode = wait_for(lambda: self.__driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/img"))
        qrcode_src = qrcode.get_attribute("src")

        qrcode_src = qrcode_src.replace("data:image/png;base64,", "")
        qrcode_image = Image.open(BytesIO(base64.b64decode(qrcode_src)))
        qrcode_image.save("qrcode.png", "PNG")
        qrcode_image.show()

    def __get_qrcode_canvas(self):
        canvas_64 = "return %s.toDataURL('image/png')" % js_get_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/canvas")
        qrcode_src = wait_for(lambda: self.__driver.execute_script(canvas_64))

        qrcode_src = qrcode_src.replace("data:image/png;base64,", "")
        qrcode_image = Image.open(BytesIO(base64.b64decode(qrcode_src)))
        qrcode_image.save("qrcode.png", "PNG")
        qrcode_image.show()
