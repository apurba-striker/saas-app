from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit


this_dir = pathlib.Path(__file__).resolve().parent



def home_page_view(request, *args, **kwargs):
    
    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path= request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count": qs.count(),
    }
    html_template= "home.html"
    PageVisit.objects.create()
    return render(request, html_template,my_context)
    