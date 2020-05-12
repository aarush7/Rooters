from django.urls import path
from user_roles.viewsgroup.AttendantView import AttendantView,AttendantupdateView
from user_roles.viewsgroup.OperatorView import OperatorView,OperatorupdateView
from user_roles.viewsgroup.DriverView import DriverView,DriverupdateView
urlpatterns=[
    path('user_roles/attendant/',AttendantView.as_view()),
    path('user_roles/attendant/<uuid:pk>', AttendantupdateView.as_view()),
    path('user_roles/operator/',OperatorView.as_view()),
    path('user_roles/operator/<uuid:pk>', OperatorupdateView.as_view()),
    path('user_roles/driver/',DriverView.as_view()),
    path('user_roles/driver/<uuid:pk>', DriverupdateView.as_view()),
    
]