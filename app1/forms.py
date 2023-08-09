from django.forms import ModelForm
from .models import JobVacations

class JobForm(ModelForm):
    class Meta:
        model = JobVacations
        fields= ['name', 'salary','information']
class JobForm2(ModelForm):
    class Meta:
        model = JobVacations
        fields= ['name', 'salary','information','places']