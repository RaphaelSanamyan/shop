from os import system

system("python -m venv venv")
system("venv\\Scripts\\activate")
system("pip install -r requirements.txt")
system("python manage.py run")
