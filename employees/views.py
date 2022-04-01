from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
""" Using function-based view """
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Employee


def index(request):
    object_list = Employee.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 3) # 3 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page_obj': page_obj})

""" Using class-based view """

# from django.views.generic import ListView

# from . models import Employee


# class Index(ListView):
#     model = Employee
#     context_object_name = 'employees'
#     paginate_by = 6
#     template_name = 'index.html'

""" Custom Middleware"""
def home(request):
    print("I am view for custom middleware")
    return HttpResponse("Custom middleware works")