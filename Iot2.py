import requests
import json
url = "http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22" 
 
r=requests.get(url)

text=r.text
print(text)
out_file=open ("file.json","w")
json.dump(text,out_file)
out_file.close()

