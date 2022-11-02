# Routes

## admin.py

Routes for admin functions. Utilizes Flask-login and Flask-security for login and role requirements for endpoints.

### /users

login required, admin role required.

Calls get_user_table function for user list and passes to templates/admin/users.html for table render

### /admin/user/new

login required, admin role required.

Provides form to templates/admin/new_user.html for rendering and returns data to add_user function on POST to add user.

### /admin/user/*user_id*/edit

login required, admin role required.

Provides form to templates/admin/edit_user.html for rendering and returns data to update_user function on POST to edit user based on user_id param in URL path.

### /admin/user/*user_id*/delete

login required, admin role required.

Calls delete_user_byID function to delete user on POST based on user_id param in URL path.

### /admin/user/*user_id*/view

login required, admin role required.

Calls a query to get a user object based on provided user_id in request path and passes to template/admin/view_user.html for rendering.

## auth.py

Provides routes for login and logout of user

### /auth/login

Determines if the current user is already logged in and redirects to dashboard page if true. Provides form for templates/auth/login.html and provides data on POST to Flask-Login package to login the user. 

### /auth/logout

Flask-login package function to logout user.

## dashboard.py

Provides routes for dashboard and main index redirect to dashboard

### /dashboard

Calls get_dashboard function to return dashboard items for templates/dashboard/dashboard.html to render.

## poams.py

Routes for poam functions. Utilizes Flask-login and Flask-security for login and role requirements for endpoints.

### /poams

login required. Any role allowed.

Calls get_poam_table function to return all poams for templates/poams/poams.html table render. 

### /poams/new

login required, admin or editor role required.

Provides form to templates/poam/new_poam.html for rendering and calls add_poam function on POST to add poam to database.

### /poams/*poam_id*/edit

login required, admin or editor role required.

Provides form to templates/poam/edit_poam.html for rendering and calls update_poam function to update the poam in the database.

### /poams/*poam_id*/delete

login required, admin or editor role required.

calls delete_poam_byID function providing poam_id to delete poam associated with primary key.

### /poams/*poam_id*/view

login required, admin or editor role required.

calls get_poam function to query for poam based on primary key and provided to templates/poams/view_poam.html for rendering of poam data.

## user.py

Provides all user routes for profile view and password update. Flask-security utilized for login required functionality.

### /user/profile

Renders templates/user/profile.html template to provide current user information based on Flask-login package functions

### /user/password

Provides form to templates/user/password.html for password change form. On POST passes form data to validate_and_updatePass function for password change.