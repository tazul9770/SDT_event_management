from django.urls import path
from user.views import register, log_out, active_user, user_list, assign_role, create_group, group_list, delete_group, delete_user
from user.views import ProfileView, LoginUser
from django.contrib.auth.views import LogoutView

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
    path('profile/', ProfileView.as_view(), name='profile')
]
