
from django.urls import path
from app_booking import views
from django.conf import settings # ++
from django.conf.urls.static import static #++

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),


    path('appointments/', views.appo_list, name='appointments'),
    path('booking/', views.booking_page, name='booking'),

    path('department/', views.department_page, name='department'),
    path('doctors/', views.doctors_page, name='doctors'),
    path('aboutus/', views.aboutus_page, name='aboutus'),
    path('contactus/', views.contactus_page, name='contactus'),

    path('login/', views.Login, name='login'),
    path('logout/', views.logout_user, name='logout'),
                  # path('signup/', views.signup, name='signup'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# add this to get images
