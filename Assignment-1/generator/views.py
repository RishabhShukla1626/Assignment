from django.shortcuts import render
import string_utils
import random


# Create your views here.
def generator(request):
    return render(request, 'generator/index.html')

def password(request):
    
    password = ''
    length = 0
    lower_case = list('abcdefghijklmnopqrstuvwxyz')
    upper_case = list('abcdefghijklmnopqrstuvwxyz'.upper())
    number = list('1234567890')
    special_chars = list('!@#$%^&*()_+?<>\|')

    if request.GET.get('uppercase'):
        uppercase_length = int(request.GET.get('uppercase_length'))
        length += uppercase_length
        for char in range(uppercase_length):    
            password += random.choice(upper_case)

    if request.GET.get('lowercase'):
        lower_length = int(request.GET.get('lowercase_length'))
        length += lower_length
        for char in range(lower_length):    
            password += random.choice(lower_case)

    if request.GET.get('numbers'):
        numbers_length = int(request.GET.get('numbers_length')[0])
        length += numbers_length
        for char in range(numbers_length):    
            password += random.choice(number)

    if request.GET.get('specialchars'):
        specialchar_length = int(request.GET.get('specialchar_length')[0])
        length += specialchar_length
        for char in range(specialchar_length):    
            password += random.choice(special_chars)

    if length > 11 and length < 39:
        password = string_utils.shuffle(password)
        return render(request, 'generator/password.html', {"password": password})
    return render(request, 'generator/index.html', {"error": 'An error occured'})