from django.shortcuts import render, redirect
from django.contrib import admin
from dynamic_models.models import ModelSchema, FieldSchema
import pandas as pd
import math

def avg_att_per():
    """
    This function creates a dynamic model schema 'v20_avg_att' and defines fields for storing average attendance data.
    The fields include 'per_lvl', which represents the percentage level, and 'co1', 'co2', 'co3', and 'co4' for different course outcomes.
    """
    book_schema = ModelSchema.objects.create(name='v20_avg_att')
    
    # Create the 'per_lvl' field
    per_lvl = FieldSchema.objects.create(
        name='per_lvl',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    
    # Create the 'co1', 'co2', 'co3', 'co4' fields
    lst = ['co1', 'co2', 'co3', 'co4']
    for i in range(4):
        lst[i] = FieldSchema.objects.create(
            name=lst[i],
            data_type='integer',
            model_schema=book_schema,
            max_length=255,
        )

def mid1_attain1():
    """
    This function creates a dynamic model schema 'v20cpl5' and defines fields for storing mid-semester attainment data.
    The fields include 'at_atmp_per' representing the attainment level, and 'co1q1a' to 'co3q3c' for different course outcomes.
    """
    book_schema = ModelSchema.objects.create(name='v20cpl5')
    
    # Create the 'at_atmp_per' field
    at_atmp_per = FieldSchema.objects.create(
        name='at_atmp_per',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    
    # Create fields for different course outcomes and their levels
    c = 0
    lst = ['a' + str(i) for i in range(9)]
    alp = ['a', 'b', 'c']
    for i in range(3):
        for j in range(3):
            lst[c] = FieldSchema.objects.create(
                name='co' + str(i+1) + 'q' + str(i+1) + alp[j],
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1

def cpl():
    """
    This function creates a dynamic model schema 'v20cpl1' and defines fields for storing course performance level data.
    The fields include 'co' representing the course outcome, and 'pl', 'tpl1', 'tpl2', 'tpl3' representing performance levels.
    """
    book_schema = ModelSchema.objects.create(name='v20cpl1')
    
    # Create the 'co' field
    co = FieldSchema.objects.create(
        name='co',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    
    # Create fields for performance levels
    lst = ['pl', 'tpl1', 'tpl2', 'tpl3']
    for i in range(4):
        lst[i] = FieldSchema.objects.create(
            name=lst[i],
            data_type='integer',
            model_schema=book_schema,
            max_length=255,
        )

def call():
    """
    This function creates a dynamic model schema 'mid14' and defines fields for storing mid-semester assessment data.
    The fields include'Roll_no' for student roll number and 'q1a' to 'q9' for different assessment questions.
    """
    book_schema = ModelSchema.objects.create(name='mid14')
    
    # Create the 'Roll_no' field
    rno = FieldSchema.objects.create(
        name='Roll_no',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    
    # Create fields for different assessment questions
    lst = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
    alp=['a','b','c']
    c = 0
    for i in range(3):
        for j in range(3):
            lst[c] = FieldSchema.objects.create(
                name='q' + str(i+1) + alp[j],
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1
    
    # Create the 'Total' field
    total = FieldSchema.objects.create(
        name='Total',
        data_type='integer',
        model_schema=book_schema,
        max_length=255,
    )

# def data_insert():
#     """
#     This function inserts data into the dynamically created models based on an Excel file.
#     It reads the data from the Excel file, creates model instances, and saves them to the database.
#     """
#     book_schema = ModelSchema.objects.get(name='mid14')
#     Book = book_schema.as_model()
    
#     # Read the Excel file
#     df1 = pd.read_excel("C:/Users/Dell/OneDrive/Desktop/obexl1.xlsx")
#     df = df1[5:]
#     df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']
    
#     # Replace NaN and 'A' values with appropriate placeholders
#     df = df.fillna(-1)
#     df = df.replace('A', -2)
    
#     # Define course details
#     branch = 'CSE'
#     course_code = 'V20qwer'
#     academic_year = '2021-22'
#     sem = 'IV'
    
#     # Process the data and insert into the models
#     for i in df.index:
#         f = Book.objects.create(
#             roll_no=df['rno'][i],
#             q1a=df['q1'][i],
#             q1b=df['q2'][i],
#             q1c=df['q3'][i],
#             q2a=df['q4'][i],
#             q2b=df['q5'][i],
#             q2c=df['q6'][i],
#             q3a=df['q7'][i],
#             q3b=df['q8'][i],
#             q3c=df['q9'][i],
#             total=df['total'][i],
#             branch=branch,
#             course_code=course_code,
#             academic_year=academic_year,
#             sem=sem
#         )
#         f.save()
def data_insert():
    """
    This function inserts data from an Excel file into the dynamically created models.
    It reads the data from the Excel file, processes it, and saves the data as model instances.
    """

    # Get the dynamic model schema
    book_schema = ModelSchema.objects.get(name='mid14')
    Book = book_schema.as_model()

    # Read the data from the Excel file
    df1 = pd.read_excel("C:/Users/Dell/OneDrive/Desktop/obexl1.xlsx")
    df = df1[5:]
    df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']
    df1.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']

    # Replace NaN and 'A' values with appropriate placeholders
    df = df.fillna(-1)
    df = df.replace('A', -2)

    # Extract necessary data
    df2 = df1[3:4]
    df2.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total']
    branch = 'CSE'
    course_code = 'V20qwer'
    academic_year = '2021-22'
    sem = 'IV'

    val = []
    lst = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']

    # Get maximum percentages for each CO from 'V20cpl1' model
    T3 = ModelSchema.objects.get(name='V20cpl1')
    t3 = T3.as_model()
    max_per = []
    for i in range(3):
        obj = t3.objects.get(co='co'+str(i+1), branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
        max_per.append(obj.pl)

    # Calculate the number of students who attained the CO for each assessment question
    for i in range(9):
        df[lst[i]] = pd.to_numeric(df[lst[i]])
        mxp = max_per[0] if i <= 2 else max_per[1] if i <= 5 else max_per[2]
        l = len(df[df[lst[i]] >= math.ceil((df2.at[3, lst[i]] * mxp) / 100)])
        val.append(l)

    atmp = []

    # Calculate the number of students who attempted the assessment question
    for i in range(9):
        df[lst[i]] = pd.to_numeric(df[lst[i]])
        l = len(df[df[lst[i]] >= 0])
        atmp.append(l)

    # Insert data into the 'mid14' model
    for i in df.index:
        f = Book.objects.create(
            roll_no=df['rno'][i],
            q1a=df['q1'][i],
            q1b=df['q2'][i],
            q1c=df['q3'][i],
            q2a=df['q4'][i],
            q2b=df['q5'][i],
            q2c=df['q6'][i],
            q3a=df['q7'][i],
            q3b=df['q8'][i],
            q3c=df['q9'][i],
            total=df['total'][i],
            branch=branch,
            course_code=course_code,
            academic_year=academic_year,
            sem=sem
        )
        f.save()

    # Get the dynamic models 'v20cpl5' and 'v20_avg_att'
    T1 = ModelSchema.objects.get(name='v20cpl5')
    t1 = T1.as_model()
    T2 = ModelSchema.objects.get(name='v20_avg_att')
    t2 = T2.as_model()

    # Insert data into 'v20cpl5' model
    obj1 = t1.objects.create(
        at_atmp_per='attained',
        co1q1a=val[0],
        co1q1b=val[1],
        co1q1c=val[2],
        co2q2a=val[3],
        co2q2b=val[4],
        co2q2c=val[5],
        co3q3a=val[6],
        co3q3b=val[7],
        co3q3c=val[8],
        branch=branch,
        course_code=course_code,
        academic_year=academic_year,
        sem=sem
    )
    obj1.save()

    # Insert data into 'v20cpl5' model for attempted questions
    obj2 = t1.objects.create(
        at_atmp_per='attempted',
        co1q1a=atmp[0],
        co1q1b=atmp[1],
        co1q1c=atmp[2],
        co2q2a=atmp[3],
        co2q2b=atmp[4],
        co2q2c=atmp[5],
        co3q3a=atmp[6],
        co3q3b=atmp[7],
        co3q3c=atmp[8],
        branch=branch,
        course_code=course_code,
        academic_year=academic_year,
        sem=sem
    )
    obj2.save()

    per = []

    # Calculate the percentage of students who attained the CO for each question
    for i in range(9):
        try:
            per.append(round(val[i] / atmp[i] * 100, 2))
        except ZeroDivisionError:
            per.append(0)

    # Insert data into 'v20cpl5' model for percentage
    obj3 = t1.objects.create(
        at_atmp_per='percentage',
        co1q1a=per[0],
        co1q1b=per[1],
        co1q1c=per[2],
        co2q2a=per[3],
        co2q2b=per[4],
        co2q2c=per[5],
        co3q3a=per[6],
        co3q3b=per[7],
        co3q3c=per[8],
        branch=branch,
        course_code=course_code,
        academic_year=academic_year,
        sem=sem
    )
    obj3.save()

    l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    per2 = []

    # Calculate the average percentage of each CO
    for i in l:
        c = 3 if per[i[2]] != 0 else 2
        per2.append(round((per[i[0]] + per[i[1]] + per[i[2]]) / c, 2))

    # Insert data into 'v20_avg_att' model
    T2 = ModelSchema.objects.get(name='v20_avg_att')
    t2 = T2.as_model()
    obj4 = t2.objects.create(
        per_lvl='percentage',
        co1=per2[0],
        co2=per2[1],
        co3=per2[2],
        branch=branch,
        course_code=course_code,
        academic_year=academic_year,
        sem=sem
    )
    obj4.save()

    pvl = []

    # Determine the performance level for each CO
    for i in range(3):
        obj = t3.objects.get(co='co'+str(i+1), branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
        el = 1 if per2[i] >= obj.tpl1 else 2 if per2[i] >= obj.tpl2 else 3 if per2[i] >= obj.tpl3 else 0
        pvl.append(el)

    # Insert data into 'v20_avg_att' model for performance level
    obj5 = t2.objects.create(
        per_lvl='pvl',
        co1=pvl[0],
        co2=pvl[1],
        co3=pvl[2],
        branch=branch,
        course_code=course_code,
        academic_year=academic_year,
        sem=sem
    )
    obj5.save()

def storeinput(request):
    """
    This function handles the storing of input data from the user.
    It takes the input Excel file, passes it to the 'data_insert' function,
    and redirects to the login page.
    """
    if request.method == 'POST':
        nm = request.POST['myfile']
        name = r'{}'.format(nm[1:-1])
        name1 = name.replace("\\", '/')
        data_insert(name1)
    else:
        return redirect('login')

    return render(request, 'storeinput.html')

def dy_test():
    """
    This function creates a dynamic model schema 'test1' and its corresponding model 'test1'.
    It adds three integer fields to the model.
    """
    book_schema = ModelSchema.objects.create(name='test1')
    lst = ['co1', 'co2', 'co3']
    for i in range(3):
        lst[i] = FieldSchema.objects.create(
            name=lst[i],
            data_type='integer',
            model_schema=book_schema,
            max_length=255,
        )
    Book = book_schema.as_model()

def prac():
    """
    This function creates an instance of the 'test1' model and saves it with field values.
    """
    T3 = ModelSchema.objects.get(name='test1')
    t3 = T3.as_model()
    obj = t3()
    lst = ['co'+str(i) for i in range(1, 4)]
    val = [4, 5, 6]
    for i, field_name in enumerate(lst):
        setattr(obj, field_name, val[i])
    obj.save()

def index(request):
    """
    This function serves as the view for the index page.
    It can be used to trigger various functions related to dynamic models.
    """
    return render(request, 'index.html')

def uplod(request):
    """
    This function serves as the view for the upload page.
    """
    return render(request, 'uplod.html')

def sem_avg_att_per():
    """
    This function creates a dynamic model schema 'sem_v20_avg_att' and its corresponding model 'sem_v20_avg_att'.
    It adds fields for percentage levels of each CO.
    """
    book_schema = ModelSchema.objects.create(name='sem_v20_avg_att')
    attain = FieldSchema.objects.create(
        name='per_lvl',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    lst = ['co1', 'co2', 'co3', 'co4', 'co5']
    for i in range(5):
        lst[i] = FieldSchema.objects.create(
            name=lst[i],
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

def sem_mid1_attain1():
    """
    This function creates a dynamic model schema 'sem_v20cpl5' and its corresponding model 'sem_v20cpl5'.
    It adds fields for attainment levels of each CO for each question.
    """
    book_schema = ModelSchema.objects.create(name='sem_v20cpl5')
    attain = FieldSchema.objects.create(
        name='at_atmp_per',
        data_type='character',
        model_schema=book_schema,
        max_length=255,
    )
    c = 0
    lst = ['a'+str(i) for i in range(9)]
    alp = ['a', 'b', 'c']
    for i in range(3):
        for j in range(3):
            lst[c] = FieldSchema.objects.create(
                name='co'+str(i+1)+'q'+str(i+1)+alp[j],
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1

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

# Additional functions and views have been omitted for brevity.
def sem_call():
    """
    This function creates a dynamic model schema 'V20sem2' and its corresponding model 'V20sem2'.
    It adds fields for each question in the format 'qXa', 'qXb', 'qXc' (X represents the question number).
    """
    book_schema = ModelSchema.objects.create(name='V20sem2')
    q = 'q'
    alp = ['a', 'b', 'c']

    # Add fields to the schema
    lst = ['a'+str(i) for i in range(15)]
    c = 0
    sno = FieldSchema.objects.create(
        name='Roll_no',
        data_type='integer',
        model_schema=book_schema,
        max_length=255,
    )
    for i in range(5):
        for j in range(3):
            lst[c] = FieldSchema.objects.create(
                name=q+str(i+1)+alp[j],
                data_type='integer',
                model_schema=book_schema,
                max_length=255,
            )
            c += 1

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


def sem_data_insert():
    """
    This function inserts data into the 'V20sem2' model based on the provided Excel file.
    It calculates various values and inserts them into the corresponding models.
    """
    book_schema = ModelSchema.objects.get(name='V20sem2')
    Book = book_schema.as_model()
    
    df1 = pd.read_excel("D:/obesem.xlsx")
    df = df1[5:]
    df2 = df1[3:4]
    
    df = df.fillna(-1)
    df = df.replace('A', -2)
    df.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15']
    df2.columns = ['sn', 'rno', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15']
    
    branch = 'CSE'
    course_code = 'V20qwer'
    academic_year = '2021-22'
    sem = 'IV'
    val = []
    lst = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15']
    
    T3 = ModelSchema.objects.get(name='V20cpl1')
    t3 = T3.as_model()
    max_per = []
    
    for i in range(5):
        obj = t3.objects.get(co='co'+str(i+1), branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
        max_per.append(obj.pl)

    for i in range(15):
        df[lst[i]] = pd.to_numeric(df[lst[i]])
        mxp = max_per[0] if i <= 2 else max_per[1] if i <= 5 else max_per[2] if i <= 8 else max_per[3] if i <= 11 else max_per[4]
        l = len(df[df[lst[i]] >= math.ceil((df2.at[3, lst[i]] * mxp) / 100)])
        val.append(l)
    
    atmp = []
    for i in range(15):
        df[lst[i]] = pd.to_numeric(df[lst[i]])
        l = len(df[df[lst[i]] >= 0])
        atmp.append(l)
   
    for i in df.index:
        f = Book.objects.create(roll_no=df['sn'][i], q1a=df['q1'][i], q1b=df['q2'][i], q1c=df['q3'][i], q2a=df['q4'][i], q2b=df['q5'][i], q2c=df['q6'][i], q3a=df['q7'][i], q3b=df['q8'][i], q3c=df['q9'][i], q4a=df['q10'][i], q4b=df['q11'][i], q4c=df['q12'][i], q5a=df['q13'][i], q5b=df['q14'][i], q5c=df['q15'][i], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
        f.save()
    
    T1 = ModelSchema.objects.get(name='sem_v20cpl5')
    t1 = T1.as_model()
    obj1 = t1.objects.create(at_atmp_per='attained', co1q1a=val[0], co1q1b=val[1], co1q1c=val[2], co2q2a=val[3], co2q2b=val[4], co2q2c=val[5], co3q3a=val[6], co3q3b=val[7], co3q3c=val[8], co4q4a=val[9], co4q4b=val[10], co4q4c=val[11], co5q5a=val[12], co5q5b=val[13], co5q5c=val[14], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
    obj1.save()
    
    obj2 = t1.objects.create(at_atmp_per='attempted', co1q1a=atmp[0], co1q1b=atmp[1], co1q1c=atmp[2], co2q2a=atmp[3], co2q2b=atmp[4], co2q2c=atmp[5], co3q3a=atmp[6], co3q3b=atmp[7], co3q3c=atmp[8], co4q4a=atmp[9], co4q4b=atmp[10], co4q4c=atmp[11], co5q5a=atmp[12], co5q5b=atmp[13], co5q5c=atmp[14], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
    obj2.save()

    per = []
    for i in range(15):
        try:
            per.append(round(val[i] / atmp[i] * 100, 2))
        except ZeroDivisionError:
            per.append(0)
    
    obj3 = t1.objects.create(at_atmp_per='percentage', co1q1a=per[0], co1q1b=per[1], co1q1c=per[2], co2q2a=per[3], co2q2b=per[4], co2q2c=per[5], co3q3a=per[6], co3q3b=per[7], co3q3c=per[8], co4q4a=per[9], co4q4b=per[10], co4q4c=per[11], co5q5a=per[12], co5q5b=per[13], co5q5c=per[14], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
    obj3.save()
    
    l = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
    per2 = []
    for i in l:
        c = 3 if per[i[2]] != 0 else 2
        per2.append(round((per[i[0]] + per[i[1]] + per[i[2]]) / c, 2))
    
    T2 = ModelSchema.objects.get(name='sem_v20_avg_att')
    t2 = T2.as_model()
    obj4 = t2.objects.create(per_lvl='percentage', co1=per2[0], co2=per2[1], co3=per2[2], co4=per2[3], co5=per2[4], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
    obj4.save()
    
    pvl = []
    for i in range(5):
        obj = t3.objects.get(co='co'+str(i+1), branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
        el = 1 if per2[i] >= obj.tpl1 else 2 if per2[i] >= obj.tpl2 else 3 if per2[i] >= obj.tpl3 else 0
        pvl.append(el)
    
    obj5 = t2.objects.create(per_lvl='pvl', co1=pvl[0], co2=pvl[1], co3=pvl[2], co4=pvl[3], co5=pvl[4], branch=branch, course_code=course_code, academic_year=academic_year, sem=sem)
    obj5.save()
