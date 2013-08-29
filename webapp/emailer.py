

from django.template.loader import render_to_string
from requests import post


def send_email(from_email, to_email, subject, text, html):
    email_info = {
        'from_email': from_email,
        'to_email': to_email,
        'subject': subject,
        'text': text,
        'html': html,
        'api_key': 'd3d4a1cdc45f791ea525c942966b211da658ca3ae429a28bbc2f0bde'
    }

    r = post("https://appcubator.com/sendhostedemail/", data=email_info)
    assert r.status_code == 200, "Invalid email call"


def send_template_email(from_email, to_email, subject, text, template_file, request):
    user = request.user
    template_context = ({"User": user, "AppName": "Book face"})
    html = "<pre>%s</pre>" % render_to_string(template_file, template_context)
    email_info = {
        'from_email': from_email,
        'to_email': to_email,
        'subject': subject,
        'text': text,
        'html': html,
        'api_key': 'd3d4a1cdc45f791ea525c942966b211da658ca3ae429a28bbc2f0bde'
    }

    r = post("https://appcubator.com/sendhostedemail/", data=email_info)
    assert r.status_code == 200, "Invalid email call"
