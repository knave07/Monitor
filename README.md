# Monitor
What it Does :It gets the information of employee by tracking his/her MAC address and keeps track on his/her presence within the area of the company.

How to Set Up the server:

First UNZIP/MOVE the file in your Document Directory. 

Open terminal and locate to Document/moniter/SourceCode/

Run these commands to setup project and database:

python manage.py makemigrations getdata

python manage.py makemigrations employee

python manage.py migrate


Run these commands to create Admin User:

python manage.py createsuperuser

Then provide your information which will be used for your admin login.

Check your IP address of router to which you are connected.

In our case we have hardcoded this IP as ‘10.42.0.’ in line 22 of file main.py of SourceCode which you will have to change.

In our case we have taken 10 minutes to moniter you can type how much minutes you want to keep track in line 37 you have to fill the minutes.

