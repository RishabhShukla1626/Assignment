from django.urls import path
from . import views
app_name='debates'

urlpatterns = [
    path("debates/", views.debates, name="debates"),
    path("argue/<str:pk>/", views.add_arguement, name="argue"),
    # path("project/<str:pk>/", views, name="project"),
    # path("create-project", views, name="create-project"),
    # path("update-project/<str:pk>/", views, name="update-project"),
    # path("delete-project/<str:pk>/", views, name="delete-project"),
]