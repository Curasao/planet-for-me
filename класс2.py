import requests
res = {'id':'6','email':'test@request.com','first_name':'Olga','last_name':'Ivanova','avatar':'https://reqres.in/img/faces/2-image.jpg'}
r = requests.post('https://httpbin.org/post',data = res)
print(r.text)




