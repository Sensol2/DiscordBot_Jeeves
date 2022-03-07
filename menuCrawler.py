import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys                     #send_key에 필요
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             #웹드라이버 딜레이
from selenium.webdriver.support import expected_conditions as EC    #예외처리
from selenium.common.exceptions import TimeoutException      

def WaitForClass_CanBeClicked(driver, delaySec, class_name):
    wait = WebDriverWait(driver, delaySec)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))

def WaitForClass_Visible(driver, delaySec, class_name):
    wait = WebDriverWait(driver, delaySec)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
    
def WaitForID_Visible(driver, delaySec, id_name):
    wait = WebDriverWait(driver, delaySec)
    wait.until(EC.visibility_of_element_located((By.ID, id_name)))

def WaitForTag_Visible(driver, delaySec, tag_name):
    wait = WebDriverWait(driver, delaySec)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, tag_name)))

def GetDodamMenu(driver):
    driver.get('http://m.soongguri.com/')
    WaitForClass_Visible(driver, 10, 'ui-select')
    time.sleep(1)
    driver.execute_script("useMenu(2,'');")
    WaitForClass_Visible(driver, 10, 'menu_list')
    menuText = driver.find_element_by_class_name('menu_list').text
    return menuText

def mainFunc(option = 1):
    # =====드라이버 및 옵션 생성=====
    options = webdriver.ChromeOptions()

    # 필요없고 해결방법도 없는 에러로그들 제거 옵션 추가
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    #Alert 팝업 없애는 옵션 추가 (로그인 실패 대응)
    options.add_argument("--disable-popup-blocking")

    # # 창 숨기는 옵션 추가
    options.add_argument("headless")

    # 드라이버 로드
    try:
        driver = webdriver.Chrome('.\CoreFiles\chromedriver\chromedriver.exe', options=options)
        driver.set_window_size(1920, 1080)
    except:
        print("! 크롬 드라이버 로드 실패. 크롬 버전과 호환되는 크롬드라이버가 설치되어 있는지, chromedriver.exe가 폴더 내에 있는지 확인해주세요.")
        return

    if option == 1:
        return GetDodamMenu(driver)
    driver.quit()