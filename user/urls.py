from django.urls import path
from user.views import register, log_out, active_user, user_list, assign_role, create_group, group_list, delete_group, delete_user
from user.views import ProfileView, LoginUser, ChangePassword, CustomPasswordResetView, CustomPasswordResetConfirmView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('register/', register, name='register'),
    #path('login/', log_in, name='login'),
    path('login/', LoginUser.as_view(), name='login'),
    #path('logout/', log_out, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('active/<int:user_id>/<str:token>/', active_user),
    path('user_list/', user_list, name='user_list'), 
    path('assign_role/<int:user_id>/', assign_role, name='assign_role'),
    path('create_group/', create_group, name='create_group'),
    path('group_list/', group_list, name='group_list'),
    path('delete_group/<int:group_id>/', delete_group, name='delete_group'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change_password/', ChangePassword.as_view(), name='change-password'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
