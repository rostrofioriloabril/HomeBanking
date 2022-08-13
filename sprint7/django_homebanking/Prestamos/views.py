from django.shortcuts import render
from . forms import PrestamosForm

# Create your views here.

def prestamos(request):
    forms=PrestamosForm()
    return render(request, "Prestamos/prestamos.html", {'form': forms})


'''
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': forms})
'''