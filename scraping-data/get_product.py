import sys
sys.path.append("C:/Users/INFINITY/EMBULAH/database/")
import database
from selenium import webdriver
import json
import requests
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def postCompetitors(itemid, shopid, image, title, ctime, normal_stock, global_sold, sold, price, total_rating_count, liked_count, rating_star, model_id, model_name, model_normal_stock, model_sold, model_price, model_image, username, location, store_name):
    url = "https://commercial.bisbas.id/api/v1.0/mp_abc_class/competitor_analysis/post_competitor_data.php"
    payload = json.dumps({
    "itemid": itemid,
    "shopid": shopid,
    "image": image,
    "title": title,
    "ctime": ctime,
    "normal_stock": normal_stock,
    "global_sold": global_sold,
    "sold": sold,
    "price": price,
    "total_rating_count": total_rating_count,
    "liked_count": liked_count,
    "rating_star": rating_star,
    "model_id": model_id,
    "model_name": model_name,
    "model_normal_stock": model_normal_stock,
    "model_sold": model_sold,
    "model_price": model_price,
    "model_image": model_image,
    "username": username,
    "location": location,
    "store_name": store_name
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        print(response.text)
        'sd'
    else:
        price("eror api post")

def get_data():
    url = "https://commercial.bisbas.id/api/v1.0/mp_abc_class/competitor_analysis/get_competitor_data.php"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()


# competitors_data    = database.query("SELECT `ids`, `sku`, `url`, `itemId`, `shopId`, `created_at`, `updated_at` FROM `competitors_data`")

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
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='shopee-searchbar-input__input']")))


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
asd = []
datas = get_data()

for competitors in get_data():
    print(competitors)
    # shop_id = 389631657
    # item_id = 23947956290
    ids         = competitors['ids']
    sku         = competitors['sku']
    url         = competitors['url']
    item_id     = competitors['itemId']
    shop_id     = competitors['shopId']
    warehouse_id= competitors['warehouse_id']
    product_data    = consoleProduct(shop_id,item_id)
    # product_data    = json.load(open("scraping-data/product.json"))
    # itemid  = item_id
    title               = product_data['data']['item']['title']
    ctime               = product_data['data']['item']['ctime']
    date_time           = datetime.fromtimestamp(ctime).strftime("%Y-%m-%d")
    global_sold         = product_data['data']['product_review']['global_sold']
    total_rating_count  = product_data['data']['product_review']['total_rating_count']
    liked_count         = product_data['data']['product_review']['liked_count']
    rating_star         = float(product_data['data']['product_review']['rating_star'])
    image               = product_data['data']['product_images']['images'][0]
    normal_stock        = product_data['data']['item']['normal_stock']
    price               = product_data['data']['item']['price']
    with open("scraping-data/product.json", "w") as w:
        w.write(json.dumps(consoleProduct(shop_id,item_id), indent=4))

    with open("scraping-data/store.json", "w") as w:
        w.write(json.dumps(consoleStore(shop_id,item_id), indent=4))
    place               = product_data['data']['shop_detailed']['place']
    username            = product_data['data']['shop_detailed']['account']['username']
    store_name          = product_data['data']['shop_detailed']['name']
    decoration          = consoleStore(shop_id,item_id)['data']['decoration']
    # decoration          = json.load(open("scraping-data/store.json"))['data']['decoration']
    for recomend in decoration:
        if int(recomend['type']) == 15:
            recommendations = recomend['recommendations']
            break
    for items in recommendations['items']:
        if item_id == items['itemid']:
            sold            = items['sold']
    for models in product_data['data']['item']['models']:
        model_id        = models['model_id']
        model_name      = models['name']
        model_normal_stock    = models['normal_stock']
        model_sold      = models['sold']
        model_price     = int(float(int(models['price'])/100000))
        model_image     = ''
        postCompetitors(item_id, shop_id, image, title, date_time, normal_stock, global_sold, sold, price, total_rating_count, liked_count, rating_star, model_id, model_name, model_normal_stock, model_sold, model_price, model_image, username, place, store_name)
        # asd.append({
        #     "itemid"   : item_id,
        #     "shopid"   : shop_id,
        #     "image" : image,
        #     "title" : title,
        #     "ctime" : date_time,
        #     "normal_stock"  : normal_stock,
        #     "global_sold"   : global_sold,
        #     "sold"  : sold,
        #     "price" : price,
        #     "total_rating_count"    : total_rating_count,
        #     "liked_count"   : liked_count,
        #     "rating_star"   : rating_star,
        #     "model_id"  : model_id,
        #     "model_name"    : model_name,
        #     "model_normal_stock"    : model_normal_stock,
        #     "model_sold"    : model_sold,
        #     "model_price"   : model_price,
        #     "model_image"   : model_image,
        #     "username"  : username,
        #     "location" : place,
        #     "store_name"    : store_name
        #     })
# shopid
# with open("scraping-data/datas.json", "w") as w:
#     w.write(json.dumps(asd, indent=4))

# print(consoleStore(389631657,23947956290))
# print(consoleProduct(3722694,8433542870))
# Tutup peramban
driver.quit()