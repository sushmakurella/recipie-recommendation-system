from django.urls import path
from . import views,lessonplan

urlpatterns = [
    path('',views.home,name='home'),
    # path('adminlog',views.adminlog,name='adminlog'),
    # path('login',views.login_request,name='login'),
    # path('register',views.register_request,name='register'),
    # path('adlogout',views.adlogout,name='adlogout'),
    path('index',views.index,name='index'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('add_regulation',views.add_regulation,name='add_regulation'),
    path('Regulations',views.Regulations,name='Regulations'),
    path('Courses',views.Courses,name='Courses'),
    path('Manage_Faculty',views.Manage_Faculty,name='Manage_FacultyManage_Faculty'),
    path('test1',views.test1,name='test1'),
    path('course_marks',views.course_marks,name='course_marks'),
    path('storeinput',views.storeinput,name='storeinput'),
    path('faculty_dashboard',views.faculty_dashboard,name='faculty_dashboard'),
    path('department_dashboard',views.department_dashboard,name='department_dashboard'),
    #***************************New**********
    path('login',lessonplan.login,name='login'),
    path('lessonplan/inputform',lessonplan.inputform,name='inputform'),
    path('lessonplan/storeinput',lessonplan.storeinput,name='storeinput'),
    path('lessonplan/inputcoursecode',lessonplan.inputcoursecode,name='inputcoursecode'),
    path('lessonplan/updatecoursecode',lessonplan.updatecoursecode,name='updatecoursecode'),
    path('lessonplan/updateplan',lessonplan.updateplan,name='updateplan'),
    path('lessonplan/updateinput',lessonplan.updateinput,name='storeinput'),
    path('lessonplan/viewplan',lessonplan.viewplan,name='viewplan'),
    path('lessonplan/mainpage',lessonplan.mainpage,name='mainpage'),
]