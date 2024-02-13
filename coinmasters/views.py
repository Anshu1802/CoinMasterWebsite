from django.shortcuts import render,redirect





def function(request):
    return render(request,'index.html')