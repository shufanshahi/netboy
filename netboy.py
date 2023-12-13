#you might need to Install the module selenius . just go to the terminal and write : pip install selenium
#download the cromedriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("chromedriver_path") #change_this_to your chromedriver_path

def get_driver(theLink):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(theLink)
    return driver

def get_time():
    lowest_use = 100000
    index = 0
    driver = get_driver("http://10.220.20.12/index.php/home/login")
    user = ["user_id1", "user_id2", "user_id3", "user_id4"] #change_this_to_user_id
    passW = ["user_id1_password", "user_id2_password", "user_id3_password", "user_id4_password"] #change_this_to_password
    for i in range(4):
        driver.find_element(by="id", value="username").send_keys(user[i])
        driver.find_element(by="id", value="password").send_keys(passW[i] + Keys.RETURN)
        time.sleep(2)
        element = driver.find_element(by="xpath", value='//*[@id="updates"]/div[1]/table/tbody/tr[6]/td[2]')
        print(user[i]+":")
        print(element.text)
        lowest_use = min(lowest_use,int(element.text.split(" ")[0]))
        if lowest_use == int(element.text.split(" ")[0]):
            index = i
        driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/ul/li[4]/a/span").click()
    return index


def change_wifi(lowest_user_id, lowest_user_pass):
    driver = get_driver("http://tplinkwifi.net")
    driver.find_element(by="id", value="pcPassword").send_keys("admin_password"+Keys.RETURN) #change_this_to_admin_password

    time.sleep(3)
    driver.switch_to.frame("frame1")
    driver.find_element(by="id", value="menu_network").click()
    driver.switch_to.default_content()
    driver.switch_to.frame("frame2")

    time.sleep(2)



    element = driver.find_element(by="id", value="username")
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys(lowest_user_id)

    element = driver.find_element(by="id", value="pwd")
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys(lowest_user_pass)

    element = driver.find_element(by="id", value="pwd2")
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys(lowest_user_pass)

    driver.find_element(by="id", value="saveBtn").click()


    time.sleep(5)


def main():
    user = ["user_id1", "user_id2", "user_id3", "user_id4"] #change_this_to_user_id
    passW = ["user_id1_password", "user_id2_password", "user_id3_password", "user_id4_password"] #change_this_to_password
    index = get_time()
    change_wifi(user[index], passW[index])

main()



