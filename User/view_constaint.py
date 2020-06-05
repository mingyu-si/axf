from django.core.cache import cache
from django.core.mail import send_mail
from django.template import loader


def send_email(name, token, email):
    subject = '来自爱鲜峰的邮件'
    message = '邮件激活'
    index = loader.get_template('axf/user/active.html')

    context = {
        'name': name,
        'url': 'http://127.0.0.1:8000/axfuser/account/?token=' + str(token)
    }

    result = index.render(context=context)
    html_message = result
    from_email = 'simingyu_mail@163.com'
    recipient_list = [email]
    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
