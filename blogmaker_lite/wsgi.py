import os

from django.core.wsgi import get_wsgi_application

# handles incoming request and gives appropriate response
os.environ["DJANGO_SETTINGS_MODULE"] = "blogmaker_lite.settings"
application = get_wsgi_application()
