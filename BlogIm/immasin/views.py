from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post, Contact, Slide1



class FutView(ListView):
    model = Post
    template_name = 'futer.html'



class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'

def contact_us(request):
    if request.POST:
        new_contact = Contact.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            message=request.POST['message']
        )

    return render(request, "contact us.html", {})


def HomeView(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'home.html', context)



def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        pos = Post.objects.filter(title__contains=searched)

        return render(request, 'search_venues.html', {'searched':searched, 'pos':pos})
    else:
       return render(request, 'search_venues.html', {})






def allpost(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'allpost.html', context)




def aboutme(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'aboutme.html', context)


def handle_not_found(request, exception):
    return render(request, 'not-found.html')