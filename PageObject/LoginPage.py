from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Storing the Login Page WebElements
    Username = (By.ID, "login-form_username")
    Password = (By.XPATH, "//input[@placeholder = 'Password']")
    LoginButton = (By.CSS_SELECTOR, ".ant-btn")

    def username(self):
         return self.driver.find_element(*LoginPage.Username) #Using * to deserialize the tuple

    def password(self):
        return self.driver.find_element(*LoginPage.Password)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.LoginButton)