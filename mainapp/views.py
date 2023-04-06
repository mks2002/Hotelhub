# mainapp we created for login details and login model table so here we serve all the pages related to user signup and login..

# import all basic rendering and redirecting modules...
# from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# datetime module is used for deal with dates..
from datetime import datetime as dt

# this are all our models which we used in this section..

from mainapp.models import Login
from bookings.models import Bookinghotel
from payments.models import Paymentdetail

from django.contrib import messages

# this is for hashing the password before save it to database.....
from django.contrib.auth.hashers import make_password, check_password


# we dont use Hotellist here..
# from hotellist.models import Hotellist

# this is the same signup page using messages freamework..
def signup(request):
    if request.method == "POST":
        un = request.POST.get('name')
        email = request.POST.get('useremail')
        pw = request.POST.get('password')
        cpw = request.POST.get('cpassword')

        if pw != cpw:
            messages.error(request, 'password and confirm password must be same !')
            
        elif len(pw)<8:
            messages.warning(request,'password length must be of 8 digit !')    
        else:
            if Login.objects.filter(username=un).exists() | Login.objects.filter(email=email).exists():
                messages.warning(
                    request, 'username or email already exist select another !')
            else:
                pw = make_password(pw)
                maindata = Login(username=un, email=email, password=pw)
                maindata.save()
                messages.success(
                    request, 'you have registered succesfully, now you can login !')
                url = '/login/'
                return HttpResponseRedirect(url)
    return render(request, 'signup.html')


@never_cache
def login(request):

    if request.method == "POST":
        un = request.POST.get('name')
        pw = request.POST.get('password')

        try:
            user = Login.objects.get(username=un)
        except Login.DoesNotExist:
            user = None

        if user is not None and check_password(pw, user.password):
            hl = 'all'
            request.session['user_{}_uname'.format(user.id)] = user.username
            request.session['user_{}_uemail'.format(user.id)] = user.email
            request.session['user_{}_upass'.format(user.id)] = user.password
            id = user.id
            url = "/hotellist/{}/{}".format(hl, id)
            messages.success(
                request, f'welcome mr. {user.username} you are successfully logged in, now you can do your bookings !')
            return HttpResponseRedirect(url)
        else:
            messages.error(
                request, 'you are not registered create account to login !')
            return render(request, 'login.html')

    if request.method == "GET":
        messages.warning(request, 'for booking you need to login first !')
        return render(request, 'login.html')


# first delete all the sessions using del command...
# session.flush will delete all the cookies corresponding to the session key...
# session.clear_expired will delete all the deleted data from the table....


def logout_user(request, id):
    if 'user_{}_uname'.format(id) not in request.session and 'user_{}_upass'.format(id) not in request.session and 'user_{}_uemail'.format(id) not in request.session:
        return HttpResponseRedirect('/login/')
    elif 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
        user = Login.objects.get(
            username=request.session.get('user_{}_uname'.format(id)))
        del request.session['user_{}_uname'.format(user.id)]
        del request.session['user_{}_uemail'.format(user.id)]
        del request.session['user_{}_upass'.format(user.id)]
        request.session.flush()
        request.session.clear_expired()
        messages.info(request, 'you are logged out !')
    return HttpResponseRedirect('/login/')


# this is for forgot password and this is before login ...
def update(request):
    if request.method == "GET":
        messages.warning(request, 'enter new password here !')
        return render(request, 'update_password.html')

    if request.method == "POST":
        name = request.POST.get('name')
        new = request.POST.get('newpassword')
        cnew = request.POST.get('confirm_newpassword')
        if Login.objects.filter(username=name).exists():
            main = Login.objects.get(username=name)
            oldpassword = main.password
            if len(new)<8:
                messages.warning(request,'your new password must be of atleast 8 digit !')
            # here cnew is the newconfirm password....
            elif new == cnew:
                if check_password(new, oldpassword):
                    messages.warning(
                        request, 'your new password is to similar to old password select another !')
                else:
                    updatedpassword = make_password(new)
                    Login.objects.filter(username=name).update(
                        password=updatedpassword)
                    # when we update the password we have to update it in the Bookinghotel and payment table also othewise data is not properly displayed...
                    Bookinghotel.objects.filter(username=name).update(
                        userpassword=updatedpassword)
                    Paymentdetail.objects.filter(
                        username=name).update(password=updatedpassword)
                    messages.success(
                        request, 'your password is updated successfully now you can login !')
                    url = '/login/'
                    return HttpResponseRedirect(url)
            else:
                messages.error(
                    request, 'password and confirm password must be same !')
        else:
            messages.error(
                request, 'No such account is exist pls enter a valid username !')
    return render(request, 'update_password.html')


# we can also create one update password after the login .....
