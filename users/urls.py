from django.urls import path

from .views import UpdateUser

urlpatterns = [
    path('<int:pk>/update/', UpdateUser.as_view(), name='update'),
]
