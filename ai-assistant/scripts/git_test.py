import requests

url = "https://api.github.com/repos/aokicreativeoffice/AokiCreativeOfficeGTD/contents"

r = requests.get(url)

print(r.json())