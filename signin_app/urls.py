from django.urls import path
from signin_app import views
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
    

    
]