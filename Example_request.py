import requests
import webbrowser

# param = {"wd": "网络爬虫"}
# r = requests.get('https://www.baidu.com/s?', params=param)
# print(r.url)
# webbrowser.open(r.url)
#
# data = {'firstname': 'Fanjie', 'lastname': 'Kong'}
# r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
# print(r.text)

# file = {'uploadFile': open('C:/Users/Dell/Pictures/Screenshots/20111111114.jpg', 'rb')}
# r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
# print(r.text)

# payload = {'username': 'kfj', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
# r2 = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r2.text)

session = requests.session()
payload = {'username': 'kfj', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)