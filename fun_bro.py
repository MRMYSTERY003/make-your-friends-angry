from selenium import webdriver as wb
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



path = 'user-data-dir=C:\\Users\\YOUR USER NAME\\App Data\\Local\\Google\\Chrome\\User Data\\automation' ## DONT FORGET TO ENTER THE USER NAME HERE
o = wb.ChromeOptions()
o.add_argument(path)
driver = wb.Chrome('C:\\Users\\kamat\\Desktop\\python projrcts\\pythonProject\\chromedriver.exe', options = o) ## ENTER THE PATH OF THE WEBDRIVER INSTALLED
driver.get('https://web.whatsapp.com')

print('----------'*5)
victom = input('enter the targer name : ')
try:
    search = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    search.clear()
    search.send_keys(victom)
    target = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, f'//span[@title = "{victom}"]')))
    target.click()
except:
    print('target name not found.... try again...')
    driver.close()
    exit()

message = input('\nenter the message you what to send: ') or 'hi'

def send(message):
    m_box = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')))
    m_box.clear()
    m_box.send_keys(message)
    send = wd(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')))
    send.click()

num = int(input('enter the number of times you want to send: ')) or 10
for i in range(num):
        send(message)
        print('.',end = '')

print('\nsuccessfully send .....')
