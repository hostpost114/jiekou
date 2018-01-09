#coding=utf-8
import requests
s=requests.Session()
payload={'user': 'hostpost114@gmail.com', 'password': 'lixiang123456'}
response=requests.get('https://github.com/login',data=payload)
y=s.get('https://api.github.com/users/octocat/orgs',params=payload)
print(response.url)
print(response.status_code)
print(y.status_code,y.url,y.text)