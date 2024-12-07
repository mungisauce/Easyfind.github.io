import os
from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from Attendance.forms import AttendanceForm, UserLoginForm, AccountForm
from Attendance.models import Contact


def base(request):
    return render(request, 'base.html')


def attendance_records(request):
    return render(request, 'attendance_records.html')


def mark_attendance(request):
    return render(request, 'mark_attendance.html')


def worker_list(request):

    return render(request, 'worker_list.html')







def blog(request):
    return render(request,'blog.html')





def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect( 'https://www.thetalentcabin.com//')

            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login_view.html',{'form':form})



def signup(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = AccountForm()
    return render(request, 'signup.html',{'form':form})




def contact(request):
    if request.method == "POST":
     form = AttendanceForm(request.POST,request.FILES)
     if form.is_valid():
        form.save()
        return redirect('about')
    else:
        form = AttendanceForm()
    return render(request, 'contact.html', {'form': form})
def about(request):
    data =Contact.objects.all()
    context = {'data': data}
    return render(request, 'about.html',context)
def update(request,id):
    attendance = get_object_or_404(Contact,id=id)
    if request.method == "POST":
        form = AttendanceForm(request.POST,request.FILES,instance=attendance)
        if form.is_valid():
            form.save()
            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, f'Customer updated successfully! {file_name} uploaded')
            else:
                messages.error(request, f'Customer updated successfully!')
                return redirect('about')
        else:
            messages.error(request, f'Please confirm your changes!')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'update.html', {'form': form, 'attendance': attendance})


def delete(request,id ):
    attendance = get_object_or_404(Contact,id=id)
    try:
        attendance.delete()
        messages.success(request, 'User deleted successfully!')
    except Exception as e:
        messages.error(request, 'User not deleted')
    return redirect('about')
