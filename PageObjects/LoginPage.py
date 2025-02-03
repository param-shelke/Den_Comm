from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Login:
    sign_in_link_Xpath = (By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li[2]/a')
    email_textbox_id = (By.ID, 'email')
    password_textbox_id = (By.ID, 'pass')
    sign_in_btn_id = (By.ID, 'send2')
    # signout_drop_xpath = (By.XPATH, '//span[@class="customer-name active"]/button')
    signout_drop_xpath = (By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')

    # signout_link_xpath = (By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li[2]/div/ul/li[
    # 3]/a')
    signout_link_xpath =(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')

    def __init__(self, driver):
        self.driver = driver

    def click_On_link(self):
        self.driver.find_element(*self.sign_in_link_Xpath).click()

    def set_username(self, username):
        email_element = self.driver.find_element(*self.email_textbox_id)
        email_element.clear()
        email_element.send_keys(username)

    def set_password(self, password):
        password_element = self.driver.find_element(*self.password_textbox_id)
        password_element.clear()
        password_element.send_keys(password)

    def click_on_btn(self):
        self.driver.find_element(*self.sign_in_btn_id).click()

    def signout_drop(self):
        self.driver.find_element(*self.signout_drop_xpath).click()

    def move_to_element(self):
        act = ActionChains(self.driver)
        signout_element = self.driver.find_element(*self.signout_link_xpath)
        act.move_to_element(signout_element).click().perform()
