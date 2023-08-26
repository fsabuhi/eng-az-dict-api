from django.shortcuts import render
from django.http import HttpResponse
import dictapi.dict.getword as getwordfromdb
def members(request):
    return HttpResponse("Hello world!")
"""
This function takes a word as input and returns the results from the getword function.
"""
from django.http import JsonResponse
from dictapi.dict.getword import getword

def getword(request, word):
    """
    Returns the results from the getword function.
    """
    results = getwordfromdb.getword(word)
    return JsonResponse(results, safe=False)
