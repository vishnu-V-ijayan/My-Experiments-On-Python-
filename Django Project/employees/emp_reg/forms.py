from django import forms
from .models import emp


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=emp
        fields=('fullname','mobile','empcode','position')
        labels={
            'fullname':'Full Name',
            'empcode':'Emp code',


        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['empcode'].required=False
