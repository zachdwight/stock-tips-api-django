# stock-tips-api-django
Quick introductory coding walkthrough utilizing Django (python &amp; REST) for small API.  Our goal is to return stock news with sentiment for cooler clustering downstream.  But for now, let's just setup the API.


### SETUP FROM SCRATCH

1 ] Create virtual environment
```
python3 -m venv myenv
source myenv/bin/activate
```
2 ] Install dependencies necessary (including Django)
```
pip install django djangorestframework requests beautifulsoup4
```
3 ] Create new project and components
```
django-admin startproject myproject
cd myproject
python manage.py startapp news
```
4 ] Copy the files here that are useful below into your app (or the whole repo and go with that)

- myproject/urls.py
- myproject/news/urls.py
- myproject/views.py

5 ] Run the server
```
python manage.py runserver
```
6 ] View results

http://127.0.0.1:8000/financial-news/

<img width="1160" alt="Screen Shot 2025-03-05 at 8 38 27 AM" src="https://github.com/user-attachments/assets/12a8a6a7-dfe6-429a-9165-d225eaf5c97c" />

