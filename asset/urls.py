from django.urls import path
from . import views

urlpatterns = [
    path('assetcreate',views.AssetCreate.as_view()),
]
