from blog.models import Post, Tag
from django.shortcuts import render


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            plist = list()
        else:
            plist = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        plist = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            plist = plist.filter(category_id=category_id)

    return render(request, 'blog/list.html',
                  context={'post_list': plist})


def post_detail(request, post_id=None):
    try:
        p = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        p = None

    return render(request, 'blog/detail.html',
                  context={'post': p})
