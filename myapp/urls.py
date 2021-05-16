from django.urls import path
from myapp.views import HomeView, SignupView, LoginView, AboutView, ServiceView, user_logout, FaqView, SettingsView, ContactView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServiceView.as_view(), name='services'),
    path('faq', FaqView.as_view(), name='faq'),
    path('setting', SettingsView.as_view(), name='setting'),
    path('contact', ContactView.as_view(), name='contact'),
    path('user_logout', user_logout, name='user_logout')
]
