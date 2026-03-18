from django import forms
from .models import Employee,Document

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        # fields=['empname','phone']
        # exclude=['empname','phone']

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields='__all__'
