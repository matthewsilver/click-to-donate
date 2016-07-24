'''
Click on click to donate websites!
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.care2.com/click-to-donate/rainforest/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/children/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/big-cats/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/breast-cancer/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/seals/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/animal-rescue/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/oceans/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/primates/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/global-warming/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/violence-against-women/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.get('http://www.care2.com/click-to-donate/wolves/')
driver.find_element_by_xpath('//*[@id="c2dm-click-clickToBtn"]').click()
driver.quit()
