from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Create_Account:
    create_account_link_XPATH = (By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li[3]/a')
    first_name_text_ID = (By.ID, 'firstname')
    last_name_text_id = (By.ID, 'lastname')
    email_text_id = (By.ID, 'email_address')
    password_text_id = (By.ID, 'password')
    confirm_password_text_ID = (By.ID, 'password-confirmation')
    required_filed_textword_red = (By.XPATH, '//*[@id="form-validate"]/fieldset[2]')
    create_button_Xpath = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')

    sucsess_message = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div/text()')

    def __init__(self, driver):
        self.driver = driver

    def click_on_create_acccount_link(self):
        self.driver.find_element(*self.create_account_link_XPATH).click()

    def Enter_username(self, username):
        self.driver.find_element(*self.first_name_text_ID).send_keys(username)

    def Enter_lastname(self, lastname):
        self.driver.find_element(*self.last_name_text_id).send_keys(lastname)

    def Enter_email(self, email):
        self.driver.find_element(*self.email_text_id).send_keys(email)

    def Enter_password(self, password):
        self.driver.find_element(*self.password_text_id).send_keys(password)

    def Enter_password_confirm(self, pass1):
        self.driver.find_element(*self.confirm_password_text_ID).send_keys(pass1)

    def click_on_create_button(self):
        self.driver.find_element(*self.create_button_Xpath).click()

    def get_success_msg(self):
        return self.driver.find_element(*self.sucsess_message).text()
