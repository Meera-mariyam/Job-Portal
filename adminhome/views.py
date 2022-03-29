from django.shortcuts import redirect, render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from Home.models import Company,Candidate,Login
from django.views.generic import View,TemplateView,UpdateView,ListView
from django.contrib import messages


class Adminhomee(TemplateView):
    template_name = 'adminhome/adminhome.html'

def alogout(request):
    try:
      del request.session['email']
    except:
      pass
    messages.info(request,'You are successfully logged off')
    return redirect('/login')
    #return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/login';</script>")


class Allcompany(View) :
    def get(self,request):
        sta = 1
        comp1 = Company.objects.select_related().filter(status=sta)
        context = {'comp': comp1}
        return render(request, 'adminhome/allcompany.html', context)

class Allcandidate(View):
    def get(self,request):
        sta = 1
        cond1 = Candidate.objects.select_related().filter(status=sta)
        context = {'cond':cond1}
        return render(request,'adminhome/allcandidate.html',context)

class Newcandidate(View):
    def get(self,request):
        stat = 0
        cond = Candidate.objects.select_related().filter(status = stat)
        context = {'cond' : cond}
        return render(request,'adminhome/newcandidate.html',context)

class Newcompany(View):
    def get(self,request):
        sta = 0
        comp = Company.objects.select_related().filter(status=sta)
        context = {'comp': comp}
        return render(request, 'adminhome/newcompany.html', context)

class Acceptcompany(ListView):
    def get(self,request,id):
        accep = Login.objects.get(id = id)
        accecmp = Company.objects.get(login_id = id)
        accep.status = 1
        accecmp.status = 1
        accep.save()
        accecmp.save()
        messages.info(request,'Accepted')
        return redirect('newcompany')
        #return HttpResponse("<script>alert('Accepted ...');window.location ='../newcompany/';</script>")

class Acceptcandidate(View):
    def get(self,request,id):
        accep = Login.objects.get(id = id)
        accecan = Candidate.objects.get(login_id = id)
        accep.status = 1
        accecan.status = 1
        accep.save()
        accecan.save()
        messages.info(request,'Accepted')
        return redirect('newcandidate')
        #return HttpResponse("<script>alert('Accepted....');window.location='../newcandidate/';</script>")

class Rejectcompany(UpdateView):
    def post(self,request,id):
        rej = Login.objects.get(id = id)
        rejc = Company.objects.get(login_id = id)
        rej.delete()
        rejc.delete()
        messages.info(request,'Rejected')
        return redirect('newcompany')
        #return HttpResponse("<script>alert('Rejected..');window.location ='../newcompany/';</script>")

class Rejectcandidate(UpdateView):
    def post(self,request,id):
        rejcn = Login.objects.get(id=id)
        rejcnd = Candidate.objects.get(login_id=id)
        #email = rejcnd.email
        rejcn.delete()
        rejcnd.delete()
        messages.info(request,'Rejected')
        return redirect('newcandidate')
        #return HttpResponse("<script>alert('Rejected.. ');window.location ='../newcandidate/';</script>")





# Create your views here.
