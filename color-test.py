from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 构建浏览器实例
driver = webdriver.Edge()
#driver = webdriver.Edge(executable_path='./msedgedriver.exe')
sign_in_url = "https://www.webhek.com/post/color-test/"
driver.get(sign_in_url)

time.sleep(3)

cover_button = driver.find_element(By.ID, 'overlay99')
print(cover_button)
cover_button.click()

start_button = driver.find_element(By.XPATH, '//*[@id="index"]/div[2]/button')
print(start_button)
start_button.click()

def get_unique(styledict):
    cnt_dict = dict()
    unique_style = ""
    for key in styledict:
        if styledict[key] not in cnt_dict:
            cnt_dict[styledict[key]] = 1
        else:
            cnt_dict[styledict[key]] += 1
    for key in cnt_dict:
        if cnt_dict[key] == 1:
            unique_style = key
            break
    for key in styledict:
        if styledict[key] == unique_style:
            return key

while(True):
    try:
        dict_style = dict()
        cnt = 0
        while(True):
            try:
                cnt += 1
                block = driver.find_element(By.XPATH, '//*[@id="box"]/span['+str(cnt)+']')
                dict_style[block] = block.get_attribute('style')
            except:
                break
        unique_tag = get_unique(dict_style)
        unique_tag.click()
    except:
        break

time.sleep(200)