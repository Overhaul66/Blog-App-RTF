from django.urls import path
from .views import test, index

urlpatterns = [
    path("", index, name="index"),
    path("testing", test, name='testing'),
]