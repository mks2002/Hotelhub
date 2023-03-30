# integrate paypal payment gateway....



#____________________________________________________________________________________

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

# @login_required
# def login(request):
#     if request.user.is_authenticated:
#         # If user is already authenticated, redirect to hotel list page
#         return redirect('hotel_list')

#     if request.method == "POST":
#         un = request.POST.get('name')
#         pw = request.POST.get('password')

#         user = authenticate(request, username=un, password=pw)

#         if user is not None:
#             login(request, user)
#             hl = 'all'
#             url = f"/hotellist/{hl}/{user.id}"
#             messages.success(
#                 request, f'Welcome, {user.username}! You are successfully logged in. Now you can do your bookings!')
#             return redirect(url)
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return render(request, 'login.html')

#     if request.method == "GET":
#         messages.warning(request, 'For booking, you need to login first!')
#         return render(request, 'login.html')



#__________________________________________________________________________
# /accounts/login/?next=/login/
# /accounts/login/?next=/login/

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
# from django.urls import reverse
# from django.contrib import messages

# @login_required
# def login(request):
#     if request.user.is_authenticated:
#         # If user is already authenticated, redirect to hotel list page
#         return redirect('hotel_list')

#     if request.method == "POST":
#         un = request.POST.get('name')
#         pw = request.POST.get('password')

#         user = authenticate(request, username=un, password=pw)

#         if user is not None:
#             login(request, user)
#             hl = 'all'
#             url = reverse('hotel_list', args=[hl, user.id])
#             messages.success(
#                 request, f'Welcome, {user.username}! You are successfully logged in. Now you can do your bookings!')
#             return redirect(url)
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return render(request, 'login.html')

#     if request.method == "GET":
#         messages.warning(request, 'For booking, you need to login first!')
#         return render(request, 'login.html')

#__________________________________________________________________________________

   #  if request.method == "GET":
   #      if 'logged_in' in request.session:
   #          prev_url = request.META.get('HTTP_REFERER')
   #          if prev_url is not None and prev_url != request.build_absolute_uri(reverse('login')):
   #              id = request.session.get('user_{}_uname'.format(
   #                  request.session.get('user_id')))
   #              hl = 'all'
   #              url = "/hotellist/{}/{}".format(hl, id)
   #              messages.warning(
   #                  request, 'you are logged in, so you cant go back without logout !')
   #              return HttpResponseRedirect(url)
   #          else:
   #              id = request.session.get('user_{}_uname'.format(
   #                  request.session.get('user_id')))
   #              hl = 'all'
   #              url = "/hotellist/{}/{}".format(hl, id)
   #              return HttpResponseRedirect(url)
   #      else:
   #          messages.warning(request, 'for booking you need to login first !')
   #          return render(request, 'login.html')




    # if request.method == "GET":
    #     if 'logged_in' in request.session:
    #         prev_url = request.META.get('HTTP_REFERER')
    #         if prev_url is not None:
    #             id = request.session.get('user_{}_uname'.format(
    #                 request.session.get('user_id')))
    #             hl = 'all'
    #             url = "/hotellist/{}/{}".format(hl, id)
    #             messages.warning(
    #                 request, 'you are logged in, so you cant go back without logout !')
    #             return HttpResponseRedirect(url)
    #         else:
    #             id = request.session.get('user_{}_uname'.format(
    #                 request.session.get('user_id')))
    #             hl = 'all'
    #             url = "/hotellist/{}/{}".format(hl, id)
    #             return HttpResponseRedirect(url)
    #     else:
    #         messages.warning(request, 'for booking you need to login first !')
    #         return render(request, 'login.html')







    # if request.method == "GET":
    #     if 'logged_in' in request.session:
    #         prev_url = request.META.get('HTTP_REFERER')
    #         if prev_url is not None:
    #             messages.warning(
    #                 request, 'you are logged in, so you cant go back without logout !')
    #             return HttpResponseRedirect(prev_url)
    #         else:
    #             hl = 'all'
    #             id = request.session.get('user_id')
    #             url = reverse('hotellist', args=[hl, id])
    #             return HttpResponseRedirect(url)
    #     else:
    #         messages.warning(request, 'for booking you need to login first !')
    #         return render(request, 'login.html')