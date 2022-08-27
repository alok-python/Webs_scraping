import time , requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
import pytesseract
from PIL import Image

path='C:\Program Files\chromedriver.exe'
browser = webdriver.Chrome(path     )
browser.get('https://bidplus.gem.gov.in/advance-search')

# click on Search By Consignee Location
browser.find_element(By.LINK_TEXT, "Search by Consignee Location").click()
# Enter State Name in .send_key("State_Name")
browser.find_element(By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/select[1]").click()
time.sleep(3)
browser.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/select[1]/option[11]").click()

# Enter State Name in .send_key("City")
browser.find_element(By.ID, "city_name_con").send_keys("NEW DELHI")

# click on from date input box
browser.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]").click()
time.sleep(2)

# select the date
browser.find_element(By.XPATH, '/html[1]/body[1]/div[7]/table[1]/tbody[1]/tr[5]/td[4]/a[1]').click()

# click on to date input box
browser.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[3]/div[1]/input[1]").click()
time.sleep(2)

#Select Date
browser.find_element(By.XPATH, '/html[1]/body[1]/div[7]/table[1]/tbody[1]/tr[5]/td[2]/a[1]').click()
time.sleep(1)


#select captcha image By element 
images = browser.find_element(By.CSS_SELECTOR, "#tab2 > div > form > div:nth-child(3) > div.col-md-5 > span > img").get_attribute("src")
im = Image.open(requests.get(images, stream=True).raw)
ki=pytesseract.get_tesseract_version()

# Paste the path of tessract-ocr path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd =pytesseract.pytesseract.tesseract_cmd

# Extract text from image
text = pytesseract.image_to_string(im)

# After extracting text from image sent the text value in Captcha text boxt
browser.find_element(By.CSS_SELECTOR,"div[id='tab2'] input[placeholder='Enter captcha here']").send_keys(text)

time.sleep(20)
