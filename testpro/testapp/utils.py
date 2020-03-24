import json
from django.http import HttpResponse
from django.core.serializers import serialize
class Crud_opration(object):
    def Json_form_valid(self,data):
        try:
            json_load=json.loads(data)
            validation=True
        except ValueError:
            validation=False
        return validation
    def httpResponse(self,msg,status):
        dump_msg=json.dumps(msg)
        return HttpResponse(dump_msg,content_type="application/json",status=status)
    def serializing(self,querysets):
        serili_data=serialize("json",querysets,fields=("ename","email"))
        load_data=json.loads(serili_data)
        print(load_data)##[{'model': 'testapp.employeesdetails', 'pk': 4, 'fields': {'ename': 'kvi', 'email': 'k@mail.com'}}]
        record_form=[]
        for element in load_data:
            record_form.append(element["fields"])
            record_form.append(element["pk"])
        print("fields",record_form)##fields [{'ename': 'svi', 'email': 's@mail.com'}, 6]
        dump_data=record_form
        return dump_data