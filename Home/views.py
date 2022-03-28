from pyexpat import model
from urllib import request
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf  import settings
from django.urls import reverse_lazy
from Home.models import Login,Company,Candidate
from django.views.generic import UpdateView
from django.views.generic import View,TemplateView

# Create your views here.
class Index(TemplateView) :
    '''context = {}
    return render(request,'Home/index.html',context)'''
    template_name = 'Home/index.html'

class About(TemplateView):
    template_name = 'Home/about.html'
    

class  Contact(TemplateView):
    '''return render(request,'Home/contact.html')'''
    template_name = 'Home/contact.html'



'''

def candreg(request):
    return render(request,'Home/candidate_reg.html')

def candregprocess(request):
    if request.method == 'POST':
        logincn = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        logincn.email= email
        logincn.password =password
        logincn.category = 'candidate'
        logincn.status = 0
        logincn.save()
        
        cand = Candidate()
        name = request.POST.get('name')
        addr = request.POST.get('address')
        dob = request.POST.get('dob')
        phone = request.POST.get('phonenumber')
        state = request.POST.get('state')
        place = request.POST.get('place')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username =request.POST.get('username')
        cand.candidatename = name
        cand.address = addr
        cand.dob = dob
        cand.phone = phone
        cand.state = state
        cand.place = place
        cand.qualification = qualification
        cand.gender = gender
        cand.email = email
        cand.username = username
        cand.login = logincn
        cand.status = 0
        cand.save()
        return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/candreg';</script>")
'''
class  Candreg(View):
    def get(self,request):
        return render(request,'Home/candidate_reg.html')
    def post(self,request):
        logincn = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        logincn.email= email
        logincn.password =password
        logincn.category = 'candidate'
        logincn.status = 0
        logincn.save()
        
        cand = Candidate()
        name = request.POST.get('name')
        addr = request.POST.get('address')
        dob = request.POST.get('dob')
        phone = request.POST.get('phonenumber')
        state = request.POST.get('state')
        place = request.POST.get('place')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username =request.POST.get('username')
        cand.candidatename = name
        cand.address = addr
        cand.dob = dob
        cand.phone = phone
        cand.state = state
        cand.place = place
        cand.qualification = qualification
        cand.gender = gender
        cand.email = email
        cand.username = username
        cand.login = logincn
        cand.status = 0
        cand.save()
        return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/home_index';</script>")

class Companyreg(View):
    def get(self,request):
        return render(request,'Home/company_reg.html')

    def post(self,request):
        logincm = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        logincm.email= email
        logincm.password =password
        logincm.category = 'company'
        logincm.status = 0
        logincm.save()

    
        comp = Company()
        companyname = request.POST.get('companyname')
        regid = request.POST.get('cregid')
        address = request.POST.get('address')
        phone = request.POST.get('phonenumber')
        state = request.POST.get('state')
        place = request.POST.get('place')
        owner = request.POST.get('owner')
        websiteid = request.POST.get('websiteid')
        desp = request.POST.get('description')
        email = request.POST.get('email')
        username = request.POST.get('username')
        comp.companyname =companyname
        comp.regid = regid
        comp.address = address
        comp.phone = phone
        comp.state = state
        comp.place = place
        comp.companyowner = owner
        comp.websiteid = websiteid
        comp.description = desp
        comp.email = email
        comp.username = username
        comp.login =logincm
        comp.status = 0
        comp.save()
        return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/home_index';</script>")



'''
def companyreg(request):
    return render(request,'Home/company_reg.html')

def companyregprocess(request):
    ueslogincm = Login()
    email = request.POST.get('email')
    password = request.POST.get('password')
    logincm.email= email
    logincm.password =password
    logincm.category = 'company'
    logincm.status = 0
    logincm.save()

    comp = Company()
    companyname = request.POST.get('companyname')
    regid = request.POST.get('cregid')
    address = request.POST.get('address')
    phone = request.POST.get('phonenumber')
    state = request.POST.get('state')
    place = request.POST.get('place')
    owner = request.POST.get('owner')
    websiteid = request.POST.get('websiteid')
    desp = request.POST.get('description')
    email = request.POST.get('email')
    username = request.POST.get('username')
    comp.companyname =companyname
    comp.regid = regid
    comp.address = address
    comp.phone = phone
    comp.state = state
    comp.place = place
    comp.companyowner = owner
    comp.websiteid = websiteid
    comp.description = desp
    comp.email = email
    comp.username = username
    comp.login =logincm
    comp.status = 0
    comp.save()
    return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/companyreg';</script>")
'''
'''
def login(request):
    return render(request,'Home/login.html')
def loginprocess(request):
    if reqt.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if (Login.objects.filter(email=email, password=password).exists()):
            logins = Login.objects.filter(email=email, password=password)
            for login in logins:

                #login=Login()
                usertype = login.category
                status = login.status
                request.session["usertype"] = usertype

                if ((usertype == "admin")&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'adminhome/adminhome.html')
                elif ((usertype == 'candidate')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'candidate/candidate.html')
                elif ((usertype == 'company')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'company/company.html')

                else:
                    template = loader.get_template("home/login.html")
                    context = {"error": "Incorrect username or password"}
                    return HttpResponse(template.render(context, request))

                    # dic = {'msg': 'Invalid user name or password'}
                    # return render(request, 'login.html', context=dic)
        else:
            template = loader.get_template("home/login.html")
            context = {"error": "Incorrect Information"}
            return render(request,'candidate/candidate.html')
    else:
        template = loader.get_template("home/login.html")
        context = {}
        return HttpResponse(template.render(context, request))
        '''
class LoginView(View):
    def get(self,request):
        return render(request,"Home/login.html")
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (Login.objects.filter(email=email, password=password).exists()):
            logins = Login.objects.filter(email=email, password=password)
            for login in logins:

                #login=Login()
                usertype = login.category
                status = login.status
                request.session["usertype"] = usertype
                request.session["status"] = status
                if ((usertype == "admin")&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'adminhome/adminhome.html')
                elif ((usertype == 'candidate')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'candidate/candidate.html')
                elif ((usertype == 'company')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'company/company.html')

                else:
                    template = loader.get_template("home/login.html")
                    context = {"error": "Incorrect username or password"}
                    return HttpResponse(template.render(context, request))

                    # dic = {'msg': 'Invalid user name or password'}
                    # return render(request, 'login.html', context=dic)
        else:
            template = loader.get_template("home/login.html")
            context = {"error": "Incorrect Information"}
            return render(request,'candidate/candidate.html')
    