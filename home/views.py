from django.shortcuts import render, redirect
from .models import College
from .forms import UserForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    context = {}
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
                to_email = list(str(college.college_email).split(' '))
                try:
                    send_mail(subject, message, email, to_email)
                except BadHeaderError:
                    template = 'home/signup.html'
                    context = {
                        'form': form,
                        'errors': 'Invalid header found.',
                        'options': options
                    }
                    return render(request, template, context)
                return redirect('home')
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
