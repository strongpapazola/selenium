from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from os import system
import subprocess

def shell(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

def msg(title, text): # Windows Only
    shell("mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( '"+text+"', 10, '"+title+"', 64 );close()\"")

def aksesxpath(driver, xpath):
    try:
        wait = WebDriverWait(driver, 5)
        return wait.until(EC.visibility_of_element_located((By.XPATH, str(xpath))))
    except Exception as e:
        print(e)
        return False

def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=cookie")
        driver = webdriver.Chrome(executable_path="C:\\Users\\yourPath\\toChromeDriver\\chromedriver.exe", chrome_options=chrome_options)
        driver.get('https://github.com/strongpapapazola/selenium')            

        aksesxpath(driver, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/div/span/span[1]/span/span[1]').click()
        aksesxpath(driver, '/html/body/span/span/span[1]/input').clear()
        aksesxpath(driver, '/html/body/span/span/span[1]/input').send_keys("Insert Keys")
        while True:
            if aksesxpath(driver, '/html/body/span/span/span[2]/ul/li').text != 'Searching…': # Wait Loading
                aksesxpath(driver, '/html/body/span/span/span[2]/ul/li').click()
                break
            time.sleep(1)
    except:
        print('Gagal Login')
        input('[enter to login]')
        aksesxpath(driver, '/html/body/div[1]/div/div/form/div[1]/input').send_keys('sadmin@gmail.com')
        aksesxpath(driver, '/html/body/div[1]/div/div/form/div[2]/input').send_keys('p4pu4b4r4t')
        aksesxpath(driver, '/html/body/div[1]/div/div/form/div[3]/button').click()
        driver.close()

if '__main__' == __name__:
    print('Warning', 'Pastikan QUIS 6 BARIS!!')
    # while True:
    #     try:
    #         main()
    #     except Exception as e:
    #         print(e)
    main()
