# coding: utf-8

# Copyright Luna Technology 2014


from django.shortcuts import render


def landing(request):
    context = {}
    return render(request, 'templates/landing.html', context)
