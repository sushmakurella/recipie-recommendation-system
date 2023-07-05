from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    # path('adminlog',views.adminlog,name='adminlog'),
    # path('login',views.login_request,name='login'),
    # path('register',views.register_request,name='register'),
    # path('adlogout',views.adlogout,name='adlogout'),
    path('index',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('faculty_dashboard',views.faculty_dashboard,name='faculty_dashboard'),
    path('Dashboard',views.admin_dashboard,name='Dashboard'),
    path('lessonplans',views.lessonplans,name='lessonplans'),
]