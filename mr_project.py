from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time


class Mrr:
    SIGN_IN_BUTTON = (By.ID, "idSIButton9")
    SIGN_IN_BUTTON_BI =(By.CSS_SELECTOR,".bibutton.primary")
    EMAIL_TEXT_AREA1 = (By.ID, 'i0116')
    EMAIL_TEXT_AREA = (By.XPATH, '//*[@id="i0116"]')
    ILERI = (By.ID, 'idSIButton9')
    PASSWORD_TEXT_AREA = (By.ID, 'i0118')
    OTURUM_ACIK_KALSIN = (By.ID, "KmsiCheckboxField")
    PASSWORD = " "
    EMAIL = " "
    SITE = ""
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.SITE)
        self.wait = WebDriverWait(self.driver, 30)

    def test_navigate(self):
        window_before = self.driver.window_handles[0]
        self.driver.implicitly_wait(10)
        self.wait.until(ec.presence_of_element_located(self.SIGN_IN_BUTTON_BI)).click()
        self.driver.implicitly_wait(10)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.wait.until(ec.presence_of_element_located(self.EMAIL_TEXT_AREA)).send_keys(self.EMAIL)
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.wait.until(ec.presence_of_element_located(self.ILERI)).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.wait.until(ec.presence_of_element_located(self.PASSWORD_TEXT_AREA)).send_keys(self.PASSWORD)
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.wait.until(ec.presence_of_element_located(self.SIGN_IN_BUTTON)).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.wait.until(ec.presence_of_element_located(self.OTURUM_ACIK_KALSIN)).click()
        self.driver.implicitly_wait(10)
        time.sleep(1)
        self.wait.until(ec.presence_of_element_located(self.SIGN_IN_BUTTON)).click()
        time.sleep(10)
        self.driver.refresh()

        self.driver.switch_to.window(window_before)
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        time.sleep(10)
        screenshot_path = "screenshot.png"  # Kaydedilecek ekran görüntüsünün dosya adı ve yolunu belirtir
        self.driver.implicitly_wait(30)
        self.driver.save_screenshot(screenshot_path)
        self.wait.until(ec.presence_of_element_located(self.SIGN_IN_BUTTON)).click()
        self.driver.implicitly_wait(20)
        print("Ekran görüntüsü başarıyla alındı ve {} dosyasına kaydedildi.".format(screenshot_path))

    def tearDown(self):
        self.driver.close()


Mrr().test_navigate()
