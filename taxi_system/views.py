from django.shortcuts import render
from  .models import*
from django.views.generic import ListView,DetailView
from .models import Post
# import telebot

# me = 696007117
# TOKEN = ''
# bot = telebot.Teleobot(TOKEN)
class HomeView(ListView):
	model = Post
	template_name = 'services.html'

class ServicesListView(ListView):
	model = Post
	template_name = 'reviews.html'	

def index(request):
	if request.method == 'POST':
		n = request.POST['Name']
		e = request.POST['Email']
		qayerdan  = request.POST['From']
		qayergacha = request.POST['To']
		t = request.POST['Time']
		d = request.POST['Date']
		m = request.POST['Message']
		a = request.POST['Adults']
		ch = request.POST['Children']
		c = request.POST['Comfort']
		Buyurtmalar.objects.create(name=n, email=e,qayerdan=qayerdan, qayergacha=qayergacha,time=t,date=d, message=m,adults=a,children=ch,comfort=c,)
		print('#'*50)
	else:
		print('error'*10)	
	return render(request,'index.html')


def contact(request):
	if request.method == 'POST':
		n = request.POST['name']
		e = request.POST['email']
		p = request.POST['phone']
		m = request.POST['message']
		contact.objects.create(name=n, email=e,phone=p, message=m,)
		print('*'*50)
	else:
		print('#'*10)	

	return render(request,'contact.html')
def about(request):
	
	return render(request,'about.html')
def cars(request):
	
	return render(request,'cars.html')
def services(request):

	return render(request,'services.html')	