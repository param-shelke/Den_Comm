# # from selenium import webdriver
# # from selenium.webdriver import ActionChains
# #
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.select import Select
# #
# # driver = webdriver.Chrome()
# # driver.maximize_window()
# # driver.implicitly_wait(10)
# # driver.get('https://magento.softwaretestingboard.com/')
# #
# # driver.find_element((By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li[2]/a')).click()
# # driver.find_element((By.ID, 'email')).send_keys('param@123gmail.com')
# # driver.find_element(By.ID,'pass').send_keys('Param@123')
# # driver.find_element(By.ID, 'send2').click()
# # driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button').click()
# # signout_link_xpath = driver.find_elements(By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li['
# #                                                     '2]/div/ul/li[3]/a')
# # act = ActionChains(driver)
# # act.move_to_element(signout_link_xpath).click().perform()
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://magento.softwaretestingboard.com/')
#
# # Logging in
# driver.find_element(By.XPATH, '//a[@class="action skip contentarea"]/following-sibling::ul/li[2]/a').click()
# driver.find_element(By.ID, 'email').send_keys('param@123gmail.com')
# driver.find_element(By.ID, 'pass').send_keys('Param@123')
# driver.find_element(By.ID, 'send2').click()
#
# # Hovering over the customer name to reveal the sign-out dropdown
# signout_button = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
# signout_button.click()
# # Using ActionChains to hover over the sign-out button
#
#
# sign_out_link = driver.find_element(By.XPATH,'/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a')
# act = ActionChains(driver)
# act.move_to_element(sign_out_link).click().perform()
# #
# # # Wait until the Sign Out link becomes clickable and click it
# # signout_link = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.XPATH, '//a[@class="action switch"]'))
# # )
# # signout_link.click()
#
# # Close the browser
# driver.quit()
