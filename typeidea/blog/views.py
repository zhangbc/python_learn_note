from blog.models import Category, Post
from config.models import SideBar
from django.shortcuts import render


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
