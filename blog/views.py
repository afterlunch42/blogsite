from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Count
from .models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count

# Create your views here.
EACH_PAGE_BLOGS_NUMBER = 5


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    if paginator.num_pages > 1:  # 处理分类下无内容情况
        page_range = [i for i in range(current_page_num - 2, current_page_num + 3) if 0 < i < paginator.num_pages]
        if page_range[0] - 1 >= 2:  # 前省略
            page_range.insert(0, "...")
        if paginator.num_pages - page_range[-1] >= 2:  # 后成略
            page_range.append("...")
        if page_range[0] is not 1:  # 添加首页
            page_range.insert(0, 1)
        if page_range[-1] is not paginator.num_pages:  # 添加尾页
            page_range.append(paginator.num_pages)
    else:
        page_range = [1]
    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('create_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(create_time__year=blog_date.year, create_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] =blog_count
    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_dates'] = blog_dates_dict  # 通过遍历进行计数再添加到字典中实现
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))  # 使用annotate添加blog_count属性
    return context


def blog_list(request):  # 博客列表
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response('blog_list.html', context)


def blog_with_type(request, blog_type_pk):  # 按种类筛选出需要显示的博客种类

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blog_type_list = Blog.objects.filter(blog_type=blog_type)  # 添加筛选
    context = get_blog_list_common_data(request, blog_type_list)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html', context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(create_time__year=year, create_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_type'] = '{}年{}月'.format(year, month)
    return render_to_response('blogs_with_type.html', context)


def blog_detail(request, blog_pk):  # 博客详情
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(create_time__gt=blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt=blog.create_time).first()
    return render_to_response('blog_detail.html', context)
