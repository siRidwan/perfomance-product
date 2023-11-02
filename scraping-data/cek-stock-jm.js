function getCsrfToken(callback) {
  var url_sku = "https://www.jakmall.com/";

  $.ajax({
    url: url_sku,
    type: "GET",
    headers: {
      'Host'              : 'www.jakmall.com',
      'Connection'        : 'keep-alive',
      'sec-ch-ua'         : '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      'sec-ch-ua-mobile'  : '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
      'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Sec-Fetch-Site'    : 'same-origin',
      'Sec-Fetch-Mode'    : 'navigate',
      'Sec-Fetch-User'    : '?1',
      'Sec-Fetch-Dest'    : 'document',
      'Referer'           : 'https://www.jakmall.com/abc-store/taffware-humi-air-humidifier-ultrasonic-wood-grain-300ml-k-h98',
      'Accept-Encoding'   : 'gzip, deflate, br',
      'Accept-Language'   : 'id,id-ID;q=0.9,en;q=0.8',
      'X-Requested-With': 'XMLHttpRequest' // Tambahkan header ini
    },
    success: function (data) {
      var csrfToken = document.querySelector('meta[id="_token"]').getAttribute('content');
      callback(csrfToken); // Panggil callback dengan csrfToken
    },
    error: function (xhr, status, error) {
      // Tangani kesalahan jika ada
      console.log("Error: " + error);
      callback(null); // Panggil callback dengan null jika terjadi kesalahan
    }
  });
}

getCsrfToken(function(csrfToken) {
  if (csrfToken) {
    console.log("CSRF Token:", csrfToken);
    var sku = "1917816241778";
    var url_sku = "https://www.jakmall.com/search?q=" + sku;

    $.ajax({
      url: url_sku,
      type: "GET",
      headers: {
        'Host'              : 'www.jakmall.com',
        'Connection'        : 'keep-alive',
        'sec-ch-ua'         : '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile'  : '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site'    : 'same-origin',
        'Sec-Fetch-Mode'    : 'navigate',
        'Sec-Fetch-User'    : '?1',
        'Sec-Fetch-Dest'    : 'document',
        'Referer'           : 'https://www.jakmall.com/abc-store/taffware-humi-air-humidifier-ultrasonic-wood-grain-300ml-k-h98',
        'Accept-Encoding'   : 'gzip, deflate, br',
        'Accept-Language'   : 'id,id-ID;q=0.9,en;q=0.8',
        'X-Requested-With': 'XMLHttpRequest' // Tambahkan header ini
      },
      success: function (data) {
        // Lakukan parsing teks JSON menjadi objek JavaScript
        var products = data.products;
        var product_code, product_sku;
        
        products[0].sku.forEach(product => {
          if (product.code === sku){
              product_code = product.code; // Assign nilai ke variabel
              product_sku = product.sku; // Assign nilai ke variabel
          }
        });

        // Sekarang Anda dapat mengakses product_code dan product_sku di sini
        console.log(product_code);
        console.log(product_sku);

        var url_clean = "https://www.jakmall.com/cart/items";
        var headers = {
            'Host'              : 'www.jakmall.com',
            'Connection'        : 'keep-alive',
            'sec-ch-ua'         : '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile'  : '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site'    : 'same-origin',
            'Sec-Fetch-Mode'    : 'navigate',
            'Sec-Fetch-User'    : '?1',
            'Sec-Fetch-Dest'    : 'document',
            'Referer'           : 'https://www.jakmall.com/abc-store/taffware-humi-air-humidifier-ultrasonic-wood-grain-300ml-k-h98',
            'Accept-Encoding'   : 'gzip, deflate, br',
            'Accept-Language'   : 'id,id-ID;q=0.9,en;q=0.8',
            'X-Csrf-Token': csrfToken,
            'X-Requested-With': 'XMLHttpRequest' // Tambahkan header ini
        };
        var payload_clean = JSON.stringify({ "sku_codes": [product_code] });

        $.ajax({
          url: url_clean,
          type: "POST",
          contentType: "application/json",
          headers: headers,
          contentType: "application/json; charset=utf-8",
          data: payload_clean,
          success: function (data) {
            // Tangani respons sukses di sini
            console.log(data);
          },
          error: function (xhr, status, error) {
            // Tangani kesalahan jika ada
            console.log("Error: " + error);
          }
        });
      },
      error: function (xhr, status, error) {
        // Tangani kesalahan jika ada
        console.log("Error: " + error);
      }
    });
  } else {
    console.log("Gagal mendapatkan CSRF Token.");
  }
});

