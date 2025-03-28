from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_application", views.new_application, name="new_application"),
    path("application_sent/<str:pk>", views.application_sent, name="application_sent"),
    path("application_detail/<str:pk>", views.application_detail, name="application_detail"),
    path("application_detail_form/", views.application_detail_form, name="application_detail_form"),
    path("edit_application/<str:pk>", views.edit_application, name="edit_application"),
    path("delete_application/<str:pk>", views.delete_application, name="delete_application"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("admin_view", views.admin_view, name="admin_view"),
] 