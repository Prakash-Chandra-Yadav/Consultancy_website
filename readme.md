# Construction Company Website

A Django web application built for a construction company to establish their online presence. Projects, team members, and contact details are all managed through the Django admin panel without touching any code.

## Pages

**Home** is the main landing page. **About** lists team members pulled from the database. **Projects** shows every project uploaded through the admin, each with its own detail page auto-generated when a project is saved. **Contact** displays the company phone, email, and location.

## What can be managed from the admin

The company owner can log into `/admin/` and handle everything without a developer:

Adding a project just means filling in the title, description, date, and uploading an image. It shows up on the Projects page immediately with its own URL. Contact details like phone number, email, and office location can be updated at any time. Team member profiles on the About page can be added or removed, each with a name, position, experience level, and photo.

## Tech Stack

Python 3.12, Django, SQLite, Pillow for image handling.

## Project Structure

```
website/
├── django_project/          # Project-level configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── page/                    # Main application
│   ├── models.py            # Post, Contact, Professionals models
│   ├── views.py             # Function-based views for all pages
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin panel registration
│   ├── tests.py             # Automated test suite
│   └── migrations/
├── media/
│   ├── projects/
│   └── professionals/
└── manage.py
```

## Data Models

### Post (Projects)
Stores construction project entries uploaded by the admin.

| Field | Type | Description |
|---|---|---|
| title | CharField | Project title |
| body | TextField | Project description |
| author | ForeignKey (User) | Linked to Django's built-in User model |
| name | CharField | Display name |
| position | CharField | Role/position label |
| date | DateField | Project date |
| image | ImageField | Uploaded project image stored in `media/projects/` |

Each Post has a `get_absolute_url()` method that generates its own detail page URL automatically.

### Contact
Stores the company contact information, editable from the admin.

| Field | Type | Description |
|---|---|---|
| phone | CharField | Company phone number |
| email | EmailField | Company email address |
| location | CharField | Office location |

### Professionals
Stores team member profiles shown on the About page.

| Field | Type | Description |
|---|---|---|
| name | CharField | Team member name |
| position | CharField | Job title |
| experience | CharField | Experience level |
| image | ImageField | Profile photo stored in `media/professionals/` |

## URL Structure

| URL | View | Description |
|---|---|---|
| `/` | `homeview` | Home page |
| `/about/` | `aboutView` | About page with team members |
| `/contact/` | `contactview` | Contact page |
| `/projects/` | `projectview` | Lists all projects |
| `/projects/<pk>/` | `project_details` | Individual project detail page |
| `/admin/` | Django Admin | Content management panel |

## Setup

```bash
git clone <your-repo-url>
cd website

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` to manage content.

## Tests

```bash
python manage.py test page
```

| Test | What it checks |
|---|---|
| `test_post_model` | Post model stores title, body, and author correctly |
| `test_post_has_image` | Image field is populated and returns a valid URL ending in `.jpg` |
| `test_url_exists` | Home page returns HTTP 200 |
| `test_project_details` | Detail page returns 200 for a valid pk and 404 for a non-existent one |
| `test_project_detail_shows_image` | Detail page renders the uploaded image URL in the HTML |

Tests use `SimpleUploadedFile` to simulate image uploads without needing real files on disk.

## How to Add Content

Log into `/admin/` with your superuser credentials. To add a project, go to Posts, click Add Post, fill in the fields and upload an image, then save. It appears on the Projects page immediately. To update contact details, go to Contacts and edit the existing record. To add a team member, go to Professionals and add a new entry with a photo.

## Limitations

No pagination on the Projects page, so all projects load at once. The contact page is display only and does not have a form for visitors to send a message.

## What This Project Covers

This is the first complete Django project built from scratch. It covers Django app structure, function based views, model design with ForeignKey relationships and image uploads, dynamic URL routing with primary key parameters, Django ORM basics, admin panel setup for non-technical content management, and automated testing with model tests, URL status checks, template assertions, and simulated image uploads.
