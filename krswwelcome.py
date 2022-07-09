import requests
url ="http://inet-ip.info/"
response = requests.get(url)
print(response.text)


print ((response.text).find('Your IP Address is <strong>'))
print((response.text)[(response.text).find('Your IP Address is <strong>'):(response.text).find('</strong>.</p>')])
