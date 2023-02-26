from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import createMessage
from .models import Message
 
context ={}
def index(request):
    return render(request, "deneme.html", context)

def home(request):
    getData = Message.objects.all()
    return render(request, "pages/home.html", {"dbData":getData})

def second(response):
	return render(response, "pages/second.html", context)

def third(response):
	return render(response, "pages/third.html", context)

def form(response):
    if(response.method) == "POST":
        form = createMessage(response.POST)
        
        if(form.is_valid()):
            fullName = form.cleaned_data["fullName"]
            mailAddress = form.cleaned_data["mailAddress"]
            uMessage = form.cleaned_data["uMessage"]
            newMessage = Message(fullName=fullName, mailAddress = mailAddress, uMessage = uMessage)
            newMessage.save()
            form = createMessage()
            return render(response, "pages/form.html", {"form": form, "newMessage":newMessage})
    else:
        form = createMessage()
        return render(response, "pages/form.html", {"form": form})
    



