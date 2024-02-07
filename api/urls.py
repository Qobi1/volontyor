from django.urls import path
from .views import *

urlpatterns = [
    path('tadbirlar/', EventAPIView.as_view(), name='Event-all'),
    path('tadbirlar/<str:slug>/', EventAPIView.as_view(), name='Event-one'),
    path('volontyor/', VolunteerAPIView.as_view(), name='Volunteer-one'),
    path('volontyor/<str:slug>/', VolunteerAPIView.as_view(), name='Volunteer-all'),
    path('investor/', InvestorAPIView.as_view(), name='Investor-one'),
    path('investor/<str:slug>/', InvestorAPIView.as_view(), name='Investor-all'),
    path('news/', NewsAPIView.as_view(), name='News-one'),
    path('news/<str:slug>/', NewsAPIView.as_view(), name='News-all'),
]