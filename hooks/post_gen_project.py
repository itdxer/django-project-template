import os


os.system('pip install -r requirements/development.txt')
os.system('./manage.py syncdb --noinput')
os.system('./manage.py migrate --noinput')
os.system('./manage.py loaddata user')
