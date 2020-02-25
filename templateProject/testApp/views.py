from django.shortcuts import render
import datetime
# Create your views here.
'''
def wish(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'testApp/wish.html',context=my_dict)
'''
def wish(request):
    date=datetime.datetime.now()
    msg='Hello Ajit !!! Very Very Good '
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning'
    elif h<16:
        msg+='AfterNoon'
    elif h<21:
        msg+='Evening'
    else:
        msg = 'Hello Ajit !!! Very Very Good Night'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/wish.html',context=my_dict)
