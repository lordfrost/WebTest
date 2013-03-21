from django.template import loader, Context
from django.http import  HttpResponse
from doit.models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("first")
    c = Context({'posts' : posts})
    return HttpResponse(t.render(c))