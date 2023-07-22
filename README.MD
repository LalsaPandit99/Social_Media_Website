Steps to run this project
1. Create a directory using following command:
mkdir socialMediaWebsite

2. go into this directory using following command:
cd socialMediaWebsite

3. create virtual environemtn using following command:
python -m venv socialMediaWebsite

4. Activate the enviroment create in step 3
socialMediaWebsiteVens/ Scripts/activate.ps1

5. install django and pillow in this environemnt
pip install django or pip3 install django
pip install  or pip3 install django

6. go to the folder of this application

7. To create superuser: python manage.py createsuperuser

8. To run server: python manage.py runserver

------
Link Views and Templates,
* Create a view
* Add path related to view in urls.py
* Create template
* Link template with view

Models,
* Create models
* Register the model in admin.py
* Run makemigrations,- python manage.py makemigrations
* Run migrate   - python manage.py migrate

-----------
create a view which require user login and that views should list down all the posts in the websites
------------------------
create a models

* create a class which should be inheritad from models.Model
* Decide 