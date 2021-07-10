from blog.adminforms import PostAdminForm
from blog.models import Category, Post, Tag
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline]

    @staticmethod
    def post_count(obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """
    自定义过滤器只展示当前用户分类
    """

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """返回要展示 的内容和l查询用的 id"""

        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        """根据 URL Query 的内容返 回列表页数据"""

        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())

        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm
    list_display = ('title', 'category', 'owner', 'status', 'created_time', 'operator')
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = False

    save_on_top = True

    exclude = ('owner', )
    # 作用：1）限定要展示的字段；2）配置展示字段的顺序。
    # fields = (('category', 'title'), 'desc', 'status', 'content', 'tag')

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            )
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': ('tag', ),
        })
    )

    filter_horizontal = ('tag', )

    @staticmethod
    def operator(obj):
        return format_html(
            '<a href="{}">编 辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj, ))
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }

        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.bundle.js', )
