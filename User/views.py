import uuid
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL import ImageFont
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from User.models import AxfUser
from User.view_constaint import send_email
from axf import settings


def login(request):
    if request.method == 'GET':
        return render(request, 'axf/user/login.html')
    else:
        # 先判断验证码是否正确
        # 然后判断用户名和密码(减少数据库的读取操作)
        imgcode = request.POST.get('imgcode')
        imgcode1 = request.session.get('verify_code')

        if imgcode.lower() == imgcode1.lower():
            name = request.POST.get('name')
            users = AxfUser.objects.filter(name=name)

            if users.exists():
                user = users.first()
                password = request.POST.get('password')

                result = check_password(password, user.password)
                if result:
                    if user.active == 1:
                        request.session['user_id'] = user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        context = {
                            'msg': '账号未激活'
                        }
                        return render(request, 'axf/user/login.html', context=context)
                else:
                    context = {
                        'msg': '密码输入错误'
                    }
                    return render(request, 'axf/user/login.html', context=context)
            else:
                context = {
                    'msg': '用户名输入错误'
                }
                return render(request, 'axf/user/login.html', context=context)
        else:
            context = {
                'msg': '验证码输入错误'
            }
            return render(request, 'axf/user/login.html', context=context)


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        new_password = make_password(password)

        user = AxfUser()

        user.name = name
        user.password = new_password
        user.email = email
        user.icon = icon

        token = uuid.uuid4()
        user.token = token
        user.save()

        cache.set(token, user.id, timeout=60)

        send_email(name, token, email)
        return redirect(reverse('axfuser:login'))


def checkName(request):
    # 注册时检查用户名是否可以使用
    name = request.GET.get('name')
    users = AxfUser.objects.filter(name=name)

    data = {
        'msg': '用户名可以使用',
        'status': 200
    }
    if users.count() > 0:
        data['msg'] = '用户名已存在'
        data['status'] = 201
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def account(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    name = request.GET.get('name')
    print(name)

    if user_id:
        user = AxfUser.objects.filter(token=token)[0]

        user.active = True
        user.save()
        # 将缓存中的token删除，以免多次激活
        cache.delete(token)

        return HttpResponse('激活成功')

    # elif request.GET.get('')

    else:
        return HttpResponse('邮件已过期，请重新发送！！！')


def get_code(request):
    # 登入时，第一步检查验证码
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (250, 50)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 50)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(40 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(1000):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):
    request.session.flush()
    return redirect(reverse('axfuser:login'))
