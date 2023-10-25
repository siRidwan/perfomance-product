// Objek yang akan dikirim dalam tubuh permintaan (request body)
const requestData = {
  "entry_point": "ShopByPDP",
  "rcmd_condition": {
     "cat_id": 100535,
     "item_id": 23419209268,
     "step2_upstream": "search",
     "upstream": "pdp"
  },
  "version": 3,
  "shopid": 783124108
};

// Konfigurasi permintaan
const requestOptions = {
method: 'POST',
headers: {
  'Content-Type': 'application/json', // Atur tipe konten menjadi JSON
},
body: JSON.stringify(requestData) // Mengubah objek menjadi string JSON
};

// Kirim permintaan POST
fetch('https://shopee.co.id/api/v4/shop/get_shop_tab', requestOptions)
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.text();
})
.then(data => {
  console.log('Response data:', data);
})
.catch(error => console.error('An error occurred:', error));