from django.shortcuts import render


def main_index(request):
    return render(request, 'index.html')
