

# импортируем библиотеку
import requests
  
# api
URL = "https://reqres.in/api/users?page=2"

api = {"id","email","last_name"}
  
# выбираем поля для импорта
PARAMS = {'id','email':api}
  
# отправляем запрос get
r = requests.get(url = URL, params = PARAMS)
  
# экспортируем данные в json
data = r.json()

print (r.json)




