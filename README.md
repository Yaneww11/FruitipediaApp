# Fruitipedia App

## Overview

The **Fruitipedia App** is a web application developed using Django, designed to provide users with a comprehensive database of fruits. The app allows users to create, view, edit, and delete entries for different fruits, categorized by their type. This project was part of a hands-on workshop aimed at teaching Python ORM concepts, web development with Django, and templating at Software University.

## Project Structure

- **Django Project:** `fruitipediaApp`
- **App Name:** `fruits`

## Key Features

### 1. Project Setup & Configuration
- Created the Django project `fruitipediaApp` and set up the `fruits` app.
- Integrated provided HTML templates, images, and CSS files.
- Configured static files and templates in Django settings.
- Managed URL routing for loading specific templates for each app.

### 2. Database Design
- **Category Model:**
  - Character field, required, with unique constraints.
- **Fruit Model:**
  - Fields: `name`, `image_url`, `description`, `nutrition`.
  - Validation for `name`: Only letters allowed; raises `ValidationError` if the rule is violated.

### 3. Frontend Pages
- **Index Page (`index.html`):** 
  - Navigation to "Create Category", "Create Fruit", and "Dashboard".
  
- **Dashboard Page (`dashboard.html`):** 
  - Displays all created fruits or a message if no fruits are available.
  
- **Create Category Page (`create-category.html`):** 
  - Form for adding new categories with validation.
  
- **Create Fruit Page (`create-fruit.html`):** 
  - Form for adding new fruits with validation.
  
- **Fruit Details Page (`details-fruit.html`):**
  - Displays detailed information about a fruit with "Edit" and "Delete" options.
  
- **Edit/Delete Fruit Pages (`edit-fruit.html`, `delete-fruit.html`):**
  - Forms pre-filled with fruit data for editing or confirming deletion.

### 4. Template Inheritance
- Created a base template `base.html` for common components like the header, footer, and navigation bar.
- Extended `base.html` across all other templates to maintain consistency and reduce redundancy.

### 5. Views and URL Routing
- Developed views to handle HTTP requests for creating, viewing, editing, and deleting fruits.
- Configured URL patterns to map specific URLs to corresponding views.

## Technologies Used
- **Backend:** Django, Python
- **Frontend:** HTML, CSS
- **Database:** Postgres (Django ORM)
- **Tools:** Git, PyCharm

## Outcome
The **Fruitipedia App** successfully demonstrates the use of Django ORM, template inheritance, and full-stack development using Django. The project serves as a practical example of creating a scalable and maintainable web application with Django.

---

This project was developed as part of the Python ORM course at [Software University](https://softuni.bg).
