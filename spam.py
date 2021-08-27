from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

message = str(input('Masukkan message anda: '))
id_channel = input('Masukkan ID Channel: ')
jumlahLoop = int(input('Masukkan jumlah spam: '))

browser = webdriver.Chrome(executable_path='YOUR_CHROME_DRIVER_PATH')
browser.get("https://discord.com/app")

print("[]Waiting channel room")

chat = WebDriverWait(browser, timeout=999999999).until(lambda d: d.find_element_by_xpath(f'//div[@aria-label="Message #{id_channel}"]'))
for x in range(jumlahLoop):
    chat.send_keys(message)
    chat.send_keys(Keys.ENTER)

print(f'{jumlahLoop} berhasil terkirim')