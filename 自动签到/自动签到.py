import selenium
import time
from selenium import webdriver
username="201606010504"
passwd="03010029"
driver = webdriver.Chrome()
driver.get('http://tb.bucea.edu.cn:8075/WebReport/ReportServer?op=fs')
driver.implicitly_wait(10)
elem=driver.find_element_by_class_name("fs-login-username")
elem.send_keys(username)
elem=driver.find_element_by_class_name("fs-login-password")
elem.send_keys(passwd)
elem=driver.find_element_by_id("fs-login-btn")
elem.click()
elem=driver.find_element_by_class_name("fs-menu-icon")
elem.click()
elem=driver.find_element_by_class_name("menutree-text")
elem.click()
driver.implicitly_wait(30)
driver.find_element_by_css_selector(".x-text.fr-widget-click.fr-radio-radioon")