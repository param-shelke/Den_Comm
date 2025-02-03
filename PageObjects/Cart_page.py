from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    women_dropdown_xpath = (By.XPATH, '//*[@id="ui-id-4"]/span[2]')
    women_tops_link_drop_xpath = (By.XPATH, '//*[@id="ui-id-9"]')
    women_top_jackets_link_xpath = (By.XPATH, '//*[@id="ui-id-11"]')
    size_jackets_xpath = (By.XPATH, "//*[@class='swatch-opt-1396']/div/div/div[1][contains(@option-id, '166')]")
    color_black_xpath = (By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[2]/div["
                                   "2]/div/div[1]")
    addto_cart_button_xpath = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div['
                                         '1]/form/button/span')
    cart_page_button_xpath = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a')
    quanity_xpath = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[1]/span[1]')
    Item_in_cart_string_xpath = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[1]/span[2]')
