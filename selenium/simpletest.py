from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucelabs.com")
element = driver.find_element(By.XPATH, '//a[text()="Platforms"]');
element.click();
pricing_link = driver.find_element(By.XPATH, '//a[text()="Pricing"]');
pricing_link.click();
driver.close();


