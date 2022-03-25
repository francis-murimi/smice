from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


app_name = 'home'
urlpatterns = [
    path('',views.home,name = 'home'),
    path('documentation/',views.documentation,name='documentation'),
    path('contact/',views.contact,name='contact'),
    #path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out'),
    path('account/',views.account,name='account'),
    #orders
    path('order_view/',views.order_view,name='order_view'),
    path('order/<int:id>/',views.order_see,name='order_see'),
    #password reset views
    #password.html contains form for email,email_template is template shown in email
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='home/password.html',email_template_name='home/email.html',success_url=reverse_lazy('home:password_reset_done')),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html.',success_url=reverse_lazy('home:password_reset_complete')),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),name='password_reset_complete'),
    ]