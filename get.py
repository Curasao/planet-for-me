

# ����������� ����������
import requests
  
# api
URL = "https://reqres.in/api/users?page=2"

api = {"id","email","last_name"}
  
# �������� ���� ��� �������
PARAMS = {'id','email':api}
  
# ���������� ������ get
r = requests.get(url = URL, params = PARAMS)
  
# ������������ ������ � json
data = r.json()

print (r.json)




