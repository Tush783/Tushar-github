import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from tests.conftest import take_screenshot
from utilities.BaseClass import BaseClass


#All the test cases are mapped under this class
class TestMap(BaseClass):

     def test_mapcase(self):
        log = self.getLogger()

        loginPage = LoginPage(self.driver)
        loginPage.username().send_keys("TusharShetty")
        loginPage.password().send_keys("Tushar")
        loginPage.loginButton().click()

        time.sleep(5)

        homePage = HomePage(self.driver) #Home Page Object Created
        land_details = homePage.get_Land_Details()
        log.info("Getting all the land details")
        download_buttons = homePage.download_Buttons()
        i = 0

        for dl in download_buttons:
            dl.click()
            time.sleep(2)
            try:
                error_message = homePage.map_not_found()
                #error_message = self.driver.find_element(By.XPATH, "//div[@class='ant-notification-notice-message']")
                if error_message.is_displayed():
                    log.info(f"Unexpected error message: download failed - {land_details[i].text}")
                    take_screenshot(self.driver, land_details[i].text)
                    i += 1

            except NoSuchElementException:
                log.info(f"Map Downloaded Successfully: {land_details[i].text}")
                take_screenshot(self.driver, land_details[i].text)
                i += 1












