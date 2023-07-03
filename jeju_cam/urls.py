from django.urls import path

from jeju_cam.views import UserView

app_name = "jeju_cam"

urlpatterns = [
    path("user/", UserView.as_view(), name="user_list_create"),
    path("user/<int:pk>/", UserView.as_view(), name="user_detail_update_delete"),
]
