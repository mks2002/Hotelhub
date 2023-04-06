from django.shortcuts import render
from django.http import HttpResponseRedirect
from bookings.models import Bookinghotel
from payments.models import Paymentdetail

from django.contrib import messages
from operator import not_
# Create your views here.


# session__id
# order_id


# this is for payment form page ..

from django.views.decorators.cache import never_cache
from django.core.exceptions import ObjectDoesNotExist


@never_cache
def paymentpage(request):
    id = request.GET.get('session__id')
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session and 'user_{}_uemail'.format(id) not in request.session and 'user_{}_uemail'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session:
        data = {}
        if request.method == "GET":
            id = request.GET.get('session__id')
            oid = request.GET.get('order_id')
            try:
                maindata = Bookinghotel.objects.get(id=oid)
            except ObjectDoesNotExist:
                messages.error(
                    request, 'the page you currrently looking for is not available..')
                url = "/dashboard/{}".format(id)
                data1 = {'id': id, 'url': url}
                return render(request, 'error_page.html', data1)
            if maindata.payment_status == 'paid':
                url = "/dashboard/{}".format(id)
                return HttpResponseRedirect(url)
            else:
                cost = request.GET.get('cost')
                # maindata = Bookinghotel.objects.get(id=oid)
                un = maindata.username
                email = maindata.useremail
                pw = maindata.userpassword
                url = "/dashboard/{}".format(id)
                data = {'id': id, 'url': url, 'un': un, 'uemail': email,
                        'pw': pw, 'cost': cost, 'oid': oid}
                return render(request, 'payment.html', data)

        try:
            if request.method == "POST":
                uname = request.POST.get('username')
                upass = request.POST.get('password')
                order_no = request.POST.get('order_no')
                total_cost = request.POST.get('total_cost')
                email = request.POST.get('email')

                # this are get method variable....
                id = request.GET.get('session__id')
                oid = request.GET.get('order_id')
                cost = request.GET.get('cost')
                maindata = Bookinghotel.objects.get(id=oid)
                un = maindata.username
                pw = maindata.userpassword

                full_name = (maindata.firstname + ' ' +
                             maindata.lastname).upper()
                url = "/dashboard/{}".format(id)

                data1 = Paymentdetail(
                    username=uname, password=upass, useremail=email, order_no=order_no, total_cost=cost)
                data1.save()
                Bookinghotel.objects.filter(
                    id=order_no).update(payment_status='paid')

                data = {'id': id, 'url': url}
                messages.success(
                    request, f'your payment has been done successfully for the order of mr. {full_name} !')
                response = HttpResponseRedirect(url)
                return response
        except Exception as e:
            pass
    return render(request, 'payment.html', data)
