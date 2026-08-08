from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegistrationForm, LoginForm, AssignRoleForm, CreateGroupForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm, EditProfileForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            messages.success(request, "A confirmation mail send. Please check your email!")
            return redirect('register')
    return render(request, 'authentication/register.html', {'form':form})

"""This is user login function based view """
# def log_in(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     return render(request, 'authentication/login.html', {'form':form})

"""This is user login class based view """
class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else super().get_success_url()

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def active_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Inavalid id or token")
    except User.DoesNotExist:
        return HttpResponse("User does not found")
    
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin/user_list.html', {'users':users})

def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()
    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear() # remove old group
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('assign_role', user_id=user.id)
    return render(request, 'admin/assign_role.html', {'form':form})

def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('create_group')
    return render(request, 'admin/create_group.html', {'form':form})

def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'admin/group_list.html', {'groups':groups})

def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    messages.success(request, f'{group.name} deleted successfully')
    return redirect('group_list')

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully")
    return redirect('user_list')

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['username'] = user.username
        context['email'] = user.email
        context['name'] = user.get_full_name()

        context['member_since'] = user.date_joined
        context['last_login'] = user.last_login
        context['status'] = user.is_active
        context['designation'] = user.designation
        context['designation_title'] = user.designation_related_something
        context['image'] = user.image
        context['location'] = user.location
        context['bio'] = user.bio

        return context

class ChangePassword(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html'

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('login')
    html_email_template_name = 'authentication/reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'https' if self.request.is_secure() else 'http'
        context['domain'] = self.request.get_host()
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'A Reset email sent. Please check your email')
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'authentication/password_reset.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(
            self.request, 'Password reset successfully')
        return super().form_valid(form)

class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/update_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your profile has been updated successfully.")
        return redirect('profile')
    
class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'home.html'
    #context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        contact = form.instance
        send_mail(
            subject=f"New contact message from {contact.name}",
            message=f"Email: {contact.email}\nMessage: \n{contact.message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['tazulislam42609770@gmail.com'],
            fail_silently=False
        )
        send_mail(
            subject="Thanks for messaging us",
            message="We have received your message. Our team will contact you soon.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[contact.email],
            fail_silently=False
        )
        return response
    