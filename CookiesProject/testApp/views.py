from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#how to test our browser supports cookies or not
def index(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index page</h1>')
def check_view(request):
    if request.session.test_cookie_worked():
        print('cookie are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Checking Page</h1>')

#session management by using cookies
def count_view(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'testapp/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response