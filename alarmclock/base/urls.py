from django.urls import path
from .views import SetAlarm, ConfirmAlarm

urlpatterns = [
    path('', SetAlarm.as_view(), name="time"),
    path('confirm_alarm', ConfirmAlarm.as_view(), name="confirm"),
]