from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf  import settings
from django.db.models import Q
from Home.models import Company,Candidate,Login
from Company.models import Vacancies
from Candidate.models import ApplyVacancy
from django.views.generic import View,TemplateView,UpdateView

class Candidatehome(TemplateView):
    template_name = 'candidate/candidate.html'

class  Vacancy(View):
    def get(self,request):
        lid = request.session.get('userid')
        vacn = Vacancies.objects.filter(status=1)
        appvcn = ApplyVacancy.objects.filter(candlogin_id = lid)
        comp = Company.objects.all()
        context = {'vacn': vacn, 'comp': comp,'appvcn': appvcn,'lid':lid}
        return render(request, 'candidate/viewvacancies.html', context)

class  Searchvacancy(View):
    def get(self,request):
        return render(request, 'candidate/searchvacancy.html')
    def post(self,request):
        qual = request.POST.get("qualification")
        jobloc = request.POST.get("joblocation")
        vacn = Vacancies.objects.filter(Q(qualification = qual)|Q(joblocation = jobloc))
        comp = Company.objects.all()
        context = {'vacn': vacn, 'comp': comp}
        return render(request, 'candidate/viewsearchvacancy.html',context)
    
'''
def apply(request,id):
    lid = request.session.get('userid')
    cnd = Candidate.objects.get(login_id = lid)
    vid = Vacancies.objects.get(id=id)
    context = {'vid': vid,'cnd':cnd}
    return render(request,'candidate/applyvacancy.html',context)

def applyvacancyprocess(request):
    lid = request.session.get('userid')
    vid = request.POST.get("vid")
    candidatename = request.POST.get("candname")
    candidatemail= request.POST.get("candemail")
    qual = request.POST.get("qualification")
    skill = request.POST.get("skill")
    contact = request.POST.get("contact")
    experience = request.POST.get("experience")
    location = request.POST.get("location")
    uploadresume = request.FILES.get("resumeupload")

    av = ApplyVacancy()
    av.candidatename = candidatename
    av.candidatemail = candidatemail
    av.qualification = qual
    av.keyskill = skill
    av.experience = experience
    av.location = location
    av.contactno = contact
    av.resume = uploadresume
    av.candlogin_id = lid
    av.vacancyid_id = vid
    av.save()
    return HttpResponse("<script>alert('Successfully apply vacancy');window.location ='vacancies/';</script>")
    '''

class Apply(UpdateView):
    def get(self,request,id):
        lid = request.session.get('userid')
        cnd = Candidate.objects.get(login_id = lid)
        vid = Vacancies.objects.get(id=id)
        context = {'vid': vid,'cnd':cnd}
        return render(request,'candidate/applyvacancy.html',context)

class Applyvacancy(UpdateView):
    def post(self,request):
        lid = request.session.get('userid')
        vid = request.POST.get("vid")
        candidatename = request.POST.get("candname")
        candidatemail= request.POST.get("candemail")
        qual = request.POST.get("qualification")
        skill = request.POST.get("skill")
        contact = request.POST.get("contact")
        experience = request.POST.get("experience")
        location = request.POST.get("location")
        uploadresume = request.FILES.get("resumeupload")

        av = ApplyVacancy()
        av.candidatename = candidatename
        av.candidatemail = candidatemail
        av.qualification = qual
        av.keyskill = skill
        av.experience = experience
        av.location = location
        av.contactno = contact
        av.resume = uploadresume
        av.candlogin_id = lid
        av.vacancyid_id = vid
        av.save()
        return HttpResponse("<script>alert('Successfully apply vacancy');window.location ='vacancies/';</script>")


def calogout(request):
    try:
      del request.session['email']
    except:
      pass
    return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/login';</script>")
