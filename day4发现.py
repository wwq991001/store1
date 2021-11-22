from appium import webdriver
from appium.webdriver.common.mobileby import By
import time
from appium.webdriver.common.touch_action import TouchAction

url = "127.0.0.1:4723/wd/hub"
param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.sina.weibo",
  "appActivity": "com.sina.weibo.SplashActivity"
}
# 'com.xindong.rocket.activity.LaunchActivity

driver = webdriver.Remote(url, param)

driver.implicitly_wait(7)

TouchAction(driver).tap(x=473, y=795).perform()
driver.implicitly_wait(7)
time.sleep(4)
TouchAction(driver).tap(x=500, y=709).perform()
driver.implicitly_wait(7)
time.sleep(4)
TouchAction(driver).tap(x=347, y=1237).perform()
driver.implicitly_wait(7)
time.sleep(4)
TouchAction(driver).tap(x=400, y=72).perform()
driver.implicitly_wait(7)
time.sleep(4)
el1 = driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword")
el1.send_keys("鬼畜")
driver.implicitly_wait(7)
time.sleep(4)
TouchAction(driver).tap(x=356, y=150).perform()
driver.implicitly_wait(7)
time.sleep(4)
TouchAction(driver).press(x=286, y=1195).move_to(x=250, y=534).release().perform()
driver.implicitly_wait(7)
time.sleep(2)
TouchAction(driver).tap(x=578, y=1131).perform()
driver.implicitly_wait(7)
time.sleep(4)

driver.quit()



