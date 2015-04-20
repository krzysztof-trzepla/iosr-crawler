from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from nlp import extractor
from .forms import SentenceForm


def login(request):
    return render(request, 'ui/login.html')


@login_required(login_url='/')
def home(request):
    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            keywords = extractor.keywords(form.cleaned_data['sentence'])
            return render(request, 'ui/home.html',
                          {'form': SentenceForm(), 'keywords': keywords})
        else:
            messages.add_message(request, messages.ERROR, 'Invalid sentence.')
    form = SentenceForm()
    return render(request, 'ui/home.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')