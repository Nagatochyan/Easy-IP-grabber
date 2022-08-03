import requests
url ="http://inet-ip.info/"
response = requests.get(url)
print(response.text)



#use discord webhook and send ip to your server
print((response.text)[(response.text).find('Your IP Address is <strong>'):(response.text).find('</strong>.</p>')])
