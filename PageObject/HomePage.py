from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver): #Driver passed to the constructor
        self.driver = driver

    #Storing the HomePage WebElements
    landItems = (By.XPATH,"//*[@class='ant-tree-node-content-wrapper ant-tree-node-content-wrapper-normal']")
    downloadButtons = (By.XPATH, "//span[@aria-label = 'download']")
    alertError = (By.XPATH, "//div[@class='ant-notification-notice-message']")


    def get_Land_Details(self):
        return self.driver.find_elements(*HomePage.landItems)

    def download_Buttons(self):
        return self.driver.find_elements(*HomePage.downloadButtons)

    def map_not_found(self):
        return self.driver.find_element(*HomePage.alertError)