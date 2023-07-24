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
    path('faculty_dashboard_sam',views.faculty_dashboard_sam,name='faculty_dashboard_sam'),
    path('admin_hods_dashboard_sam',views.admin_hods_dashboard_sam,name='admin_hods_dashboard_sam'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('Regulations',views.Regulations,name='Regulations'),
    path('Courses',views.Courses,name='Courses'),
    path('Manage_Faculty',views.Manage_Faculty,name='Manage_FacultyManage_Faculty'),
    path('lessonplans',views.lessonplans,name='lessonplans'),
    path('courses',views.courses,name='courses'),
    path('textref',views.textref,name='textref'),
    path('profmatrix',views.profmatrix,name='profmatrix'),
    path('lectureplan',views.lectureplan,name='lectureplan'),
    path('copsomatrix',views.copsomatrix,name='copsomatrix'),
    path('endsurveyquesnr',views.endsurveyquesnr,name='endsurveyquesnr'),
    path('test',views.test,name='test'),
    path('test1',views.test1,name='test1'),
]