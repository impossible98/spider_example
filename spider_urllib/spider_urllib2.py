import urllib.request

response = urllib.request.urlopen('https://httpbin.org/get')
print(type(response))
