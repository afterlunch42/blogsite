from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path("<int:blog_pk>", views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blog_with_type, name='blogs_with_type'),  # 根据标签筛选
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),  # 根据日期筛选
]
