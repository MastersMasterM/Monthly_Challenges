from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Just Sleep!",
    "february": "Work Work Work",
    "march": "Work out!!!",
    "april": "Whats wrong with me bro!",
    "may" : "Just cry and think about your bad behaviours :))",
    "june": "You are not GOD!!",
    "july": "Start the loop in july",
    "agust": "Finishing Django",
    "september" : None
}

def index(request):
    mon_name = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months": mon_name
    })

def monthly_challenge(request, month:str):
    
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month" : month
        })   
    except :
        raise Http404()

    
def month_num(request, month:int):
    forward_month = list(monthly_challenges.keys())
    if month > len(forward_month):
        raise Http404()
    mon = forward_month[month - 1]
    return HttpResponseRedirect(reverse("month-challenge",args=[mon]))