
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import doctor_model,patient_details
from django.views.generic import CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

def index(request):
    
    return render(request,"catalog/index.html")

class DoctorCreate(CreateView):
    model=doctor_model
    fields= '__all__'
class PatientCreate(CreateView):
    model=patient_details
    fields= '__all__'



def enter_details(request):
    if request.method == 'POST':
        isin = request.POST.get('location', '')
        practice=request.POST.get('type_of_doctor','')
        try:
            # Filter doctor_model instances with the provided ISIN
            banks_with_isin = doctor_model.objects.filter(Q(location=isin ) & Q(type_of_doctor=practice))
            for x in banks_with_isin:
                l1=[]
                l1.append(x.availability_times)
                l1.append(x.doctor_name)
            return render(request, 'catalog/show_values.html', {'show_val': l1})
        except doctor_model.DoesNotExist:
            error_message = "ISIN not found. Please enter a valid ISIN."
            return render(request, 'catalog/enter_details.html', {'error_message': error_message})
    return render(request, 'catalog/enter_details.html')