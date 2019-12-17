from django.shortcuts import render, redirect
from django.contrib import messages
from profilestorer.settings import EMAIL_HOST_USER
from django.conf import settings
from .forms import SignUpForm, AddPeopleForm, LoginForm, EditProfileForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


def home(request):
   return render(request, 'company/home.html' , {'title':'profilestorer'})

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
            form = SignUpForm(request.POST)
            email = request.POST['email']
            new_password = get_random_string(length=8)


            if User.objects.filter(email=email).exists():
                messages.success(request, f'email  already taken')
            else:

                subject = 'Login password '
                message = 'enter this  password for login    ' + new_password
                recepient = request.POST['email']
                send_mail(subject,
                    message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                user = User.objects.create(email = email, password=new_password )
                user.save()
                messages.success(request, f'Your account has been created! Check your email  for login')
                return redirect('company-login')


    else:
        form = SignUpForm()
    return render(request, 'company/register.html', {'form':form})




# def edit_profile(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method  == 'POST':
#         user = User.objects.create(name=request.POST.get('name'),phone=request.POST.get('phone'),
#                                 gender=request.POST.get('gender'),hobbies=request.POST.get('hobbies'),profile_picture=request.POST.get('profile_picture'))
#         user.save()
#         messages.success(request, f'details are updated login again to check')
#         return redirect('company-home')
#
#     return render(request,'company/edit_profile.html',{'user':user, 'form': form})
#
#
# def detail(request,pk):
#     details = get_object_or_404(User, pk=pk)         #it will create object
#     return render(request, 'company/detail.html',{'details':details})

def login(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)   # get will fetch details from database and it will match value with post

        if user.password == password:

            if user.type == 'Manager':
                return redirect('company-add')

            if user.type == 'Normal':
                #print('hobbies : ', user.hobbies)
                return redirect('detail',pk=user.id)
                # return detail(request,user)
        else:
            messages.success(request, 'invalids credentials')
            return redirect('company-login')

    else:
        return render(request, 'company/login.html')

def add(request):
    form = AddPeopleForm()
    if request.method == 'POST':
            form = AddPeopleForm(request.POST)
            email = request.POST['email']
            new_password = get_random_string(length=8)


            if User.objects.filter(email=email).exists():
                messages.success(request, f'email  already taken')
            else:

                subject = 'Login password '
                message = 'enter this  password for login    ' + new_password
                recepient = request.POST['email']
                send_mail(subject,
                    message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                user = User.objects.create(email = email, password=new_password, name=request.POST['name'], type=request.POST.get('type'))
                user.save()
                messages.success(request, f'Your account has been created! Check your email  for login')
                return redirect('company-home')
    return render(request, 'company/add.html', {'form':form})


def member_list(request):
    queryset = User.objects.all()
    context = {
            'object_list' : queryset,
            'title': 'List'
        }
    return render(request, 'company/list.html', context)

def member_detail(request, id):
    instance = get_object_or_404(User, id=id)
    context = {
        'name': instance.name,
        'instance': instance,
    }
    return render(request, 'company/member_detail.html', context)

def member_update(request, id=None):
    instance = get_object_or_404(User, id=id)
    form = EditProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance  = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())

    context ={
        'name': instance.name,
        'instance': instance,
        "form":form,
    }
    return render(request, 'company/edit_profile.html', context)



# class UserDetailView(DetailView):
#      model = User
#
#      def get(self, request, *args, **kwargs):
#         user = get_object_or_404(User, pk=kwargs['user_id'])
#         context = {'details':user }
#         return render(request, 'company/detail.html', context)
#
# class UserUpdateView(UpdateView):
#     model = User
#
#     fields = ('name', 'phone', 'gender', 'hobbies', 'profile_picture')
#     template_name = 'company/edit_profile.html'
#     success_url ='company/detail.html'
