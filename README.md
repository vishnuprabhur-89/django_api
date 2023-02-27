# django_api
LMS api 



# LMS api 
pip install django==4.1.0                                   - install django project
django-admin startproject projectName                       - create project 
python manage.py appName                                    - create application inside project
python manage.py runserver                                  - start the server
python manage.py createsuperuser                            - to create admin user credintials
python manage.py makemigrations appName                     - define model migration 
python manage.py migrate 

API DETAILS

POST - ADD STUDENT                     = localhost:8000/add/student/ 
GET  - FETCH STUDENT                   = localhost:8000/add/student?page=1&limit=2

1. - Add marks for n subjects (Eg: n = 5, no of subjects) for a student
POST - ADD STUDENT MARKS               = localhost:8000/student/marks/

2. - view a student marks details
GET  - FETCH ALL STUDENT MARKS         = localhost:8000/student/marks/?page=1&limit=20&searchType=student

3. - view the list of students with their total marks
GET - FETCH ALL STUDENT TOTAL MARKS    = localhost:8000/student/marks/?page=1&limit=20&searchType=totalmarks

4. - view Average marks scored by all the students for each subject
GET - localhost:8000/average/marks/
