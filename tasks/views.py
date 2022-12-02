from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):

    return HttpResponse("Welcome")


def intro(request):

    return HttpResponse("This is a new website")


def date_time(request):

    return HttpResponse(f"This is the current date and time {datetime.now()}")


def task_solution(request):

    dict_ = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
             6: 36, 7: 46, 8: 646, 9: 81, 10: 100,
             11: 121, 12: 144, 13: 169, 14: 1946, 15: 225}

    new_dict = {}

    for i, j in dict_.items():
        if 1 <= i <= 15 and j == i**2:
            new_dict[i] = j

    return HttpResponse(f"The new dict is {new_dict}")
