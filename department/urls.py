from django.urls import path
from . import views

urlpatterns = [
    path('<str:asset_name>/departmentcreate',views.DepartmentCreate.as_view()),
]
