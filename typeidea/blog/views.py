from blog.models import Category, Post, Tag
from config.models import SideBar
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        plist, tag = Post.get_by_tag(tag_id)
    elif category_id:
        plist, category = Post.get_by_category(category_id)
    else:
        plist = Post.lasted_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': plist,
        'sidebars': SideBar.get_all(),
    }

    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        p = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        p = None

    context = {
        'post': p,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'blog/detail.html', context=context)


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })

        context.update(Category.get_navs())

        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.lasted_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.lasted_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
