from django.shortcuts import render, redirect
from .models import Posta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Posta.objects.filter(publikatutako_data__lte=timezone.now()).order_by('publikatutako_data')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_pop(request, pk):
    post = get_object_or_404(Posta, pk=pk)
    return render(request, 'blog/post_pop.html', {'post': post})


def post_register(request):
    return render(request, 'blog/post_register.html')


'''def register_user(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('name') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('pass1'):
            user = auth_user()
            user.username = request.POST.get('username')
            user.first_name = request.POST.get('name')
            user.last_name = request.POST.get('lname')
            user.email = request.POST.get('email')
            user.password = request.POST.get('pass1')
            user.save()
            return render(request, 'blog/post_list.html')'''


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.publikatutako_data = timezone.now()
            post.save()
            return redirect(post_pop, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
