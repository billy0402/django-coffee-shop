from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import RequestContext


def permission_denied(request, exception, template_name='403.html'):
    messages.warning(request, '權限不足')
    return redirect('root')


def page_not_found(request, exception, template_name='404.html'):
    return render(request, 'errors/404.html', status=404)
