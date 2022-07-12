import os, sys
 
#project directory
sys.path.append('/home/p/printadj/stroyrempiter.rf/public_html/venv/lib/python3.9/site-packages')
sys.path.append('/home/p/printadj/stroyrempiter.rf/public_html')
 
#project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myRoom.settings")
 
#start server
 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
