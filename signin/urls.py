from django.urls import path
from .views import SigninView

urlpatterns = [
    path('', SigninView.as_view(), name='view_of_signin'),
]
