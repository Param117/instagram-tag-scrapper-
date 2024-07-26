#tag scrapper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import os
import wget
import time

driver_path = 'PATH'                                      #input path here for the driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


username.clear()
username.send_keys("")                 # input username between brackets(paranthesis)
password.clear()
password.send_keys("")                 # input password between brackets(paranthesis)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)
css_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37"))
).click()

time.sleep(5)
css_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._ap36._a9_1"))
).click()



keyword = input()
driver.get("https://www.instagram.com/explore/tags/" + keyword + "/")
 
# Wait for 5 seconds
time.sleep(5)

div_button = WebDriverWait(driver, 2).until( EC.element_to_be_clickable((By.CSS_SELECTOR, "div._aagw"))).click()



def scrape_and_append_usernames():
    try:
       
        svg_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Next']"))
        )
        svg_button.click()
        print("Clicked 'Next' button")

        wait = WebDriverWait(driver, 10)
        usernames_elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/span/div/a")
            )
        )
        print("Usernames elements located")
        
        usernames = [username.text for username in usernames_elements]
        print('Number of scraped usernames:', len(usernames))

        path = r'path of saved file'                                    # specify path where you need to save your file
        file_path = os.path.join(path, 'usernames.txt')
        with open(file_path, 'a') as f:  # Open file in append mode
            for username in usernames:
                f.write(username + "\n")
        print(f"Usernames appended to {file_path}")

    except TimeoutException as e:
        print(f"TimeoutException: {e}")


number_of_iterations = 100000

for _ in range(number_of_iterations):
    scrape_and_append_usernames()
