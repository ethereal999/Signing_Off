from django.contrib import messages
from django.shortcuts import render, redirect

from Signing_Off.settings import EMAIL_HOST_USER
from .models import College
from .forms import UserForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    context = {}
    messages.success(request,"Hii")
    return render(request, 'home/home.html', context)


def about(request):
    context = {}
    return render(request, 'home/About.html', context)


options = [x.name for x in College.objects.all()]


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid form')
            college = College.objects.all().filter(name=form.cleaned_data.get('college_name'))[0]
            required_email_ext = college.college_ext
            email = form.cleaned_data.get('email')
            email_ext = email.split('@')[1]
            if required_email_ext == email_ext:
                subject = "Subject"
                if form.cleaned_data.get('enquiry') == 0:
                    form_link = str(college.form_receive)
                else:
                    form_link = str(college.form_donate)
                message = "Here's a form : " + form_link
                to_email = [str(email)]
                print(to_email)
                try:
                    send_mail(subject, message,str(EMAIL_HOST_USER), to_email, fail_silently=False)
                except BadHeaderError:
                    template = 'home/signup.html'
                    context = {
                        'form': form,
                        'errors': 'Invalid header found.',
                        'options': options
                    }
                    return render(request, template, context)
                messages.success(request,'A link is sent to your email!')
                return redirect('home:home')
            else:
                template = 'home/signup.html'
                context = {
                    'form': form,
                    'errors': "This email doesn't belong to " + college.name,
                    'options': options
                }
                return render(request, template, context)
        else:
            template = 'home/signup.html'
            form = UserForm()
            context = {
                'form': form,
                'options': options,
                'errors': 'Invalid form'
            }
            return render(request, template, context)

    template = 'home/signup.html'
    form = UserForm()
    context = {
        'form': form,
        'options': options,
        'errors': ''
    }
    return render(request, template, context)
