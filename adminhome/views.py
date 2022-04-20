import email
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from Home.models import Company,Candidate,Login
from django.views.generic import View,TemplateView,UpdateView,ListView
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

class Adminhomee(TemplateView):
    template_name = 'adminhome/adminhome.html'

class Logout(View):
    def get(self,request):
        messages.info(request,'You are successfully logged off')
        return redirect('/login')
    #return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/login';</script>")


class Allcompany(View) :
    def get(self,request):
        sta = 1
        comp1 = Company.objects.select_related().filter(status=sta)
        paginator = Paginator(comp1,3)
        page = request.GET.get('page')
        try :
            comp1 = paginator.page(1)
        except PageNotAnInteger:
            comp1 = paginator.page(paginator.num_pages)
        context = {'comp': comp1,'page':page}
        return render(request, 'adminhome/allcompany.html', context)

class Allcandidate(View):
    def get(self,request):
        sta = 1
        cond1 = Candidate.objects.select_related().filter(status=sta)
        paginator = Paginator(cond1,3)
        page = request.GET.get('page')
        try :
            comp1 = paginator.page(1)
        except PageNotAnInteger:
            comp1 = paginator.page(paginator.num_pages)
        context = {'cond':cond1,'page':page}
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
        email = accecmp.email
        print(email)
        accep.status = 1
        accecmp.status = 1
        accep.save()
        accecmp.save()
        send_mail('Accepted', 'You are accepted now you can login to your account', settings.EMAIL_HOST_USER, email, fail_silently=False)
        return redirect('newcompany')
        #return HttpResponse("<script>alert('Accepted ...');window.location ='../newcompany/';</script>")

class Acceptcandidate(View):
    def get(self,request,id):
        accep = Login.objects.get(id = id)
        accecan = Candidate.objects.get(login_id = id)
        email = accecan.email
        #print(email)
        accep.status = 1
        accecan.status = 1
        accep.save()
        accecan.save()
        #send_mail('Accepted', 'You are accepted now you can login to your account', settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return redirect('newcandidate')
        #return HttpResponse("<script>alert('Accepted....');window.location='../newcandidate/';</script>")

class Rejectcompany(UpdateView):
    def post(self,request,id):
        rej = Login.objects.get(id = id)
        rejc = Company.objects.get(login_id = id)
        email = rejc.email
        rej.delete()
        rejc.delete()
        send_mail('Accepted', 'You are accepted now you can login to your account', settings.EMAIL_HOST_USER, [email], fail_silently=False)
        messages.info(request,'Rejected')
        return redirect('newcompany')
        #return HttpResponse("<script>alert('Rejected..');window.location ='../newcompany/';</script>")

class Rejectcandidate(UpdateView):
    def post(self,request,id):
        rejcn = Login.objects.get(id=id)
        rejcnd = Candidate.objects.get(login_id=id)
        email = rejcnd.email
        #email = rejcnd.email
        rejcn.delete()
        rejcnd.delete()
        send_mail('Accepted', 'You are accepted now you can login to your account', settings.EMAIL_HOST_USER, [email], fail_silently=False)
        messages.info(request,'Rejected')
        return redirect('newcandidate')
        #return HttpResponse("<script>alert('Rejected.. ');window.location ='../newcandidate/';</script>")





# Create your views here.
