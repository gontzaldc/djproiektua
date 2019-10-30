from django.shortcuts import render
from .models import Posta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.
def post_list(request):
    posts = Posta.objects.filter(publikatutako_data__lte=timezone.now()).order_by('publikatutako_data')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_pop(request, pk):
    post = get_object_or_404(Posta, pk=pk)
    return render(request, 'blog/post_pop.html', {'post': post})
