from django.shortcuts import render_to_response


def home(request):  # 主页
    context = {}
    return render_to_response('home.html', context)
