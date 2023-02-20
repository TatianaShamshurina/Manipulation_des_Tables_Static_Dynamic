# Manipulation de Iframes
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(3)
driver.switch_to.frame("packageListFrame")                                  #rentrer dans la frame 1
time.sleep(2)
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()             #cliquer sur le lien
time.sleep(3)
driver.switch_to.default_content()                                          #retourner dans default-content
time.sleep(3)

driver.switch_to.frame("packageFrame")                                      #zaxodim vo vtoruyu frame
time.sleep(3)
driver.find_element(By.LINK_TEXT,"WebDriver").click()                       #klikaem na Webdriver
driver.switch_to.default_content()                                          #vyxodim
time.sleep(3)

driver.switch_to.frame("classFrame")                                                            #zaxodim v 3 frame
driver.find_element(By.XPATH," //div[@class='topNav']//a[normalize-space()='Help']").click()        #click HELP
time.sleep(3)
driver.switch_to.default_content()                                                              #vyxodim
time.sleep(3)
driver.close()