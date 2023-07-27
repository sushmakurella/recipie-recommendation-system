from django.urls import path
from . import views,lessonplan

urlpatterns = [
    # path('',views.home,name='home'),
    # path('',views.index,name='index'),


    #<=========================================Admin urls=======================================>
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('add_regulation',views.add_regulation,name='add_regulation'),
    path('Regulations',views.Regulations,name='Regulations'),
    path('Courses',views.Course,name='Courses'),
    path('add_course',views.add_course,name='add_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('Manage_Faculty',views.Manage_Faculty,name='Manage_Faculty'),
    path('add_faculty',views.add_faculty,name='add_faculty'),
    path('edit_faculty/<int:id>/', views.edit_faculty, name='edit_faculty'),
    path('delete_faculty/<int:id>/', views.delete_faculty, name='delete_faculty'),
    #<=========================================Faculty urls=======================================>
    
    # path('test1',views.test1,name='test1'),
    # path('course_marks',views.course_marks,name='course_marks'),
    # path('storeinput',views.storeinput,name='storeinput'),
    path('',views.user_login,name='index'),
    path('user_register',views.user_registration,name='user_register'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('faculty_dashboard',views.faculty_dashboard,name='faculty_dashboard'),

    #<=========================================College Admin urls=======================================>

    path('department_dashboard',views.department_dashboard,name='department_dashboard'),






    #<=========================================Lesson Plan=======================================>
    
    path('login',lessonplan.login,name='login'),
    path('lessonplan/inputform',lessonplan.inputform,name='inputform'),
    path('lessonplan/storeinput',lessonplan.storeinput,name='storeinput'),
    path('lessonplan/inputcoursecode',lessonplan.inputcoursecode,name='inputcoursecode'),
    path('lessonplan/updatecoursecode',lessonplan.updatecoursecode,name='updatecoursecode'),
    path('lessonplan/updateplan',lessonplan.updateplan,name='updateplan'),
    path('lessonplan/updateinput',lessonplan.updateinput,name='storeinput'),
    path('lessonplan/viewplan',lessonplan.viewplan,name='viewplan'),
    path('lessonplan/mainpage',lessonplan.mainpage,name='mainpage'),
    #path('lessonplan/mainpageview',lessonplan.mainpageview,name='mainpageview'),
]