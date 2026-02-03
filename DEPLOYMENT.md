# Deployment Guide

This guide covers how to deploy the E-commerce API to free hosting platforms.

## Option 1: Render (Recommended)

Render is the easiest way to deploy this project because we have already configured the necessary build scripts (`build.sh`) and settings.

### Prerequisites
1.  Push this project to a GitHub repository.

### Steps
1.  **Sign Up**: Go to [render.com](https://render.com/) and sign up/login with GitHub.
2.  **Create Web Service**:
    *   Click "New +" and select **Web Service**.
    *   Connect your GitHub repository.
3.  **Configure Service**:
    *   **Name**: Give your service a name (e.g., `ecommerce-api`).
    *   **Region**: Choose the one closest to you.
    *   **Branch**: `main` (or `master`).
    *   **Runtime**: `Python 3`.
    *   **Build Command**: `./build.sh`
    *   **Start Command**: `gunicorn ecommerce_project.wsgi:application`
    *   **Plan**: Select **Free**.
4.  **Environment Variables**:
    *   Scroll down to "Environment Variables" and add:
        *   `PYTHON_VERSION`: `3.9.18`
        *   `SECRET_KEY`: (Generate a random string)
        *   `DEBUG`: `False`
        *   `DATABASE_URL`: (See Database section below)
5.  **Database (PostgreSQL)**:
    *   In the Render Dashboard, click "New +" -> **PostgreSQL**.
    *   Name it (e.g., `ecommerce-db`).
    *   Select **Free** plan.
    *   Once created, copy the **Internal Database URL**.
    *   Go back to your Web Service -> Environment -> Edit.
    *   Add/Update `DATABASE_URL` with the value you copied.
6.  **Deploy**: Click "Create Web Service". Render will run the build script and start your app.

---

## Option 2: PythonAnywhere

PythonAnywhere provides a free tier specifically for Python hosting.

### Steps
1.  **Sign Up**: Go to [pythonanywhere.com](https://www.pythonanywhere.com/) and create a beginner account.
2.  **Upload Code**:
    *   Go to the **Bash** console.
    *   Clone your repository: `git clone https://github.com/your-username/your-repo.git`
3.  **Virtual Environment**:
    *   `cd your-repo`
    *   `mkvirtualenv --python=/usr/bin/python3.10 myenv`
    *   `pip install -r requirements.txt`
4.  **Web App Setup**:
    *   Go to the **Web** tab.
    *   Create a new web app -> Select **Manual configuration**.
    *   Select Python 3.10.
5.  **Configure WSGI**:
    *   In the Web tab, verify the **Virtualenv** path (e.g., `/home/yourusername/.virtualenvs/myenv`).
    *   Click on the **WSGI configuration file** link.
    *   Update it to point to your project:
        ```python
        import os
        import sys

        path = '/home/yourusername/your-repo'
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce_project.settings'

        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        ```
6.  **Static Files**:
    *   In the Web tab, under **Static files**:
    *   URL: `/static/`
    *   Directory: `/home/yourusername/your-repo/staticfiles` (Run `python manage.py collectstatic` in the console first).

---

## Option 3: Vercel (Serverless)

Vercel allows free hosting but requires adapting Django to run as serverless functions.

1.  Create a `vercel.json` file in the root:
    ```json
    {
      "builds": [{
        "src": "ecommerce_project/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
      }],
      "routes": [
        {
          "src": "/(.*)",
          "dest": "ecommerce_project/wsgi.py"
        }
      ]
    }
    ```
2.  Install Vercel CLI or connect via GitHub to deploy.
3.  **Note**: The free tier has limits on execution time (10s), which might be tight for some Django operations.
