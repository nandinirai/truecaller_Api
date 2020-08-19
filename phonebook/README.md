Instructions To RUN:
### cd to phonebook directory ###
#### use this to run migration ####
$ python manage.py makemigrations
$ python manage.py migrate

##### use this to create superuser ####
$ python manage.py createsuperuser
-> You'll be asked to enter username, email and password. Please do that!

##### use this to run server ####
python manage.py runserver
-> Now navigate to http://127.0.0.1:8000/admin/
-> Enter your username and password

#### Click on contacts to save new contacts and mark them as spam etc ####
#### Click on user contact mapping to select the contact associated with the user ####
#### Click on userprofiles to create your profile using contact number ###