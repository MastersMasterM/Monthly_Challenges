from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Just Sleep!",
    "february": "Work Work Work",
    "march": "Work out!!!",
    "april": "Whats wrong with me bro!",
    "may" : "Just cry and think about your bad behaviours :))",
    "june": "You are not GOD!!",
    "july": "Start the loop in july"
}

def index(request):
    mon_name = list(monthly_challenges.keys())
    response_data = """
        <ul>
    """
    for m in mon_name:
        ur = reverse("month-challenge",args=[m])
        response_data = response_data + f"<li><a href={ur}>{m.capitalize()}</a></li>"
    response_data = response_data + "</ul>"
    return HttpResponse(response_data)

def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]    
        return HttpResponse(challenge_text)   
    except :
        return HttpResponseNotFound("This month is not supported")

    
def month_num(request, month:int):
    forward_month = list(monthly_challenges.keys())
    if month > len(forward_month):
        return HttpResponseNotFound("Invalid Month")
    mon = forward_month[month - 1]
    return HttpResponseRedirect(reverse("month-challenge",args=[mon]))