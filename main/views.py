from django.shortcuts import render, reverse, redirect
from django.conf import settings
from .mixins import FormErrors, RedirectParams, APIMixin

'''
Basic view for selecting query
'''
def index(request):
    if request.method == "POST":
        cat = request.POST.get("cat", None)
        query = request.POST.get("query", None)
        if cat and query:
            return RedirectParams(url='main:results', params={"cat": cat, "query": query})

    return render(request, 'main/index.html', {})

'''
Basic view for displaying results
'''
def results(request):
    cat = request.GET.get("cat", None)
    query = request.GET.get("query", None)

    if cat and query:
        results = APIMixin(cat=cat, query=query).get_data()

        if results:
            context = {
                "results": results,
                "cat": cat,
                "query": query,
            }
            return render(request, 'main/results.html', context)
    return redirect(reverse('main:home'))

'''
View for displaying details of a selected item
'''
def detail(request, id):
    cat = request.GET.get("cat", None)

    if cat and id:
        detail = APIMixin(cat=cat, id=id).get_detail_data()

        if detail:
            context = {
                "detail": detail,
                "cat": cat,
            }
            return render(request, 'main/detail.html', context)

    return redirect(reverse('main:home'))
