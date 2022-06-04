from django.db.models import fields
from django.forms import ModelForm
from .models import Student


class UpDateInfo(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
