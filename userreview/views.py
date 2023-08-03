from django.shortcuts import render
from userreview.models import Review, Memory
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# this is the feedback form page for users...
from django.views.decorators.cache import never_cache
from django.contrib import messages


@never_cache
def review(request, id):
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
        url = '/dashboard/{}'.format(id)
        data = {'un': username, 'url': url, 'id': id}
        # this return is work for default method which is get...    
        if request.method=='GET':
            messages.warning(request,'here you can add your feedback..')
            return render(request, 'reviewform.html', data)

        if request.method == 'POST':
            name = request.POST.get('username')
            review = request.POST.get('review')
            ratings = request.POST.get('ratings')
            data = Review(username=name, user_review=review, ratings=ratings)
            data.save()
            url = '/dashboard/{}'.format(id)
            messages.success(request, 'your review is added successfully, that is visible in our blog page. !')
            data = {'un': username, 'url': url, 'id': id}
            return HttpResponseRedirect(url)
    
    

@never_cache
def blog(request, id=None):
    if id == None:
        data = Review.objects.all()
        memory = Memory.objects.all()
        datamain = {'data': data, 'memories': memory}
        return render(request, 'blogs.html', datamain)
    else:
        if (
            'user_{}_uname'.format(id) in request.session
            and 'user_{}_uemail'.format(id) in request.session
            and 'user_{}_upass'.format(id) in request.session
        ):
            data = Review.objects.all()
            memory = Memory.objects.all()
            url = '/dashboard/{}'.format(id)
            datamain = {'data': data, 'id': id, 'url': url, 'memories': memory}
            return render(request, 'blogs2.html', datamain)
        else:
            return HttpResponseRedirect('/blogs/')

@never_cache
def memory(request, id):
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
        url = '/dashboard/{}'.format(id)
        data = {'un': username, 'url': url, 'id': id}
        
        if request.method =='GET':
            messages.warning(request,'here you can share your memories..')
            return render(request, 'memoryshareForm.html', data)

        if request.method == 'POST':
            name = request.POST.get('username')
            title = request.POST.get('title')
            about = request.POST.get('about')
            image = request.FILES['image']
            data = Memory(username=name, title=title, about=about,image=image)
            data.save()
            url = '/dashboard/{}'.format(id)
            messages.success(request, 'your memory is added successfully that is visible in our blog page !')
            data = {'un': username, 'url': url, 'id': id}
            return HttpResponseRedirect(url)
        





        