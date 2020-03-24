from django import forms
from.models import EmployeesDetails
class form_validations(forms.ModelForm):
    class Meta:
        model=EmployeesDetails
        fields="__all__"