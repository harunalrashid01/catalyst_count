# forms.py
from django import forms

class CompanyBulkUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')
