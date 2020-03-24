import json
import requests
def post():
    dict_data={"ename":"loo","email":"p@mail.com","eaddress":"ppm","ephone_number":123456,
    "esalary":50}
    dump_data=json.dumps(dict_data)
    response=requests.post("http://127.0.0.1:8000/register/singleurl/",data=dump_data)
    print(response.status_code)
    print(response.json())
def getWith_id_or_none(id=None):
    data={}
    if id is not None:
        data={"id":id}
    response=requests.get("http://127.0.0.1:8000/register/singleurl/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
def put(id):
    data={"id":id,"ename":"ravi","email":"h@hg.com","eaddress":"tyj","ephone_number":123456}
    jason_dump=json.dumps(data)
    response=requests.put("http://127.0.0.1:8000/register/singleurl/",data=jason_dump)
    print(response.json())
    print(response.status_code) 
def delete(id):
    data={"id":id}
    response=requests.delete("http://127.0.0.1:8000/register/singleurl/",data=json.dumps(data))
    print(response.json())
    print(response.status_code)
delete(1)