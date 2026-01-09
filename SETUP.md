# Django REST Authentication API (Production-Ready JWT)

## 1. Environment Setup

```bash
# (Recommended) Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Django, Django REST Framework, and SimpleJWT (with blacklist support):
pip install Django djangorestframework djangorestframework-simplejwt
```

## 2. Project and App Initialization

```bash
# (Skip if project already exists)
django-admin startproject moralreport .

# Create the accounts app for authentication logic:
python manage.py startapp accounts
```

## 3. Project Structure

```
your_project/
├── accounts/
│   ├── models.py          # Custom User
│   ├── serializers.py     # SignUp, JWT, Password validation
│   ├── views.py           # RegisterView, LoginView, RefreshView
│   └── urls.py            # Route endpoints
├── moralreport/
│   ├── settings.py        # Add apps, configure DRF & JWT
│   └── urls.py            # Include accounts.urls
... (other files)
```

## 4. settings.py Modifications

- Add these to `INSTALLED_APPS`:
  ```python
  'rest_framework',
  'rest_framework_simplejwt.token_blacklist',
  'accounts',
  ```

- Declare custom user model:
  ```python
  AUTH_USER_MODEL = 'accounts.User'
  ```

- Configure DRF to use JWT, and production-grade SimpleJWT settings:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
  }

  from datetime import timedelta
  SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
      'ROTATE_REFRESH_TOKENS': True,
      'BLACKLIST_AFTER_ROTATION': True,
      'AUTH_HEADER_TYPES': ('Bearer',),
      'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
      'TOKEN_OBTAIN_SERIALIZER': 'accounts.serializers.MyTokenObtainPairSerializer',
  }
  ```

## 5. Development Steps

1. **Custom User Model:**
    - Create `accounts/models.py` extending `AbstractUser`.
    - Run migrations **before adding any users**:
      ```bash
      python manage.py makemigrations accounts
      python manage.py migrate
      ```
2. **Serializers:**
    - Implement `RegisterSerializer` (with strict password validation/checks and confirmation).
    - Implement `MyTokenObtainPairSerializer` (for custom login responses).
3. **Views:**
    - Create `RegisterView`, `LoginView` (JWT obtain pair), and `RefreshTokenView`.
4. **URLs:**
    - Wire up URLs (`accounts/urls.py`), then include in project `urls.py`:
      ```python
      path('auth/', include('accounts.urls')),
      ```
5. **DRF, SimpleJWT, and App settings** (see above).

6. **Testing (Example):**
    - `POST /auth/sign-up/` — `{ "username": ..., "email": ..., "password": ..., "password2": ... }`
    - `POST /auth/login/` — `{ "username": ..., "password": ... }` returns both `access` and `refresh` tokens
    - `POST /auth/refresh-token/` — `{ "refresh": ... }` returns new `access` (and refresh, if rotated)

## 6. Installed Dependency List

- **Django**: Leading secure, scalable Python web framework
- **djangorestframework**: Powerful, extensible REST API toolkit for Django
- **djangorestframework-simplejwt**: Secure JWT (JSON Web Token) authentication, including token rotation and blacklist functionality—critical for stateless, production APIs

## 7. Security Best Practices in This Setup
- All password validation done via Django's industry-standard validators
- Registration requires strong/unique passwords and confirmation
- JWT rotation/blacklisting prevents reuse of stolen tokens
- Only relevant data is returned in login and refresh responses
- Custom user model enables future extensibility (email login, extra fields, etc)

---

This setup delivers robust JWT authentication suitable for modern, stateless, production-grade Django projects.
