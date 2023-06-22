from django.urls import path
from .views import UserList, UserDetail, RegistrationView, LoginView


urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
