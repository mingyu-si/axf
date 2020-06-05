from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Cart.models import AxfCart
from Cart.view_containt import get_total_price


def cart(request):
    user_id = request.user_id
    carts = AxfCart.objects.filter(c_user_id=user_id)

    print('-----------------')
    print(carts)
    # 判断数据库中的选中状态，是否为全选，只有全部为选中状态，才会是True
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()

    total_price = get_total_price(user_id)
    context = {
        'carts': carts,
        'is_all_select': is_all_select,
        'total_price': total_price
    }
    return render(request, 'axf/main/cart/cart.html', context=context)


def addToCart(request):
    goodsid = request.GET.get('goodsid')

    user_id = request.user_id

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

    if carts.exists():
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num + 1

    else:
        cart = AxfCart()
        cart.c_goods_id = goodsid
        cart.c_user_id = user_id

    cart.save()

    data = {
        'status': 200,
        'msg': 'ok',
        'c_goods_num': cart.c_goods_num
    }

    return JsonResponse(data=data)


@csrf_exempt
def subToCart(request):
    cartid = request.POST.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)
    num = cart.c_goods_num

    user_id = request.session.get('user_id')

    # if num > 1:
    #     cart.c_goods_num = cart.c_goods_num - 1
    #     cart.save()
    #
    #     data = {
    #         'status': 200,
    #         'msg': 'ok',
    #         'c_goods_num': cart.c_goods_num
    #     }
    # else:
    #     cart.delete()
    #
    #     data = {
    #         'status': 200,
    #         'msg': 'ok',
    #         'c_goods_num': 0
    #         }

    data = {
        'status': 200,
        'msg': 'ok'
    }

    if num == 1:
        cart.delete()

    else:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num

    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)


def changestatus(request):
    cartid = request.GET.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)

    cart.c_is_select = not cart.c_is_select

    cart.save()

    user_id = request.session.get('user_id')
    # 在点击修改选中状态之后，再次去判断，数据库中是否为全部选中状态
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()

    data = {
        'msg': 'ok',
        'status': 200,
        'c_is_select': cart.c_is_select,
        'is_all_select': is_all_select,
        'total_price': get_total_price(user_id)
    }
    return JsonResponse(data=data)


def allselect(request):
    cartlist = request.GET.get('cartlist')

    card_list = cartlist.split('#')

    cart_list = AxfCart.objects.filter(id__in=card_list)

    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200,
        'total_price': get_total_price(user_id)
    }
    return JsonResponse(data=data)
