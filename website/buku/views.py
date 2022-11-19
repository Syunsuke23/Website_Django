from django.shortcuts import render

from.models import Post

# Create your views here.
def index(request):
    postingan = Post.objects.all()

    context = {
        'TampungPostingan' :postingan,
    }

    return render(request, 'buku/index.html', context)
