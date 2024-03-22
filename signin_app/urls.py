from django.urls import path
from signin_app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.render_home,name="render_home"),
    path("render_signin", views.render_signin ,name="render_signin"),
    path("ino", views.ino ,name="ino"),
    path("about", views.about ,name="about"),
    path("contact", views.contact ,name="contact"),
    path("index", views.index ,name="index"),
    path("login_page",views.login_page, name="login_page"),
    path("signin_page",views.signin_page, name="signin_page"),
    path("perform_login",views.perform_login, name="perform_login"),
    path("admin_dashboard/",views.admin_dashboard, name="admin_dashboard"),
    path("perform_logout",views.perform_logout, name="perform_logout"),
    path("reset_password/", auth_views.PasswordResetView.as_view(),name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(),name="password_rest_confirm "),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("reset",views.reset,name="reset"),
    path("perform_reset",views.perform_reset,name="perform_reset"),
]