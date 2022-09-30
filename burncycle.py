# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import yaml
import time

# Loads login details from YAML file
conf = yaml.full_load(open("login_details.yml"))
my_burn_email = conf["user"]["email"]
my_burn_password = conf["user"]["password"]

# Set up Chrome Driver
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://www.burn-cycle.com/my-account/pearl-district")

# Pause for page to load
time.sleep(5)

# switch to selected frame
iframe = driver.find_element(By.XPATH, "//*[@id='sf-frame']")
driver.switch_to.frame(iframe)

# Populate username and password info and click
username = driver.find_element(By.XPATH, "//input[@data-val-required='Username is required']")
username.send_keys(my_burn_email)

pw = driver.find_element(By.XPATH, "//*[@id='PASSWORD']")
pw.send_keys(my_burn_password)
login_button = driver.find_element(By.XPATH, "//*[@id='liFormWrap']/form[1]/button").click()

# Pause for page to load
time.sleep(5)

# Navigate to signup page
book_class_button = driver.find_element(By.XPATH, "//*[@id='wphReserve']").click()

# Signup for bike 8 on Monday
#monday_bike_8 = driver.find_element(By.XPATH, "//*[@id="classId_70446340"]/div[3]/a/div")
#//*[@id="classId_70828000"]/div[3]/div

# Signup for bike 8 on Tuesday


# Defines login function
#def login(url, usernameID, username, passwordId, password, submit_buttonId):
    #driver.get(url)
    #driver.find_element(By.ID, usernameID).send_keys(username)
    #driver.find_element(By.ID, passwordId).send_keys(password)
    #driver.find_element(By.ID, submit_buttonId).click()