from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from accounts.models import Userprofile
from django.db.models import Count

from django.contrib.auth.models import User
from .views import *


@login_required
def home(request):
	if request.method == 'POST':
		if 'referal' in request.POST:
			rr = Userprofile()
			rr.refer = request.POST['referal']
			rr.username = request.POST['user']
			rr.save()
			return redirect('tree')
	return render(request, "home.html", {})

@login_required
def tree_view(request):
    data = Userprofile.objects.all()
    w_data = Userprofile.objects.filter(refer=request.user)
    count_w_data = Userprofile.objects.filter(refer=request.user).count()
    q_data = []
    for p in w_data:
    	q_data += Userprofile.objects.filter(refer=p.username)
    wallet = count_w_data + len(q_data)
    amt = 1000+wallet*1000/2

    context = {'data': data, 'wallet': wallet, 'amt': amt}
    return render(request, "tree.html" , context)

def index(request):
	return render(request, 'base.html')