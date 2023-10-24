fetch('https://shopee.co.id/api/v4/pdp/get_pc?shop_id=303267443&item_id=21084086017')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.text(); // You can also use response.json() for JSON data
  })
  .then(data => {
    console.log('Response data:', data);
  })
  .catch(error => console.error('An error occurred:', error));