$(function () {
    var flagname = false;
    var flagpassword = false;

    $('#name').blur(function () {
        var name = $('#name').val();

        var reg = /^\w{3,6}$/;
        if (reg.test(name)) {
            $.getJSON('/axfuser/checkName/',
                {'name': name},
                function (data) {
                    if (data['status'] == 200) {
                        $('#nameinfo').html(data['msg']).css('color', 'green');
                        flagname = true
                    } else {
                        $('#nameinfo').html(data['msg']).css('color', 'red')
                    }
                }
            )
        } else {
            $('#nameinfo').html('用户名格式错误').css('color', 'red');
        }
    })

    $('#confirmpassword').blur(function () {
        var password = $('#password').val();
        var confirmpassword = $('#confirmpassword').val();
        if (password == confirmpassword) {
            $('#passwordinfo').html('密码无误').css('color', 'green');
            flagpassword = true
        } else {
            $('#passwordinfo').html('密码不一致').css('color', 'red')
        }
    })

    $('form').submit(function () {
        var name = $('#name').val();
        if (!name) {
            $('#nameinfo').html('用户名不能为空').css('color', 'red');
        }
        var password = $('#password').val()
        if (!password) {
            $('#pwd').html('密码不能为空').css('color', 'red');
        }
        var b = flagname & flagpassword;
        if (b == 0) {
            return false;
        } else {

        }
        var password = $('#password').val();
        var secret_password = md5(password);
        $('#password').val(secret_password)
        return true;

    })
})


