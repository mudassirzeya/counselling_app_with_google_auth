﻿# Counselling App with Google Login in Django
  This is a web-based counseling application built with Django, where users can sign up as either counselors or students. The app includes a Google login feature using OAuth2, allowing users to securely log in with their Google accounts. After logging in, students can submit queries about college admissions, and counselors can respond to these queries through an individual chat interface.

# WebApp Images 
![image](https://github.com/user-attachments/assets/56a4b983-92fb-4a46-9f81-c2ddddc216e2)
![image](https://github.com/user-attachments/assets/4c74f902-741c-4885-b846-4f0192f88e4e)
![image](https://github.com/user-attachments/assets/7888d18f-6ce4-4edc-b832-c342c62ec94c)
![image](https://github.com/user-attachments/assets/859159c4-cfa1-4d41-b2bc-979ef9e913f1)

# Features
1) Google OAuth2 Login: Users can log in securely using their Google accounts.
2) User Roles: Sign up as a counselor or a student.
3) Student Queries: Students can submit queries regarding college admissions.
4) Counselor Responses: Counselors can view a list of student queries and respond to them via an individual chat page.

# Technologies Used
1) Frontend: HTML, CSS, Bootstrap 4, JavaScript
2) Backend: Python, Django
3) Authentication: Google OAuth2

# Installation
  Follow these steps to set up the project locally.
  1) # Prerequisites
      1) Python 3.x
      2) Django
      3) pip (Python package installer)
      4) Virtualenv (optional but recommended)
  2) # Steps
      1) Clone the repository: git clone https://github.com/mudassirzeya/counselling_app_with_google_auth.git
      2) Set up a virtual environment (optional but recommended):
         1) python3 -m venv venv
         2) source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      3) Install the required dependencies:
         1) pip install django pillow
         2) pip install social-auth-app-django
      4) Set up Google OAuth2 credentials:
          1) Go to the Google Cloud Console.
          2) Select your project or create a new one.
          3) Navigate to APIs & Services > Library.
          4) Search for Google Identity Toolkit API.
          5) Click on it, and then click Enable.
      5) OAuth2 Credentials:
         1) After enabling the API, you'll need to create OAuth2 credentials (Client ID and Client Secret) which your Django app will use to authenticate users through Google.
      6) Create a .env file in the project root and add the following environment variables:
          1) SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<your-client-id>  ** in settings.py assign this client id by using os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') **
          2) SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<your-client-secret>  ** in settings.py assign this client secret key by using os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET') **
      7) Apply migrations: python manage.py migrate
      8) Create Superuser: python manage.py createsuperuser
      9) Run the development server: python manage.py runserver
  3) # Usage
      1) Login: On visiting the app, users are directed to a login page where they can log in using their Google account.
      2) Signup: After logging in, users can sign up as a counselor or a student.
      3) Submit Query (Students): Students can submit their queries related to college admissions.
      4) Respond to Queries (Counselors): Counselors can view a list of student queries and respond to them by visiting the student’s individual chat page.
      
      
         
