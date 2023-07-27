from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from dynamic_models.models import ModelSchema, FieldSchema
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# admin.site.register(ModelSchema)
# admin.site.register(FieldSchema)
import pandas as pd
import numpy as np
from .models import *
from .forms import *

#<=======================================Admin(HOD's) and Faculty Logins =================================>

def user_login(request):
    if request.user.is_authenticated:
        return redirect(faculty_dashboard)
    if request.method == "POST":
        uname = request.POST['unamef']
        pswd = request.POST['pswdf']
        if CustomUser.objects.filter(username=uname).exists():
                   obj=CustomUser.objects.get(username=uname)
                   if(obj.password==pswd):
                        login(request, obj)
                        return redirect('faculty_dashboard')
                   else:
                        print("error")
                        messages.error(request,'invalid passwod please try again')
                        return render(request, 'obeapp/land.html')

        else:
            print("in else of faculty login*******")
            return render(request, 'obeapp/land.html')
    else:
     return render(request, 'obeapp/land.html')

def user_logout(request):
    logout(request)
    return redirect(user_login)  # Replace 'login' with the name of your login page URL pattern

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_login)  # Redirect to login page after successful registration

    else:
        form = RegistrationForm()

    return render(request, 'obeapp/faculty/faculty_registration.html', {'form': form})





#<=======================================College Admin Logins =================================>


def admin_login(request):
    if request.user.is_authenticated:
        return redirect(admin_dashboard)
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password=pswd)
        if user and user.is_superuser:
            login(request, user)
            request.session['user_name'] = uname
            return redirect(admin_dashboard)
        else:
            return render(request, 'obeapp/admin_login.html', {'error': True})
    return render(request, 'obeapp/admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect(user_login)




#<=======================================Dashboards funtions =================================>


@login_required(login_url='/admin_login')
def admin_dashboard(request):
    return render(request, 'obeapp/admin/admin_dashboard.html')
def faculty_dashboard(request):
    return render(request, 'obeapp/faculty/faculty_dashboard.html')
def department_dashboard(request):
    return render(request, 'obeapp/faculty/department_admin.html')



#<=======================================Admin Activities =================================>

def Regulations(request):
    print("regulation")
    reg = Regulation.objects.all()
    return render(request, 'obeapp/admin/Regulations.html',{'reg':reg})

def add_regulation(request):
    reg = Regulation.objects.all()
    if request.method == "POST":
        regulation = request.POST['regulation']
        batch = request.POST['batch']
        print(regulation)
        if(len(Regulation.objects.filter(Regulation=regulation)) == 0):  
            Reg = Regulation()
            Reg.Sno = len(reg)+1
            Reg.Regulation = regulation
            Reg.batch = batch
            Reg.save()
            reg = Regulation.objects.all()
            return render(request, 'obeapp/admin/Regulations.html',{'reg':reg})
        else:
            messages.error(request,'Regulation already exists')
    return redirect(Regulations)

def Course(request):
    courses = Courses.objects.filter(branch="cse")
    return render(request, 'obeapp/admin/Courses.html',{'courses':courses})


def add_course(request):
    if request.method == "POST":
        course = request.POST['course']
        coursecode = request.POST['coursename']
        reg = request.POST['reg']
        sem = request.POST['sem']
        acyear = request.POST['acyear']
        branch = "cse"
        clen = Courses.objects.all()
        cour = Courses()
        cour.Sno = len(clen)+1
        cour.Coursenam = course
        cour.Coursecode = coursecode
        cour.Regulation = reg
        cour.year = acyear
        cour.semister = sem
        cour.branch = branch
        cour.save()
    return redirect(Course)

def edit_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    
    if request.method == "POST":
        # Retrieve the edited course information
        course_name = request.POST['course']
        course_code = request.POST['coursename']
        regulation = request.POST['reg']
        semester = request.POST['sem']
        academic_year = request.POST['acyear']

        # Update the course fields
        course.Coursenam = course_name
        course.Coursecode = course_code
        course.Regulation = regulation
        course.year = academic_year
        course.semister = semester
        course.save()

        # Redirect back to the Course list page
        return redirect(Course)  # Assuming you've named the URL for the course list page as 'course-list'

    return render(request, 'obeapp/admin/edit_course.html', {'course': course})


def Manage_Faculty(request):
    return render(request, 'obeapp/admin/Manage_Faculty.html')


#<=======================================Faculty Activities =================================>

# def admin_hods_dashboard_sam(request):
#     return render(request, 'obeapp/admin_hods_dashboard_sam.html')
# def faculty_dashboard_sam(request):
#     return render(request, 'obeapp/faculty/faculty_dashboard_sam.html')
# def index(request):
#     return render(request, 'obeapp/land.html')

# def test1(request):
#     return render(request, 'obeapp/frontend/test1.html')


    





# Regulations
#<=======================================Attainments block =================================>

def mid1_results_table(reg):
    l1 = ['branch', 'coursecode', 'acyear', 'sem']
    book_schema = ModelSchema.objects.create(name=str(reg) + 'mid1')
    c = 0
    for i in range(4):
        l1[i] = FieldSchema.objects.create(
            name=l1[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )
    exp = ['a' + str(i) for i in range(27)]
    c = 0
    for i in range(1, 4):
        for k in ['a', 'b', 'c']:
            for j in ['atn', 'atmp', 'per']:
                # a = 'co'+i+k+'_'+j
                exp[c] = FieldSchema.objects.create(
                    name='co' + str(i) + k + '_' + j,
                    data_type='integer' if j != 'per' else 'float',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    exp2 = ['a' + str(i) for i in range(6)]
    c1 = 0
    for i in ['co1', 'co2', 'co3']:
        for j in ['atnper', 'atnlvl']:
            # b = i+'_'+j
            exp2[c1] = FieldSchema.objects.create(
                name=i + '_' + j,
                data_type='integer' if j != 'atnper' else 'float',
                model_schema=book_schema,
                max_length=255,
            )
            c1 += 1

    Book = book_schema.as_model()


def mid2_results_table(reg):
    l1 = ['branch', 'coursecode', 'acyear', 'sem']
    book_schema = ModelSchema.objects.create(name=str(reg) + 'mid2')
    c = 0
    for i in range(4):
        l1[i] = FieldSchema.objects.create(
            name=l1[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )
    exp = ['a' + str(i) for i in range(27)]
    c = 0
    for i in range(3, 6):
        for k in ['a', 'b', 'c']:
            for j in ['atn', 'atmp', 'per']:
                # a = 'co'+i+k+'_'+j
                exp[c] = FieldSchema.objects.create(
                    name='co' + str(i) + k + '_' + j,
                    data_type='integer' if j != 'per' else 'float',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    exp2 = ['a' + str(i) for i in range(6)]
    c1 = 0
    for i in ['co3', 'co4', 'co5']:
        for j in ['atnper', 'atnlvl']:
            # b = i+'_'+j
            exp2[c1] = FieldSchema.objects.create(
                name=i + '_' + j,
                data_type='integer' if j != 'atnper' else 'float',
                model_schema=book_schema,
                max_length=255,
            )
            c1 += 1
    Book = book_schema.as_model()

def sem_results_table(reg):
    l1 = ['branch', 'coursecode', 'academicyear', 'sem']
    book_schema = ModelSchema.objects.create(name=str(reg) + 'sem')
    c = 0
    for i in range(4):
        l1[i] = FieldSchema.objects.create(
            name=l1[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )
    exp = ['a' + str(i) for i in range(45)]
    c = 0
    for i in range(1, 6):
        for k in ['a', 'b', 'c']:
            for j in ['attained', 'attempted', 'percentage']:
                # a = 'co'+i+k+'_'+j
                exp[c] = FieldSchema.objects.create(
                    name='co' + str(i) + k + '_' + j,
                    data_type='integer' if j != 'percentage' else 'float',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    exp2 = ['a' + str(i) for i in range(10)]
    c1 = 0
    for i in ['co1', 'co2', 'co3', 'co4', 'co5']:
        for j in ['attainment_percentage', 'attainment_level']:
            # b = i+'_'+j
            exp2[c1] = FieldSchema.objects.create(
                name=i + '_' + j,
                data_type='integer' if j != 'attainment_percentage' else 'float',
                model_schema=book_schema,
                max_length=255,
            )
            c1 += 1
    Book = book_schema.as_model()

def mid1_marks_table(reg):
    book_schema = ModelSchema.objects.create(name=str(reg) + 'mid1_marks')
    q = 'co'
    alp = ['a', 'b', 'c']

    # # add fields to the schema
    lst = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17',
           'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a28', 'a30']
    c = 0
    rno = FieldSchema.objects.create(
        name='Roll_no',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    for i in range(3):
        for j in alp:
            lst[c] = FieldSchema.objects.create(
                name=q + str(i + 1) + '_' + j,
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1
    alpp = ['max']
    for i in range(3):
        for k in alp:
            for j in alpp:
                lst[c] = FieldSchema.objects.create(
                    name=q + str(i + 1) + '_' + k + '_' + j,
                    data_type='integer' if j == 'max' else 'float',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    Total = FieldSchema.objects.create(
        name='Total',
        data_type='integer',
        model_schema=book_schema,
        max_length=255,
    )
    lst1 = ['branch', 'course_code', 'academic_year', 'sem']
    lst2 = ['branch', 'course_code', 'academic_year', 'sem']
    for i in range(4):
        lst1[i] = FieldSchema.objects.create(
            name=lst2[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )

    Book = book_schema.as_model()


def mid2_marks_table(reg):
    book_schema = ModelSchema.objects.create(name=str(reg) + 'mid2_marks')
    q = 'co'
    alp = ['a', 'b', 'c']

    # # add fields to the schema
    lst = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17',
           'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a28', 'a30']
    c = 0
    rno = FieldSchema.objects.create(
        name='Roll_no',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    for i in range(3, 6):
        for j in alp:
            lst[c] = FieldSchema.objects.create(
                name=q + str(i) + '_' + j,
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1
    alpp = ['max']
    for i in range(3, 6):
        for k in alp:
            for j in alpp:
                lst[c] = FieldSchema.objects.create(
                    name=q + str(i) + '_' + k + '_' + j,
                    data_type='integer' if j == 'max' else 'float',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    Total = FieldSchema.objects.create(
        name='Total',
        data_type='integer',
        model_schema=book_schema,
        max_length=255,
    )
    lst1 = ['branch', 'course_code', 'academic_year', 'sem']
    lst2 = ['branch', 'course_code', 'academic_year', 'sem']
    for i in range(4):
        lst1[i] = FieldSchema.objects.create(
            name=lst2[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )

    Book = book_schema.as_model()

def sem_marks_table(reg):
    book_schema = ModelSchema.objects.create(name=str(reg) + 'sem_marks')
    q = 'co'
    alp = ['a', 'b', 'c']
    # # add fields to the schema
    lst = ['a' + str(i) for i in range(45)]
    c = 0
    '''rno = FieldSchema.objects.create(
                name='Roll_no',
                data_type='character',
                model_schema=book_schema,
                max_length=255,
            )'''
    for i in range(5):
        for j in alp:
            lst[c] = FieldSchema.objects.create(
                name=q + str(i + 1) + '_' + j,
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1
    alpp = ['max']
    for i in range(5):
        for k in alp:
            for j in alpp:
                lst[c] = FieldSchema.objects.create(
                    name=q + str(i + 1) + '_' + k + '_' + j,
                    data_type='integer',
                    model_schema=book_schema,
                    max_length=255,
                )
                c += 1
    '''Total = FieldSchema.objects.create(
                name='Total',
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )'''
    lst1 = ['branch', 'course_code', 'academic_year', 'sem']
    lst2 = ['branch', 'course_code', 'academic_year', 'sem']
    for i in range(4):
        lst1[i] = FieldSchema.objects.create(
            name=lst2[i],
            data_type='character',
            model_schema=book_schema,
            max_length=255,
        )

    Book = book_schema.as_model()

def mid1_marks_insert(name):
    book_schema = ModelSchema.objects.get(name='v20mid1_marks')
    Book = book_schema.as_model()
    df1 = pd.read_excel(name)
    # print(df1)
    df2 = df1.drop(['Total Marks'], axis=1)
    # print(df2)
    m = list(df2.iloc[3])
    l = list(df2.iloc[2])
    print(l[2], m)
    df = pd.read_excel(name, skiprows=[0, 1, 2, 3, 4])
    df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']
    # df['q2']=df['q2'].replace({'NaN':-1})
    df = df.fillna(-1)
    df = df.replace('A', -2)
    branch = 'EEE'
    course_code = 'V20EET02'
    academic_year = '2021-22'
    sem = 'IV'
    for i in df.index:
        f = Book.objects.create(roll_no=df['rno'][i], co1_a=df['q1'][i], co1_b=df['q2'][i], co1_c=df['q3'][i],
                                co2_a=df['q4'][i], co2_b=df['q5'][i], co2_c=df['q6'][i], co3_a=df['q7'][i],
                                co3_b=df['q8'][i], co3_c=df['q9'][i], total=df['total'][i]
                                , branch=branch, course_code=course_code, academic_year=academic_year, sem=sem,
                                co1_a_max=m[2], co1_b_max=m[3], co1_c_max=m[4], co2_a_max=m[5], co2_b_max=m[6],
                                co2_c_max=m[7], co3_a_max=m[8], co3_b_max=m[9], co3_c_max=m[10])
        f.save()


def mid2_marks_insert(name):
    book_schema = ModelSchema.objects.get(name='v20mid2_marks')
    Book = book_schema.as_model()
    df1 = pd.read_excel(name)
    # print(df1)
    df2 = df1.drop(['Total Marks'], axis=1)
    # print(df2)
    m = list(df2.iloc[3])
    l = list(df2.iloc[2])
    print(l[2], m)
    df = pd.read_excel(name, skiprows=[0, 1, 2, 3, 4])
    df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']
    # df['q2']=df['q2'].replace({'NaN':-1})
    df = df.fillna(-1)
    df = df.replace('A', -2)
    branch = 'EEE'
    course_code = 'V20EET02'
    academic_year = '2021-22'
    sem = 'IV'
    for i in df.index:
        f = Book.objects.create(roll_no=df['rno'][i], co3_a=df['q1'][i], co3_b=df['q2'][i], co3_c=df['q3'][i],
                                co4_a=df['q4'][i], co4_b=df['q5'][i], co4_c=df['q6'][i], co5_a=df['q7'][i],
                                co5_b=df['q8'][i], co5_c=df['q9'][i], total=df['total'][i]
                                , branch=branch, course_code=course_code, academic_year=academic_year, sem=sem,
                                co3_a_max=m[2], co3_b_max=m[3], co3_c_max=m[4], co4_a_max=m[5], co4_b_max=m[6],
                                co4_c_max=m[7], co5_a_max=m[8], co5_b_max=m[9], co5_c_max=m[10])
        f.save()

def sem_marks_insert(regname):
    book_schema = ModelSchema.objects.get(name='v20sem_marks')
    Book = book_schema.as_model()
    df2 = pd.read_excel(regname)
    maxmarks = list(df2.iloc[3])
    df = pd.read_excel(regname, skiprows=[0, 1, 2, 3, 4])
    df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
                  'q15']
    df = df.fillna(-1)
    df = df.replace('A', -2)
    branch = 'EEE'
    course_code = 'V20EET02'
    academic_year = '2021-22'
    sem = 'IV'
    for i in df.index:
        f = Book.objects.create(co1_a=df['q1'][i], co1_b=df['q2'][i], co1_c=df['q3'][i], co2_a=df['q4'][i],
                                co2_b=df['q5'][i], co2_c=df['q6'][i], co3_a=df['q7'][i], co3_b=df['q8'][i],
                                co3_c=df['q9'][i], co4_a=df['q10'][i], co4_b=df['q11'][i], co4_c=df['q12'][i],
                                co5_a=df['q13'][i], co5_b=df['q14'][i], co5_c=df['q15'][i]
                                , branch=branch, course_code=course_code, academic_year=academic_year, sem=sem,
                                co1_a_max=maxmarks[2], co1_b_max=maxmarks[3], co1_c_max=maxmarks[4],
                                co2_a_max=maxmarks[5], co2_b_max=maxmarks[6], co2_c_max=maxmarks[7],
                                co3_a_max=maxmarks[8], co3_b_max=maxmarks[9], co3_c_max=maxmarks[10]
                                , co4_a_max=maxmarks[11], co4_b_max=maxmarks[12], co4_c_max=maxmarks[13],
                                co5_a_max=maxmarks[14], co5_b_max=maxmarks[15], co5_c_max=maxmarks[16])
        f.save()
    calculate_sem_results(regname, academic_year, course_code, branch)

def calculate_mid1_results(regname):
    book_schema = ModelSchema.objects.get(name=str(regname) + 'mid1_marks')
    book = book_schema.as_model()
    Book = book.objects.all()
    attain, attem, per, attainper, attainlvl = [], [], [], [], []
    df = pd.DataFrame(Book.values_list(), columns=Book.values()[0])
    for i in range(1, 4):
        atnpr = []
        tp = targetproficiency.objects.get(course_code=df['course_code'][0], co="co" + str(i))
        prflvl = int(tp.tpl)
        for j in ['a', 'b', 'c']:

            maxmk = df['co' + str(i) + '_' + str(j) + '_max'][0]
            df1 = df[['co' + str(i) + '_' + str(j)]]
            atn = int(df1[(df1['co' + str(i) + '_' + str(j)] >= 0) & (
                        df1['co' + str(i) + '_' + str(j)] >= maxmk * prflvl)].count(axis=0))
            atm = int(df1[df1['co' + str(i) + '_' + str(j)] >= 0].count(axis=0))
            atn1 = -1 if not atn and not atm else atn
            atm1 = -1 if not atm else atm
            attain.append(atn1)
            attem.append(atm1)
            if (atn1 != -1):
                per.append(round((atn1 / atm1) * 100, 2))
                atnpr.append((atn1 / atm1) * 100)
            else:
                per.append(-1)
        attainper.append(round(sum(atnpr) / len(atnpr), 3))
        if attainper[-1] > tp.l3:  # These level are taken  temporarly we should take form user
            attainlvl.append(3)
        elif attainper[-1] > tp.l2:
            attainlvl.append(2)
        elif attainper[-1] > tp.l1:
            attainlvl.append(1)
        else:
            attainlvl.append(0)
    # print(type(attain[0]),attem,per)
    mid1_schema = ModelSchema.objects.get(name=str(regname) + 'mid1')
    mid1 = mid1_schema.as_model()
    mid1.objects.create(branch=df['branch'][0], coursecode=df['course_code'][0], acyear=df['academic_year'][0],
                        sem=df['sem'][0],
                        co1a_atn=attain[0], co1a_atmp=attem[0], co1a_per=per[0], co1b_atn=attain[1], co1b_atmp=attem[1],
                        co1b_per=per[1], co1c_atn=attain[2], co1c_atmp=attem[2], co1c_per=per[2],
                        co2a_atn=attain[3], co2a_atmp=attem[3], co2a_per=per[3], co2b_atn=attain[4], co2b_atmp=attem[4],
                        co2b_per=per[4], co2c_atn=attain[5], co2c_atmp=attem[5], co2c_per=per[5],
                        co3a_atn=attain[6], co3a_atmp=attem[6], co3a_per=per[6], co3b_atn=attain[7], co3b_atmp=attem[7],
                        co3b_per=per[7], co3c_atn=attain[8], co3c_atmp=attem[8], co3c_per=per[8],
                        co1_atnper=attainper[0], co1_atnlvl=attainlvl[0], co2_atnper=attainper[1],
                        co2_atnlvl=attainlvl[1], co3_atnper=attainper[2], co3_atnlvl=attainlvl[2])


def calculate_mid2_results(regname):
    book_schema = ModelSchema.objects.get(name=str(regname) + 'mid2_marks')
    book = book_schema.as_model()
    Book = book.objects.all()
    attain, attem, per, attainper, attainlvl = [], [], [], [], []
    df = pd.DataFrame(Book.values_list(), columns=Book.values()[0])
    for i in range(3, 6):
        atnpr = []
        tp = targetproficiency.objects.get(course_code=df['course_code'][0], co="co" + str(i))
        prflvl = int(tp.tpl)
        for j in ['a', 'b', 'c']:
            # prflvl = df['co'+str(i)+'_'+str(j)+'_proflvl'][0]
            maxmk = df['co' + str(i) + '_' + str(j) + '_max'][0]
            df1 = df[['co' + str(i) + '_' + str(j)]]
            atn = int(df1[(df1['co' + str(i) + '_' + str(j)] >= 0) & (
                        df1['co' + str(i) + '_' + str(j)] >= maxmk * prflvl)].count(axis=0))
            atm = int(df1[df1['co' + str(i) + '_' + str(j)] >= 0].count(axis=0))
            atn1 = -1 if not atn and not atm else atn
            atm1 = -1 if not atm else atm
            attain.append(atn1)
            attem.append(atm1)
            if (atn1 != -1):
                per.append(round((atn1 / atm1) * 100, 2))
                atnpr.append((atn1 / atm1) * 100)
            else:
                per.append(-1)
        attainper.append(round(sum(atnpr) / len(atnpr), 3))
        if attainper[-1] > tp.l3:  # These level are taken  temporarly we should take form user
            attainlvl.append(3)
        elif attainper[-1] > tp.l2:
            attainlvl.append(2)
        elif attainper[-1] > tp.l1:
            attainlvl.append(1)
        else:
            attainlvl.append(0)
    # print(attain,attem,per)
    mid2_schema = ModelSchema.objects.get(name=str(regname) + 'mid2')
    mid2 = mid2_schema.as_model()
    mid2.objects.create(branch=df['branch'][0], coursecode=df['course_code'][0], acyear=df['academic_year'][0],
                        sem=df['sem'][0],
                        co3a_atn=attain[0], co3a_atmp=attem[0], co3a_per=per[0], co3b_atn=attain[1], co3b_atmp=attem[1],
                        co3b_per=per[1], co3c_atn=attain[2], co3c_atmp=attem[2], co3c_per=per[2],
                        co4a_atn=attain[3], co4a_atmp=attem[3], co4a_per=per[3], co4b_atn=attain[4], co4b_atmp=attem[4],
                        co4b_per=per[4], co4c_atn=attain[5], co4c_atmp=attem[5], co4c_per=per[5],
                        co5a_atn=attain[6], co5a_atmp=attem[6], co5a_per=per[6], co5b_atn=attain[7], co5b_atmp=attem[7],
                        co5b_per=per[7], co5c_atn=attain[8], co5c_atmp=attem[8], co5c_per=per[8],
                        co3_atnper=attainper[0], co3_atnlvl=attainlvl[0], co4_atnper=attainper[1],
                        co4_atnlvl=attainlvl[1], co5_atnper=attainper[2], co5_atnlvl=attainlvl[2])

def calculate_sem_results(regname, academicyear, coursecode, branch):
    book_schema = ModelSchema.objects.get(name=str(regname) + 'sem_marks')
    book = book_schema.as_model()
    Book = book.objects.all()
    attain, attem, per, attainper, attainlvl = [], [], [], [], []
    df = pd.DataFrame(Book.values_list(), columns=Book.values()[0])
    coursecode = df['course_code'][0]
    tp = targetproficiency.objects.filter(course_code=coursecode)
    for i in range(1, 6):
        atnpr = []
        tp = targetproficiency.objects.get(course_code=coursecode, co="co" + str(i))
        prflvl = int(tp.tpl)
        # print(prflvl)
        for j in ['a', 'b', 'c']:

            maxmk = df['co' + str(i) + '_' + str(j) + '_max'][0]
            df1 = df[['co' + str(i) + '_' + str(j)]]
            atn = int(df1[(df1['co' + str(i) + '_' + str(j)] >= 0) & (
                        df1['co' + str(i) + '_' + str(j)] > maxmk * prflvl)].count(axis=0))
            # print(df1['co'+str(i)+'_'+str(j)],"##",maxmk*prflvl)
            atm = int(df1[df1['co' + str(i) + '_' + str(j)] >= 0].count(axis=0))
            atn1 = -1 if not atn and not atm else atn
            atm1 = -1 if not atm else atm
            attain.append(atn1)
            attem.append(atm1)
            if (atn1 != -1):
                per.append(round((atn1 / atm1) * 100, 2))
                atnpr.append((atn1 / atm1) * 100)
            else:
                per.append(-1)
        attainper.append(round(sum(atnpr) / len(atnpr), 3))
        if attainper[-1] > tp.l3:  # These level are taken  temporarly we should take form user
            attainlvl.append(3)
        elif attainper[-1] > tp.l2:
            attainlvl.append(2)
        elif attainper[-1] > tp.l1:
            attainlvl.append(1)
        else:
            attainlvl.append(0)
    # print(attainper)

    sem_schema = ModelSchema.objects.get(name=str(regname) + 'sem')
    sem = sem_schema.as_model()
    sem.objects.create(branch=df['branch'][0], coursecode=df['course_code'][0], academicyear=df['academic_year'][0],
                       sem=df['sem'][0],
                       co1a_attained=attain[0], co1a_attempted=attem[0], co1a_percentage=per[0],
                       co1b_attained=attain[1], co1b_attempted=attem[1], co1b_percentage=per[1],
                       co1c_attained=attain[2], co1c_attempted=attem[2], co1c_percentage=per[2],
                       co2a_attained=attain[3], co2a_attempted=attem[3], co2a_percentage=per[3],
                       co2b_attained=attain[4], co2b_attempted=attem[4], co2b_percentage=per[4],
                       co2c_attained=attain[5], co2c_attempted=attem[5], co2c_percentage=per[5],
                       co3a_attained=attain[6], co3a_attempted=attem[6], co3a_percentage=per[6],
                       co3b_attained=attain[7], co3b_attempted=attem[7], co3b_percentage=per[7],
                       co3c_attained=attain[8], co3c_attempted=attem[8], co3c_percentage=per[8],
                       co1_attainment_percentage=attainper[0], co1_attainment_level=attainlvl[0],
                       co2_attainment_percentage=attainper[1], co2_attainment_level=attainlvl[1],
                       co3_attainment_percentage=attainper[2], co3_attainment_level=attainlvl[2],
                       co4a_attained=attain[9], co4a_attempted=attem[9], co4a_percentage=per[9],
                       co4b_attained=attain[10], co4b_attempted=attem[10], co4b_percentage=per[10],
                       co4c_attained=attain[11], co4c_attempted=attem[11], co4c_percentage=per[11],
                       co5a_attained=attain[12], co5a_attempted=attem[12], co5a_percentage=per[12],
                       co5b_attained=attain[13], co5b_attempted=attem[13], co5b_percentage=per[13],
                       co5c_attained=attain[14], co5c_attempted=attem[14], co5c_percentage=per[14],
                       co4_attainment_percentage=attainper[3], co4_attainment_level=attainlvl[3],
                       co5_attainment_percentage=attainper[4], co5_attainment_level=attainlvl[4])

def course_marks(request):
    return render(request, 'obeapp/obapp/storeinput2.html')


def storeinput(request):
    if request.method == 'POST':
        nm = request.FILES['file']
        mid1_marks_insert(nm)
        mid2_marks_insert(nm)
    else:
        return redirect('login')
    return render(request, 'obeapp/obapp/storeinput2.html')


# mid1_marks_table('v20')
# mid2_marks_table('v20')
# mid1_results_table('v20')
# mid2_results_table('v20')
# sem_marks_table('v20')
# sem_results_table('v20')
# print(len(Regulation.objects.filter(Regulation='v20')))
