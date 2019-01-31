import urllib.request

response = urllib.request.urlopen('https://httpbin.org/get')
print(response.read().decode('utf-8'))
