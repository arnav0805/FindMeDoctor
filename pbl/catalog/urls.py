from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("enter_doctor/",views.DoctorCreate.as_view(),name="enter_doctor"),
    path("enter_patient/",views.PatientCreate.as_view(),name="enter_patient"),
    path("search/",views.enter_details ,name="enter_details")
    
    
]
