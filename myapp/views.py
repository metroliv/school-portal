from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Category, Post, Article, Staff, UserProfile
from .forms import UserSettingsForm, StaffForm, UserProfileForm
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import Room


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.html"
                    reset_url = reverse('password_reset_confirm', kwargs={
                        'uidb64': user.id,
                        'token': 'token'  # Replace with a valid token generation method
                    })
                    message = f"Click the link below to reset your password:\n\n{request.build_absolute_uri(reset_url)}"
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                messages.success(request, 'An email has been sent with instructions to reset your password.')
                return redirect('password_reset_done')
            messages.error(request, 'No user found with that email address.')
            return redirect('password_reset')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

def help(request):
    return render(request, 'help.html')

def counter(request):
    return render(request, 'counter.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'article_list.html', {'articles': articles})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('/')
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def chat_room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })


def my_model(request):
    return render(request, 'MyModel.html')

@login_required
def user_settings(request):
    user = request.user
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully.')
            return redirect('user_settings')
    else:
        form = UserSettingsForm(instance=user)

    return render(request, 'user_settings.html', {'form': form})

@login_required
def staff_list(request):
    staffs = Staff.objects.all()
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()

    return render(request, 'staff_list.html', {'staffs': staffs, 'form': form})

@login_required
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})

@login_required
def staff_create(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()

    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff updated successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)

    return render(request, 'staff_form.html', {'form': form})

@login_required
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        staff.delete()
        messages.success(request, 'Staff deleted successfully.')
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profiles/profile.html', {'form': form})
