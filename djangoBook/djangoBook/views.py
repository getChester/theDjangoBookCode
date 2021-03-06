from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import datetime

def hello(request):
    return HttpResponse("Hello World!!!!")
    
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    # html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hours_ahead.html')
    html = t.render(Context({'hour_offset': offset, 'next_time': dt}))
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)