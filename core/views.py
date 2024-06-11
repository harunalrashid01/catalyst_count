from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import csv
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Company , CompanyBulkUpload

def main(request):

    if request.method=="POST":
        file=request.FILES["file"]
        File.object.create(file=file)






def is_admin(user):
    return user.is_staff



# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

@login_required
def querybuilder(request):
    return render(request, "querybuilder.html")


@user_passes_test(is_admin)
@login_required
def user(request):
    return render(request, "user.html")


def upload(request):
    return render(request, "upload.html")


# def upload_csv(request):
#     print("this is sis sadihnnnnnnnnnn")
#     if request.method == 'POST' and request.FILES['csv_file']:
#         csv_file = request.FILES['csv_file']
#         if not csv_file.name.endswith('.csv'):
#             return HttpResponse('Invalid file format. Please upload a CSV file.')
        
#         # Assuming your CSV file has a header
#         csv_data = csv.reader(csv_file)
#         next(csv_data)  # Skip the header row
        
#         for row in csv_data:
#             # Assuming your CSV has columns corresponding to your Company model fields
#             (
#                 name, domain, year_founded, industry, size_range,
#                 city, state, country, linkedin_url,
#                 current_employee_estimate, total_employee_estimate
#             ) = row
#             # Update your database here
#             Company.objects.update_or_create(
#                 name=name,
#                 defaults={
#                     'domain': domain,
#                     'year_founded': year_founded,
#                     'industry': industry,
#                     'size_range': size_range,
#                     'city': city,
#                     'state': state,
#                     'country': country,
#                     'linkedin_url': linkedin_url,
#                     'current_employee_estimate': current_employee_estimate,
#                     'total_employee_estimate': total_employee_estimate
#                 }
#             )
        
#         return HttpResponse('CSV file uploaded and data updated successfully.')
    
#     return render(request, 'upload_csv.html')
    
# def uploadcsv(request):
#   if request.method == 'GET':
#     form = CompanyBulkUploadForm()
#     return render(request, 'students/students_upload.html', {'form':form})

#   # If not GET method then proceed
#   try:
#     form = StudentBulkUploadForm(data=request.POST, files=request.FILES)
#     if form.is_valid():
#       csv_file = form.cleaned_data['csv_file']
#     if not csv_file.name.endswith('.csv'):
#       messages.error(request, 'File is not CSV type')
#       return redirect('students:student-upload')
#     # If file is too large
#     if csv_file.multiple_chunks():
#       messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
#       return redirect('students:student-upload')
    
#     file_data = csv_file.read().decode('utf-8')
#     lines = file_data.split('\n')

#     # loop over the lines and save them in db. If error, store as string and then display
#     for line in lines:
#       fields = line.split(',')
#       data_dict = {}
#       print(data_dict)
#       try:
#         form = StudentBulkUploadForm(data_dict)
#         if form.is_valid():
#           form.save()
#         else:
#           logging.getLogger('error_logger').error(form.errors.as_json())
#       except Exception as e:
#         logging.getLogger('error_logger').error(form.errors.as_json())
#         pass
#   except Exception as e:
#     logging.getLogger('error_logger').error('Unable to upload file. ' + repr(e))
#     messages.error(request, 'Unable to upload file. ' + repr(e))
#   return redirect('students:student-upload')
