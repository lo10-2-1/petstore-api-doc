import requests

request_url = "https://petstore.swagger.io/v2/pet/findByStatus"
params = {"status": "available"}

find_pets_by_status = requests.get(request_url, params=params)

pets_array = find_pets_by_status.json()
pets_array = pets_array[:9]

pets_names_ids = ''

for item in pets_array:
    pets_names_ids += (str(item.get('id')) + ' ' + item.get('name') + '\n')

print(pets_names_ids)