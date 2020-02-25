from django.shortcuts import render

# Create your views here.
def moviesInfo(request):
    my_dict={'head_msg':'Movies Information',
    'sub_msg1':'Sonali slowly getting cured',
    'sub_msg2':'Bahubali-3 is just planning',
    'sub_msg3':'Salman Khan ready to marriage',
    'photo':'images/A.jpg'
    }
    return render(request,'NewsApp/news.html',context=my_dict)

def sportsInfo(request):
    my_dict={'head_msg':'Sports Information',
    'sub_msg1':'Anushka sharma firing like anything',
    'sub_msg2':'Kohli updating in game anything can happen',
    'sub_msg3':'Worst performance by India-Sehwag',
    'photo':'images/A.jpg'
    }
    return render(request,'NewsApp/news.html',context=my_dict)

def politicsInfo(request):
    my_dict={'head_msg':'Politics Information',
    'sub_msg1':'Achhce Din Aaa gaya',
    'sub_msg2':'Rupee Value now 1$:70RS',
    'sub_msg3':'In India Single Paisa Black money No more',
    'photo':'images/A.jpg'
    }
    return render(request,'NewsApp/news.html',context=my_dict)
def Index(request):
    return render(request,'NewsApp/index.html')