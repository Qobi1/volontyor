from django.urls import path
from .views import *

urlpatterns = [
    path('events/', EventAPIView.as_view(), name='Event-all'),
    path('event/<int:pk>/', EventAPIView.as_view(), name='Event-one'),
    path('volonteers/', VolunteerAPIView.as_view(), name='Volunteer-one'),
    path('volonteer/<int:pk>/', VolunteerAPIView.as_view(), name='Volunteer-all'),
    path('investors/', InvestorAPIView.as_view(), name='Investor-one'),
    path('investor/<int:pk>/', InvestorAPIView.as_view(), name='Investor-all'),
    path('news/', NewsAPIView.as_view(), name='News-one'),
    path('news/<int:pk>/', NewsAPIView.as_view(), name='News-all'),
]