# import all basic rendering and redirecting modules...
from django.shortcuts import redirect

from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import date
from datetime import datetime as dt

# this are all our models which we used in this section..

from bookings.models import Bookinghotel, Query
from payments.models import Paymentdetail
from hotellist.models import Hotellist

from mainapp.models import Login
from django.contrib import messages

# this we install for if there is some error then we can change our custom error page with django default error page...
from django.core.exceptions import ObjectDoesNotExist


# this is the booking form page.....
@never_cache
def bookings(request, id):
    if (
        f'user_{id}_uname' not in request.session
        and f'user_{id}_upass' not in request.session
        and f'user_{id}_uemail' not in request.session
    ):
        return HttpResponseRedirect('/login/')
    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        data1 = {}
        if request.method == 'GET':
            un1 = request.session.get(f'user_{id}_uname')
            email1 = request.session.get(f'user_{id}_uemail')
            password1 = request.session.get(f'user_{id}_upass')
            hname1 = request.GET.get('hname')
            hcity1 = request.GET.get('hcity')
            hstate1 = request.GET.get('hstate')
            hcost1 = request.GET.get('hcost')
            image = request.GET.get('image_url')
            if any(val is None for val in [hname1, hcity1, hstate1, hcost1, image]):
                messages.error(
                    request,
                    'Invailed url the page you are looking for is not available...',
                )
                url = f'/dashboard/{id}'
                data1 = {'id': id, 'url': url}
                return render(request, 'error_page.html', data1)
            else:
                prefix_to_remove = '/media/'
                result_image = image[len(prefix_to_remove) :]
                if Hotellist.objects.filter(
                    name=hname1,
                    city=hcity1,
                    state=hstate1,
                    current_cost=hcost1,
                    image=result_image,
                ).exists():
                    url = '/dashboard/{}'.format(id)
                    data1 = {
                        'un1': un1,'pw1': password1,'em1': email1,'hname1': hname1,'hcity1': hcity1,'hstate1':   hstate1,'hcost1': hcost1,'url': url,'id': id,'image': image,
                    }
                    return render(request, 'booking.html', data1)
                else:
                    messages.error(
                        request,
                        'Invailed url the page you are looking for is not available...',
                    )
                    url = f'/dashboard/{id}'
                    data1 = {'id': id, 'url': url}
                    return render(request, 'error_page.html', data1)

        try:
            if request.method == 'POST':
                name = request.POST.get('name')
                last = request.POST.get('last')
                email = request.POST.get('email')
                contact = request.POST.get('contact')
                person = request.POST.get('person')
                room = request.POST.get('room')
                start = request.POST.get('startdate')
                end = request.POST.get('lastdate')

                # these are hidden fields .....
                username = request.POST.get('username')
                useremail = request.POST.get('useremail')
                password = request.POST.get('password')

                hotelname = request.POST.get('hotelname')
                hotelcity = request.POST.get('hotelcity')
                hotelstate = request.POST.get('hotelstate')
                hotelcost = request.POST.get('hotelcost')

                # these are all the get method variable....
                un1 = request.session.get(f'user_{id}_uname')
                email1 = request.session.get(f'user_{id}_uemail')
                password1 = request.session.get(f'user_{id}_upass')
                hname1 = request.GET.get('hname')
                hcity1 = request.GET.get('hcity')
                hstate1 = request.GET.get('hstate')
                hcost1 = request.GET.get('hcost')
                image = request.GET.get('image_url')
                
                url = f'/dashboard/{id}'
                data1 = {'un1': un1,'pw1': password1,'em1': email1,'hname1': hname1,'hcity1': hcity1,'hstate1': hstate1,'hcost1': hcost1,'url': url,'id': id,'image': image,}
             
                
                if start < str(date.today()):
                    messages.warning(request, 'Your starting date must be equal or more than today !')
                    return render(request, 'booking.html', data1)
                elif start > end:
                    messages.warning( request, 'your ending date must be more than start date !')
                    return render(request, 'booking.html', data1)
                else:
                    data = Bookinghotel(
                        firstname=name,
                        lastname=last,
                        email=email,
                        contact_no=contact,
                        no_people=person,
                        username=username,
                        useremail=useremail,
                        no_rooms=room,
                        userpassword=password,
                        start=start,
                        end=end,
                        hotelname=hotelname,
                        city=hotelcity,
                        state=hotelstate,
                        current_cost=hotelcost,
                    )
                    data.save()
                    url = '/dashboard/{}'.format(id)
                    full_name = (name + ' ' + last).upper()
                    data1 = {'url': url, 'id': id}

                    # this is for redirecting into the dashboard page ...
                    response = HttpResponseRedirect(url)
                    messages.success(
                        request,
                        f'Your booking has been done for mr. {full_name}. You can see your order details below !',
                    )
                    return response
        except Exception as e:
            pass
    return render(request, 'booking.html', data1)


# this is dashboard page.....
@never_cache
def dashboard(request, id):
    if (
        'user_{}_uname'.format(id) not in request.session
        and 'user_{}_upass'.format(id) not in request.session
        and 'user_{}_uemail'.format(id) not in request.session
    ):
        return HttpResponseRedirect('/login/')
    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        data = {}
        username = request.session['user_{}_uname'.format(id)]
        useremail = request.session['user_{}_uemail'.format(id)]
        password = request.session['user_{}_upass'.format(id)]
        if Login.objects.filter(
            username=username, email=useremail, password=password
        ).exists():
            tabel = Bookinghotel.objects.filter(
                username=username, userpassword=password
            )
            queries=Query.objects.filter(username=username,useremail=useremail)
            hotelurl = '/hotellist/{}/{}'.format('all', id)
            reviewurl = '/review/{}'.format(id)
            # this url is for dashboard page itself ....
            url = '/dashboard/{}'.format(id)
            data = {
                'un': username,
                'uem': useremail,
                'pw': password,
                'id': id,
                'maindata': tabel,
                'querydata':queries,
                'hotelurl': hotelurl,
                'reviewurl': reviewurl,
                'url': url,
            }
            return render(request, 'dashboard.html', data)
        return render(request, 'dashboard.html', data)


# this is for order details page.....


@never_cache
def details(request):
    id = request.GET.get('session__id')
    if (
        'user_{}_uname'.format(id) not in request.session
        and 'user_{}_upass'.format(id) not in request.session
        and 'user_{}_uemail'.format(id) not in request.session
    ):
        return HttpResponseRedirect('/login/')
    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        data = {}
        if request.method == 'GET':
            id = request.GET.get('session__id')
            detail_id = request.GET.get('id1')

            un = request.session['user_{}_uname'.format(id)]
            uemail = request.session['user_{}_uemail'.format(id)]
            password = request.session['user_{}_upass'.format(id)]

            url = '/dashboard/{}'.format(id)
            # this is we do for override the django default error page by our custom message if we want we can change it by our custom error page also.....
            try:
                maindata = Bookinghotel.objects.get(id=detail_id)
            except ObjectDoesNotExist:
                messages.error(
                    request, 'the page you currrently looking for is not available..'
                )
                data1 = {'id': id, 'url': url}
                return render(request, 'error_page.html', data1)

            print(maindata)
            bool = maindata.payment_status.lower() == 'unpaid'
            start = str(maindata.start)
            end = str(maindata.end)
            res = (dt.strptime(end, '%Y-%m-%d') - dt.strptime(start, '%Y-%m-%d')).days
            total_cost = res * maindata.current_cost * maindata.no_rooms
            data = {
                'un': un,
                'pw': password,
                'uemail': uemail,
                'maindata': maindata,
                'url': url,
                'cost': total_cost,
                'id': id,
                'bool': bool,
                'order_id': detail_id,
                'bool': bool,
            }
            return render(request, 'order_details.html', data)

        return render(request, 'order_details.html', data)


# in each page context we have to pass the id value because it is the session key variable so we use this so that we can check if someone is logged in or logged out ...

@never_cache
def delete_confirmation(request):
    id=request.GET.get('session__id')
    if (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        
        url = '/dashboard/{}'.format(id)
        orderid=request.GET.get('id1')
        if Bookinghotel.objects.filter(id=orderid).exists():
            data={'id':id,'orderid':orderid,'url':url}
            return render(request,'delete_confirmation.html',data)
        else:
            messages.error(request, 'the page you currrently looking for is not available..')
            data1 = {'id': id, 'url': url}
            return render(request, 'error_page.html', data1)
            # return HttpResponseRedirect(url)
    else:
         return HttpResponseRedirect('/login/')
        
    
    


# this page is for deleting the order......
@never_cache
def delete(request):
    id = request.GET.get('session__id')
    if (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        id1 = request.GET.get('id1')
        id = request.GET.get('session__id')
        customer_name = (
            Bookinghotel.objects.get(id=id1).firstname
            + ' '
            + Bookinghotel.objects.get(id=id1).lastname
        )
        Bookinghotel.objects.filter(id=id1).delete()
        Paymentdetail.objects.filter(order_no=id1).delete()
        url = '/dashboard/{}'.format(id)
        messages.info(
            request,
            'your order for mr. {} has been deleted successfully !'.format(
                customer_name
            ),
        )
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect('/login/')
        


@never_cache
def query(request, id):
    if (
        'user_{}_uname'.format(id) not in request.session
        and 'user_{}_upass'.format(id) not in request.session
        and 'user_{}_uemail'.format(id) not in request.session
    ):
        return HttpResponseRedirect('/login/')
    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
    ):
        username = request.session['user_{}_uname'.format(id)]
        password = request.session['user_{}_upass'.format(id)]
        emailid =  request.session['user_{}_uemail'.format(id)]
        url = '/dashboard/{}'.format(id)
        data = {'un': username, 'url': url, 'id': id, 'email':emailid}
        
        if request.method =='GET':
            messages.warning(request,'here you can ask your quaries..')
            return render(request, 'queryForm.html', data)

        if request.method == 'POST':
            name = request.POST.get('username')
            email=request.POST.get('email')
            contact=request.POST.get('contact')
            query=request.POST.get('query')
            data=Query(username=name,useremail=email,contact_no=contact,querydetails=query)
            data.save()
            url = '/dashboard/{}'.format(id)
            messages.info(request, 'your query is added successfully, we will resolve it soon, please wait for response !')
            data = {'un': username, 'url': url, 'id': id}
            return HttpResponseRedirect(url)


