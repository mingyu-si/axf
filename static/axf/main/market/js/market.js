$(function () {
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-menu-down glyphicon glyphicon-menu-up')
        $('#all_type_container').toggle();
    })
})

$(function () {
    $('#all_sort').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-menu-down glyphicon glyphicon-menu-up')
        $('#all_sort_container').toggle();
    })


})

// //自定义属性
// var goodsid = $button.attr('goodsid');
// //系统自带的
// var $class = $button.prop('class');
//
// alert(goodsid);
// alert($class);

// var $goodsid = $button.prop('goodsid');
//
// var $class = $button.attr('class');
//
// alert($goodsid);
// alert($class);

//    attr方法可以获取自定义属性 也可以获取标签自带的属性
//    prop方法可以获取标签自带的属性 而不可以获取自定义属性
$(function () {
    $('.addToCart').click(function () {
        //获取goodsid
        var $button = $(this);

        var goodsid = $button.attr('goodsid');


        $.get('/axfcart/addToCart/',
            {'goodsid': goodsid},
            function (data) {
                if (data['status'] == 200) {
                    //button标签的上一个标签
                    $button.prev().html(data['c_goods_num']);
                }else {
                    window.location.href = '/axfuser/login/'
                }
            })

    })
})

