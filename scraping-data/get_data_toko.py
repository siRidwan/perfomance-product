from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Inisialisasi driver Selenium sesuai dengan peramban yang ingin Anda gunakan
option = webdriver.ChromeOptions()
option.add_argument("--headless")
driver = webdriver.Chrome()  # Ubah sesuai dengan peramban yang Anda gunakan
cookies = {
        "domain": ".shopee.co.id",
        "expiry": 1732673513,
        "httpOnly": True,
        "name": "SPC_EC",
        "path": "/",
        "sameSite": "Lax",
        "secure": True,
        "value": "cjBxMFltWDNTdWxCdzBTSyc2qAgIdfHP0E9dyiQ9F2pcOA6FKyKyam/1IP/kPlSE4LvPMcEUkREmsCRb1GYfOs2cdsraee9NejYgbyCdutElpBaF7EYU9iyBW7fJH7JTeY0XcUCWb3HZSBFfIqlj1mzxra4WmMIToC5OjQY2aBUZ2vSbL4gJ5lYGOJ5CRqy4"
    }
# Buka situs web yang ingin Anda kunjungi
driver.get('https://shopee.co.id/')
driver.add_cookie(json.loads(json.dumps(cookies)))
wait = WebDriverWait(driver, 60)
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='shopee-searchbar-input__input']")))
driver.get('https://shopee.co.id/')
# wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='shopee-searchbar-input__input']")))
sleep(5)


item_id = 23947956290
shopid  = 389631657
requestData = {
    "entry_point": "ShopByPDP",
    "rcmd_condition": {
       "item_id": item_id,
       "step2_upstream": "search",
       "upstream": "pdp"
    },
    "version": 3,
    "shopid": shopid
 }
 

request_body  = f"""
// Objek yang akan dikirim dalam tubuh permintaan (request body)
const requestData = {requestData};"""

requestOptions = """
// Konfigurasi permintaan
const requestOptions = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json', // Atur tipe konten menjadi JSON
  },
  body: JSON.stringify(requestData) // Mengubah objek menjadi string JSON
};

// Kirim permintaan POST
return fetch('https://shopee.co.id/api/v4/shop/get_shop_tab', requestOptions)
  .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.json();
    });
"""

script  = request_body + requestOptions

result = driver.execute_script(script)
print(json.dumps(result))

sleep(20)
driver.quit()