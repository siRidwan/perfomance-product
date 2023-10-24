from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Inisialisasi driver Selenium sesuai dengan peramban yang ingin Anda gunakan
# option = webdriver.ChromeOptions()
# option.add_argument("--headless")
# driver = webdriver.Chrome()  # Ubah sesuai dengan peramban yang Anda gunakan
# cookies = {
#         "domain": ".shopee.co.id",
#         "expiry": 1732673513,
#         "httpOnly": True,
#         "name": "SPC_EC",
#         "path": "/",
#         "sameSite": "Lax",
#         "secure": True,
#         "value": "cjBxMFltWDNTdWxCdzBTSyc2qAgIdfHP0E9dyiQ9F2pcOA6FKyKyam/1IP/kPlSE4LvPMcEUkREmsCRb1GYfOs2cdsraee9NejYgbyCdutElpBaF7EYU9iyBW7fJH7JTeY0XcUCWb3HZSBFfIqlj1mzxra4WmMIToC5OjQY2aBUZ2vSbL4gJ5lYGOJ5CRqy4"
#     }
# # Buka situs web yang ingin Anda kunjungi
# driver.get('https://shopee.co.id/')
# driver.add_cookie(json.loads(json.dumps(cookies)))
# wait = WebDriverWait(driver, 60)
# wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='shopee-searchbar-input__input']")))
# driver.get('https://shopee.co.id/')
# wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='shopee-searchbar-input__input']")))


# sleep(60)
# with open("C:/Users/INFINITY/EMBULAH/Shopee/scrap/sdf.json", "w") as w:
#     w.write(json.dumps(driver.get_cookies()))
# Eksekusi konsol JavaScript secara otomatis
def consoleProduct(shop_id,item_id):
    fetching = f"""
    return fetch('https://shopee.co.id/api/v4/pdp/get_pc?shop_id={shop_id}&item_id={item_id}')"""
    respon = """
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.json();
    });
    """
    script = fetching + respon
    result = driver.execute_script(script)
    return result

def consoleStore(shopid,item_id):
    # shopid  = 389631657
    # item_id = 23947956290
    requestData = {
    "entry_point": "ShopByPDP",
    "rcmd_condition": {
        # "cat_id": 100535,
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
    return result
shop_id = 389631657
item_id = 23947956290
# product_data    = consoleProduct(shop_id,item_id)
product_data    = json.load(open("scraping-data/product.json"))
# itemid  = item_id
for models in product_data['data']['item']['models']:
    model_id    = models['model_id']
    model_name  = models['name']
    model_normal_stock    = models['normal_stock']
    model_sold     = models['sold']
    model_price     = models['price']
title               = product_data['data']['item']['title']
ctime               = product_data['data']['item']['ctime']
global_sold         = product_data['data']['product_review']['global_sold']
total_rating_count  = product_data['data']['product_review']['total_rating_count']
liked_count         = product_data['data']['product_review']['liked_count']
rating_star         = product_data['data']['product_review']['rating_star']
image               = product_data['data']['product_images']['images'][0]
# store_data      = consoleStore(shop_id,item_id)['data']['decoration'][3]
store_data      = json.load(open("scraping-data/store.json"))['data']['decoration'][3]
for items in store_data['recommendations']['items']:
    if item_id == items['itemid']:
        sold            = items['sold']
print(f"""
shop_id = {shop_id}
item_id = {item_id}
model_id    = {model_id}
model_name  = {model_name}
model_normal_stock  = {model_normal_stock}
model_sold  = {model_sold}
model_price = {model_price}
title   = {title}
ctime   = {ctime}
global_sold = {global_sold}
total_rating_count  = {total_rating_count}
liked_count = {liked_count}
rating_star = {rating_star}
image   = {image}
sold    = {sold}
""")
# shopid

# with open("scraping-data/product.json", "w") as w:
#     w.write(json.dumps(consoleProduct(389631657,23947956290), indent=4))

# with open("scraping-data/store.json", "w") as w:
#     w.write(json.dumps(consoleStore(389631657,23947956290), indent=4))

# print(consoleStore(389631657,23947956290))
# print(consoleProduct(3722694,8433542870))
# Tutup peramban
# driver.quit()