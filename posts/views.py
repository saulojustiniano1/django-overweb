from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post


def home(request):
    return render(request, 'posts/home.html')


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'posts/post_create.html'
    success_url = '/posts/'
    permission_required = "posts.add_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pertence_ao_grupo'] = self.request.user.groups.filter(
            name='MOD').exists()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'posts/post_update.html'
    success_url = '/posts/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/posts/'


class PostListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if self.request.user and not self.request.user.groups.filter(name='USER'):
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
            print(queryset.query)
        orderby = self.request.GET.get('orderby', '-pub_date')
        return queryset.order_by(orderby)


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'


class CustomLogoutView(LogoutView):
    next_page = '/posts/'


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = '/login/'
