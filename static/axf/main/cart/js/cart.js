$(function () {
    $('.subToCart').click(function () {
        var $button = $(this);

        var $div = $button.parent().parent();

        var cartid = $div.attr('cartid');
        // alert(cartid)
        $.post('/axfcart/subToCart/',
            {'cartid': cartid},
            function (data) {
                if (data['status'] == 200) {
                    if (data['c_goods_num'] >= 1) {
                        $button.next().html(data['c_goods_num'])
                    } else {
                        $div.remove()
                    }
                    $('#total_price').html(data['total_price'])

                }
            })
    })

    $('.confirm').click(function () {
        var $confirm = $(this);
        var $div = $confirm.parent()
        var cartid = $div.attr('cartid')

        $.ajax(
            {
                url: '/axfcart/changeStatus/',
                data: {'cartid': cartid},
                type: 'Get',
                dataType: 'JSON',
                success: function (data) {
                    if (data['c_is_select']) {
                        $confirm.find('span').find('span').html('✔')
                    } else {
                        $confirm.find('span').find('span').html('')
                    }
                    if (data['is_all_select']) {
                        $('#all_select').find('span').find('span').html('✔')
                    } else {
                        $('#all_select').find('span').find('span').html('')
                    }
                    $('#total_price').html(data['total_price'])
                }
            }
        )
    })

    $('#all_select').click(function () {
        //  1.要将当前要用户的购物车的选中的cartid放到一个列表，未选中的cartid放到一个列表
        //  2.如果未选中的列表长度大于0   证明有未被选中的    所以将此列表中的对应的对象修改为选中
        //  3.否则证明此时全部被选中了    那么就要将列表对应的对象修改为未被选中
        var select_list = [];
        var unselect_list = [];
        var $confirm = $('.confirm')

        //  遍历confirm
        $confirm.each(function () {
            //$(this)一个又一个的div对象
            var $div = $(this);
            var cartid = $div.parent().attr('cartid');
            //html()会判断标签中有没有内容，如果有内容，返回true，如果没有返回false
            if ($div.find('span').find('span').html()) {
                select_list.push(cartid)
            } else {
                unselect_list.push(cartid)
            }
        })
        if (unselect_list.length > 0) {
            $.getJSON('/axfcart/allselect/',
                //ajax的参数 不可以传递列表
                //join方法会将列表中所有的元素拼接
                {'cartlist': unselect_list.join('#')},
                function (data) {
                    if (data['status'] == 200) {
                        $confirm.find('span').find('span').html('✔');
                        $('#all_select').find('span').find('span').html('✔');
                        $('#total_price').html(data['total_price'])
                    }
                })
        } else {
            $.getJSON('/axfcart/allselect/',
                {'cartlist': select_list.join('#')},
                function (data) {
                    if (data['status'] == 200) {
                        $confirm.find('span').find('span').html('');
                        $('#all_select').find('span').find('span').html('');
                        $('#total_price').html(data['total_price'])
                    }
                })


        }
    })

    $('#make_order').click(function () {
        //  判断购物车是否有选中的，如果有选中则存储到订单商品
        //  如果没有被选中的    那么就退出方法
        var select_list = [];
        var unselect_list = [];

        var $confirm = $('.confirm');

        $confirm.each(function () {
            var $div = $(this);

            var cartid = $div.parent().attr('cartid');

            if ($div.find('span').find('span').html()) {
                select_list.push(cartid)
            } else {
                unselect_list.push(cartid)
            }
        })
        if (select_list.length == 0) {
            //当遇到return的时候 那么方法将直接返回 不在继续执行
            return;
        }

        $.post('/axforder/makeOrder/',
            function (data) {
               if(data['status'] == 200){
                   window.location.href = '/axforder/orderDetail/?order_id='+ data['order_id']
               }else {
                   window.location.href = 'axfuser/login/'
               }
            })

    })


})




