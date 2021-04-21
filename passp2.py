import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/196eec2f-937b-4333-bc8c-5ef690100246/LabelFile/'

data = {'file': open('5p.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('pgg8OqOMl7r_IAnj_JBlXRuLzX89nMRE', ''), files=data)

print(response.text)