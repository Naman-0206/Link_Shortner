from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import Urls
import uuid


# Create your views here.



def encrypt(url):

    #umodel = Urls.objects.get(website=url)
    surl = Urls.objects.filter(website=url)

    if not surl:
        unique_string = str(uuid.uuid4())[:8]
        while len(Urls.objects.filter(ids=unique_string)):
            unique_string = str(uuid.uuid4())[:8]
        n = Urls.objects.create(website=url , ids=unique_string)
        n.save()


    print("-------------------------------------------")
    print(surl)
    print("-------------------------------------------")
    surl = Urls.objects.filter(website=url)[0]
    return surl.ids

def decrypt(idinp):

    try:
        return Urls.objects.get(ids=idinp).website
    except:
        print( "error occured")
        return None
     

def new(request):
    print(request)
    if request.method == 'POST':
        url = request.POST.get('url')
        if url=="":
            return render(request , 'home.html')

        s_url = request.build_absolute_uri()+str(encrypt(url))

        return render(request , 'home.html' , context={
                "url":url,
                's_url':s_url,
            })

    return render(request , 'home.html')

def redirect_url(request,urls):
    print(urls)


    surl = decrypt(urls)
    if surl:
        return redirect(decrypt(urls))
    
    return render(request , 'pagenotexist.html')
 
    #return HttpResponseRedirect(decrypt(urls))