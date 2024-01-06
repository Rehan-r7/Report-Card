from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages #to display messages
from django.contrib.auth import authenticate , login , logout #returns True if username and password are are correct
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator #divides data into different pages depending
# Create your views here.

from django.db.models import Q , Sum # for or operations 

def home(request):
    return render(request,'report/index.html')

def get_students(request):
    
    queryset = Student.objects.all()
    
    if request.GET.get('search') :
        search = request.GET.get('search')
        queryset = queryset.filter(
            
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) 
            
        )
        
    paginator = Paginator(queryset, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page" , 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(request, 'report/students.html' , {'queryset' : page_obj} )

from .seed import generate_report_card
def see_marks(request , student_id):

    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    
    return render(request, 'report/see_marks.html' , {'queryset' : queryset, 'total_marks' : total_marks } )
    
    