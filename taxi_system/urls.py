from django.urls import path
from .import views



app_name = 'taxi_system'

urlpatterns = [
	path('',views.index, name='index'),
	path('about/',views.about, name='about'),
	path('cars/',views.cars, name='cars'),
	path('contact/',views.contact, name='contact'),
	path('services/',views.HomeView.as_view(),name="services"),

]	