import requests

response= 0

#while response != 200:
response= requests.get("https://www.amazon.it/dp/B0CXJ9XSVZ/ref=twister_B0D2DVFZ3H?_encoding=UTF8&psc=1")

print(response)


#if response == 200:
for x in response:
    print(f"{x}\n")
