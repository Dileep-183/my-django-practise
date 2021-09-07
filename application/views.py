from .forms import MobliesForm
from django.shortcuts import render

# Create your views here.
def home(request):
    form = MobliesForm
    return render(request,template_name='config.html',context={'form':form})
