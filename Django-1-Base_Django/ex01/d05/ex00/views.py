from django.shortcuts import render
# Create your views here.

def markdown_syntax(request):
    return render(request, 'ex00/index.html')