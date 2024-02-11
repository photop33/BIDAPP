from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver_path = 'https://github.com/photop33/BIDAPP/chromedriver.exe'  # Change this to the actual path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={chromedriver_path}")
driver = webdriver.Chrome(options=chrome_options)
username=''
password=''
XX=''
print ("Test")
driver.get("https://digital.isracard.co.il/personalarea/Login/?returnUrl=http://digital.isracard.co.il/personalarea/dashboard/")
driver.find_element("xpath", '//*[@id="flip"]').click()
driver.find_element("xpath", '//*[@id="otpLoginId_ID"]').send_keys(username)
driver.find_element("xpath", '//*[@id="cardnum"]').send_keys(password)
driver.find_element("xpath", '//*[@id="otpLoginPwd"]').send_keys(XX)
driver.find_element("xpath", '//*[@id="otpLobbyFormPassword"]/button/span[2]').click()
time.sleep(15)
driver.find_element("xpath", '/html/body/div[1]/div[1]/div[3]/div[2]/section/div[3]/div/div/div/div[2]/section[1]/div[2]/div[1]/div[1]/div/div[3]/div/div/p/a/span[2]').click()
time.sleep(10)
driver.find_element("xpath", '//*[@id="wholePageExport"]/div[5]/div/div/div/div[1]/div[1]/button[1]/img').click()
time.sleep(5)
current_url = driver.current_url

