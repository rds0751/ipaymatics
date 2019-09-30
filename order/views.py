from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpRequest, Http404
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import reverse
from payu.utils import generate_hash, verify_hash
from accounts.models import *

from django.contrib.auth.models import User

from payu.forms import PayUForm
from order.forms import OrderForm

from uuid import uuid4
from random import randint
import logging

logger = logging.getLogger('django')

def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            user = request.user
            user = User.objects.get(username=user)
            initial = order_form.cleaned_data
            initial.update({'key': settings.PAYU_INFO['merchant_key'],
                            'surl': request.build_absolute_uri(reverse('order:success')),
                            'furl': request.build_absolute_uri(reverse('order:success')),
                            'service_provider': 'payu_paisa',
                            'firstname': user.first_name,
                            'email': user.email,
                            'curl': request.build_absolute_uri(reverse('order:cancel'))})
            # Once you have all the information that you need to submit to payu
            # create a payu_form, validate it and render response using
            # template provided by PayU.
            initial.update({'hash': generate_hash(initial)})
            payu_form = PayUForm(initial)

            if payu_form.is_valid():
                context = {'form': payu_form,'action': "%s" % settings.PAYU_INFO['payment_url']}
                return render(request, 'payu_form.html', context)
            else:
                logger.error('Something went wrong! Looks like initial data\
                        used for payu_form is failing validation')
                return HttpResponse(status=500)
    else:
        initial = {'txnid': uuid4().hex,
                'productinfo': 'package',
                'amount': randint(100, 1000)/100.0}
        order_form = OrderForm(initial=initial)
    context = {'form': order_form}
    return render(request, 'checkout.html', context)

import hashlib
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_protect
@csrf_exempt
def success(request):
	if request.method == 'POST':
		if 'status' in request.POST:
			c = {}
			c.update(csrf(request))
			status=request.POST["status"]
			firstname=request.POST["firstname"]
			amount=request.POST["amount"]
			txnid=request.POST["txnid"]
			posted_hash=request.POST["hash"]
			key=request.POST["key"]
			productinfo=request.POST["productinfo"]
			email=request.POST["email"]
			salt=settings.PAYU_INFO['merchant_salt']
			data = request.POST
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq.encode('utf-8')).hexdigest().lower()
	if(hashh !=posted_hash):
		print("Invalid Transaction. Please try again")
	else:
		print("Thank You. Your order status is ", status)
		print("Your Transaction ID for this transaction is ",txnid)
		print("We have received a payment of Rs. ", amount ,". Your order will soon be shipped.")

	context = {"txnid":txnid,"status":status,"amount":amount, 'data':data}
	return render(request, 'sucess.html', context)


def failure(request):
    if request.method == 'POST':
        return render(request, 'failure.html')
    else:
        raise Http404

def cancel(request):
    if request.method == 'POST':
        return render(request, 'cancel.html')
    else:
        raise Http404