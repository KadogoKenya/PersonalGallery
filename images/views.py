from django.shortcuts import render,redirect
from django.http  import HttpResponse
# import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image,Location

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def images_of_day(request):
    # date = dt.date.today()
  
    images = Image.todays_images()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    # day = convert_dates(date)
    
    return render(request,'all-images/today-images.html',{"images":images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_images(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_of_day)

        images = Image.days_images(date)

    return render(request, 'all-images/past-images.html', {"date": date, "images":images})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})