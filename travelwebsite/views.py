
# this views render all tha project level apps which are common to entire project and not required any model query ...
# this view file is we dont get by default because it is not an application it is the main folder inside our main project this view file I created myself...


# import all basic rendering and redirecting modules...
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# requests module is used for dealing with api...
import requests


def price(request):
    return HttpResponse('this is price page')


# from here all this are dynamic pages ....
@never_cache
def homepage(request, id=None):
    if id == None:
        return render(request, 'index.html')
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url}
            return render(request, 'index2.html', data)
        else:
            return HttpResponseRedirect('/')


@never_cache
def about(request, id=None):
    if id == None:
        return render(request, 'about.html')
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url}
            return render(request, 'about2.html', data)
        else:
            return HttpResponseRedirect('/about/')


@never_cache
def services(request, id=None):
    if id == None:
        return render(request, 'services.html')
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url}
            return render(request, 'services2.html', data)
        else:
            return HttpResponseRedirect('/services/')


@never_cache
def staffs(request, id=None):
    if id == None:
        return render(request, 'staffs.html')
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url}
            return render(request, 'staffs2.html', data)
        else:
            return HttpResponseRedirect('/staffs/')


@never_cache
def travel(request, id=None):
    if id == None:
        data = {}
        try:
            if request.method == "POST":
                id1 = request.POST.get("source")
                url = "https://trains.p.rapidapi.com/"

                payload = {"search": id1}
                headers = {
                    "content-type": "application/json",

                    "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b0",
                    "X-RapidAPI-Host": "trains.p.rapidapi.com",
                }

                response = requests.request(
                    "POST", url, json=payload, headers=headers)
                datamain = response.json()
                data = {"datamain": datamain}
                return render(request, "travel_details.html", data)
        except Exception as e:
            pass
        return render(request, "travel_details.html", data)
    else:
        if 'user_{}_uname'.format(id) in request.session and 'user_{}_uemail'.format(id) in request.session and 'user_{}_upass'.format(id) in request.session:
            url = "/dashboard/{}".format(id)
            data = {'id': id, 'url': url}
            try:
                if request.method == "POST":
                    id1 = request.POST.get("source")
                    url = "https://trains.p.rapidapi.com/"

                    payload = {"search": id1}
                    headers = {
                        "content-type": "application/json",
                        "X-RapidAPI-Key": "a78e10f741mshff5ec54a01b89afp1e0ae3jsnfdbc5239b4a0",
                        "X-RapidAPI-Host": "trains.p.rapidapi.com",
                    }

                    response = requests.request(
                        "POST", url, json=payload, headers=headers)
                    datamain = response.json()
                    url = "/dashboard/{}".format(id)
                    data = {"datamain": datamain, 'id': id, 'url': url}
                    return render(request, "travel_details2.html", data)
            except Exception as e:
                pass
            return render(request, "travel_details2.html", data)
        else:
            return HttpResponseRedirect('/travel_details/')
