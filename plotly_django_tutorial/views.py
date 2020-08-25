from django.shortcuts import render


def main_index(request):
    context = {}
    return render(request, 'index.html', context)
