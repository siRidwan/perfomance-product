import requests

url = 'https://shopee.co.id/api/v4/pdp/get_pc?shop_id=303267443&item_id=21084086017'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '_ga_SW6D8G0HXK=deleted; SC_SSO_U=1479579; SC_DFP=jsLjXnJVhzkSjuyjFrfJGhSAKOwJOBQN; ...',  # Masukkan cookie Anda di sini
    'Referer': 'https://shopee.co.id/',
    'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'X-Sap-Ri': '511f3765f0f7fe26dc0ca33c01018761ee601f8d9db81149ee8d',
    'X-Sap-Sec': 'e5jI0quGz5pCl5pCmApfl52CmApCl52Cl5pwl5pCR5HClrwGl5pxl5pCdsf5pzuCl5pQlRpCZ5HClOd3WvkogpjX1y/yiaqJos0oYg2oMRQdevAVwp7QCTWfBVQZgGjEXGl8TEaP47chcEFZnEEidYsiXa0oQ2Mp7uwgdYjUlCEpi933bGhM+K1YXdI9giypbaNtypXlcJ7VAxR/2AajyfT6pt3DL4kL+DuMyzQheDNBA1TTpff0zAXymr949cC3Cjenu877ijyAbRNcoQc7HpgOnSbvtoLkqP2Xd3P6W1qlMZjwFMJ+ZwcaNYy/kS/mytKL6dqpQvq7CRrxCBRYiTfjY+Nru3DhA/LlfuDxD+IO4FdaPw+Xv6qoZGs/FJOrLTCsKMryxVOIyZB2toFnVVNatwBViHW3jME7YuTbta51o93f+apEOtFUJeR5/y7mERCys4ld5+DjxuSuQ6rfl5pCvlReGgrhGlrCl5pC5sl5pzuCl5pDl5pCg5pClSBk1A3gp62Pb66E7lT+yT/P5WjXy5pClIREvg73vg7/l5pCl5uCz5pfl52Cy5pCl5uCl5pDl5pCg5pClsy/cnvzZGv0saBCKHA8QSXG0bJgy5pClIrPUD70UMrpl5pCls=='
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes

    data = response.text  # You can also use response.json() for JSON data
    print('Response data:', data)

except requests.exceptions.RequestException as error:
    print('An error occurred:', error)
