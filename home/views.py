from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './home/home.html')

def contact(request):
    return render(request, './contact/contact.html')

def policy(request):
    return render(request, './others/privacypolicy.html')

def termsofuse(request):
    return render(request, './others/termsofuse.html')

def about(request):
    return render(request, './others/about.html')