from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')