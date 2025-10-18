Deploy to Render (step-by-step)

1. Create a GitHub repository and push this project.
2. On https://render.com, create a new Web Service -> Connect to GitHub repo.
3. Choose branch (main/master).
4. Build Command: (leave empty) Render will run pip install -r requirements.txt
5. Start Command: gunicorn mosk_pdk.wsgi
6. In Render dashboard, create a Postgres database (Add > Postgres).
7. Copy DATABASE URL from the database settings and add it as an Environment Variable named DATABASE_URL for your Web Service.
8. In the web service settings, set the environment variable DEBUG=0 for production and optionally DJANGO_SECRET_KEY.
9. Deploy; after build, go to the service URL.
10. Run migrations (you can use Render's Shell or run manage.py migrate locally before push):
    python manage.py migrate
11. Create superuser:
    python manage.py createsuperuser
