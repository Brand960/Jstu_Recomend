"""
WSGI config for jstuLib project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
# 引入系统类
import os
from django.core.wsgi import get_wsgi_application
# 默认反向代理设置地址
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jstuLib.settings")

application = get_wsgi_application()
