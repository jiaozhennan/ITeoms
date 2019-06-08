import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'qdzzzc.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.qdzzzc.com的测试邮件', 'jiaozn110@sina.com', '395288550@qq.com'
    text_content = '欢迎访问www.qdzzzc.com，青岛中资中程集团股份有限公司！'
    html_content = '<p>欢迎访问<a href="http://www.qdzzzc.com" target=blank>www.qdzzzc.com</a>，青岛中资中程集团股份有限公司！！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()