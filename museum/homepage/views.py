from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, TemplateView,  ListView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    template_name = 'homepage/homepage.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        post_to_view = Post.objects.select_main()
        post_to_view = post_to_view[len(post_to_view) - 3:len(post_to_view)] if len(post_to_view) - 3 >= 0 else []
        return post_to_view


class PostListView(ListView):
    template_name = 'homepage/post_list.html'
    paginate_by = 2
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.select_main()



class PostView(DetailView):
    model = Post
    template_name = 'homepage/post.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'homepage/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        for tag in form.cleaned_data['tags']:
            post.tags.add(tag)
        return redirect('homepage:home')

    def form_invalid(self, form):
        return render(self.request, 'homepage/create_post.html',
                      {'form': form})
