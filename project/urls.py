from django.urls import path
from . import views

urlpatterns = [
    path('<str:department_name>/projectcreate',views.ProjectCreate.as_view()),
    path('<int:project_id>/archive/create',views.ArchiveCreate.as_view()),
    path('archive/replicate',views.ArchiveReplicate.as_view()),
]
