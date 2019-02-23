from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogType(models.Model):  # 博客分类
    type_name = models.CharField(max_length=15)

    def __str__(self):  # 显示博客分类的字符内容
        return self.type_name


class Blog(models.Model):  # 博文
    title = models.CharField(max_length=80)  # 标题 字符串类型 长度限制50
    content = models.TextField()  # 内容 长文本类型
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)  # 通过外键使用上方的BlogType
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 作者 通过外键使用User
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间 自动填充时间
    last_updated_time = models.DateTimeField(auto_now=True)  # 最后修改时间 自动填充

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
