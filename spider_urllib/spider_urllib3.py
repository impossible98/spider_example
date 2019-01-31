import urllib.request

response = urllib.request.urlopen('https://httpbin.org/get')
print(response.status)
print(response.getheaders())
