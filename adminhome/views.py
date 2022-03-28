from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from Home.models import Company,Candidate,Login

def Adminhomee(request):
    return render(request,'adminhome/adminhome.html')

def alogout(request):
    try:
      del request.session['email']
    except:
      pass
    return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/login';</script>")


def allcompany(request) :
    sta = 1
    comp1 = Company.objects.select_related().filter(status=sta)
    context = {'comp': comp1}
    return render(request, 'adminhome/allcompany.html', context)

def allcandidate(request):
    sta = 1
    cond1 = Candidate.objects.select_related().filter(status=sta)
    context = {'cond':cond1}
    return render(request,'adminhome/allcandidate.html',context)

def newcandidate(request):
    stat = 0
    cond = Candidate.objects.select_related().filter(status = stat)
    context = {'cond' : cond}
    return render(request,'adminhome/newcandidate.html',context)

def newcompany(request):
    sta = 0
    comp = Company.objects.select_related().filter(status=sta)
    context = {'comp': comp}
    return render(request, 'adminhome/newcompany.html', context)

def acceptcompany(request,id):
    accep = Login.objects.get(id = id)
    accecmp = Company.objects.get(login_id = id)
    accep.status = 1
    accecmp.status = 1
    accep.save()
    accecmp.save()
    return HttpResponse("<script>alert('Accepted ...');window.location ='../newcompany/';</script>")

def acceptcandidate(request,id):
    accep = Login.objects.get(id = id)
    accecan = Candidate.objects.get(login_id = id)
    accep.status = 1
    accecan.status = 1
    accep.save()
    accecan.save()
    return HttpResponse("<script>alert('Accepted....');window.location='../newcandidate/';</script>")


def rejectcompany(request,id):
    rej = Login.objects.get(id = id)
    rejc = Company.objects.get(login_id = id)
    email = rejc.email
    rej.delete()
    rejc.delete()
    return HttpResponse("<script>alert('Rejected..');window.location ='../newcompany/';</script>")

def rejectcandidate(request,id):
    rejcn = Login.objects.get(id=id)
    rejcnd = Candidate.objects.get(login_id=id)
    email = rejcnd.email
    rejcn.delete()
    rejcnd.delete()
    return HttpResponse("<script>alert('Rejected.. ');window.location ='../newcandidate/';</script>")





# Create your views here.
