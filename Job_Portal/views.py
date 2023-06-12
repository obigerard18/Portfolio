from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Job_Portal/index.html')

def about(request):
    return render(request, 'Job_Portal/about.html')

def blog(request):
    return render(request, 'Job_Portal/blog.html')

def contact(request):
    return render(request, 'Job_Portal/contact.html')