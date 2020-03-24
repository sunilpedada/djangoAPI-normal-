from django.shortcuts import render
from django.views.generic import View
from.utils import Crud_opration
import json
from.form import form_validations
from.models import EmployeesDetails
# Create your views here.
class OneEndPoint(View,Crud_opration):
    def post(self,request,*args,**kwargs):
        recevied_data=request.body
        value=self.Json_form_valid(recevied_data)# step1 json form valid or not
        if not value:
            msg={"msg":"not a valid form"}
            return self.httpResponse(msg,status=400)
        loads_data=json.loads(recevied_data)
        forms_data=form_validations(loads_data)
        if forms_data.is_valid():
            forms_data.save(commit=True)
            get_data=EmployeesDetails.objects.get(email=loads_data["email"])
            print("geeet",get_data)###geeet EmployeesDetails object (4)
            response=self.serializing([get_data,])
            return self.httpResponse(response,status=200)
        if forms_data.errors:
            msg=json.dumps(forms_data.errors)
            return self.httpResponse(msg,status=400)
    def get(self,request,*args,**kwargs):
        data_id=request.body
        value=self.Json_form_valid(data_id)
        if not value:
            msg={"msg":"not a valid form"}
            return self.httpResponse(msg,status=400)
        load_json=json.loads(data_id)
        get_id=load_json.get("id",None)
        if get_id is not None:
            try:
                get_data=EmployeesDetails.objects.get(id=get_id)
            except EmployeesDetails.DoesNotExist:
                msg="details not in db"
                return self.httpResponse(msg,status=400)
            response=self.serializing([get_data,])
            return self.httpResponse(response,status=200)
        fetach_all=EmployeesDetails.objects.all()
        response=self.serializing(fetach_all)
        return self.httpResponse(response,status=200)
    def put(self,request,*args,**kwargs):
        data_id=request.body
        value=self.Json_form_valid(data_id)
        if not value:
            msg={"msg":"not a valid form"}
            return self.httpResponse(msg,status=400)
        load_json=json.loads(data_id)
        get_id=load_json.get("id",None)
        print("ididid",get_id)
        if get_id is None:
                msg={"msg":"id is require"}
                return self.httpResponse(msg,status=404)
        try:
            emp_data=EmployeesDetails.objects.get(pk=get_id)
        except EmployeesDetails.DoesNotExist:
            msg={"msg":"does not  exist"}
            return self.httpResponse(msg,status=400)
        json_load=json.loads(request.body)
        print("emp_data",emp_data.ename)
        original_data={"ename":emp_data.ename,
                        "esalary":emp_data.esalary,
                        "eaddress":emp_data.eaddress}
        original_data.update(json_load)
        print("original data",original_data)
        form=form_validations(original_data,instance=emp_data)
        print("forms data",form)
        if form.is_valid():
            form.save(commit=True)
            qs=EmployeesDetails.objects.get(pk=get_id)
            json_data=self.serializing([qs,])
            return self.httpResponse(json_data,status=200)
        if form.errors:
            msg=json.dumps(form.errors)
            return self.httpResponse(msg,status=400)
    def delete(self,request,*args,**kwargs):
        ##to check python manage.py dumpdata testapp.EmployeesDetails --indent 4
        data_id=request.body
        value=self.Json_form_valid(data_id)
        if not value:
            msg={"msg":"not a valid form"}
            return self.httpResponse(msg,status=400)
        load_json=json.loads(data_id)
        get_id=load_json.get("id",None)
        print("ididid",get_id)
        if get_id is None:
                msg={"msg":"id is require"}
                return self.httpResponse(msg,status=404)
        db_data=EmployeesDetails.objects.get(id=get_id)
        if db_data is None:
            msg={"msg":"dose not exist"}
            return self.httpResponse(msg,status=400)
        status_code,msg=db_data.delete()
        if status_code==1:
            msg={"msg":"deleted successfuly"}
            return self.httpResponse(msg,status=200)
        msg={"msg":"some went wrong please try later"}
        return self.httpResponse(msg,status=400)

        