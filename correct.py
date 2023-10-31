import requests, json


url = "https://api.thecatapi.com/v1/images/search"
apikey = "live_zhI0ury2bg3t3tkvE78K0VjZT1Dv5yV4rLxbMAmbTgAIjX02lPdK9QEhefrsvAR"
def getPics(auth):
   
    response = requests.get(url = f"{url}?api_key={auth}")
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return json_data
    else:
        return f"error, returned code {response.status_code}"


result = getPics(apikey)

#show me the resulting picture
# print(result)
#looks like this 

# [
#     {
#         'id': 'c2j',
#         'url': 'https://cdn2.thecatapi.com/images/c2j.jpg',
#         'width': 680, 'height': 453
#     }
# ]
iter = 25
def storePics(func, iterations):
    album = []


    for _ in range(iterations):

        result = func(apikey)
        album.extend([x['url'] for x in result])

    return json.dumps(album)

print (storePics(getPics, iter))
