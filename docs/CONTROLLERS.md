# Controllers

## admin.py

Provides admin functionality of handling users.

### get_user_table(page, count)

Queries the database for all users. The results are returned as a pagination group to allow for a multiple page table to be rendered. 

**page** - current page request parameter

**count** - number of users per page

### update_user(user_id, form)

Provides update functionality to update database with new username, role, or set the user to active. Returns if successful or not message.

**user_id** - provided primary key of user for updates

**form** - provided edit user form data

### add_user(form)

Provides add user functionality from add user page. Returns if successful or not message.

**form** - provided add user form data

### get_user(user_id)

Queries the database for a selected user. Returns user model.

**user_id** - Primary key of user for query

### delete_user_byID(user_id)

Deletes a user from the database. Returns if successful or not message.

**user_id** - Primary key of user for deletion

## auth.py

Provides login functions

### is_safe_url(target)

Validation of next parameter to limit open redirects.

**target** - next parameter

### get_user(username)

Determines if a user is present in the database for login.

**username** - Username string

### check_password(user, password)

Checks that password provided matches password in database

### load_user(user_id)

Flask-Login package function to determine if user is logged in before accessing a page

**user_id** primary key of user

### unauthorized()

Provides redirection if user is not logged in and needs permissions to view page

## init_db.py

Provides initial database creation and ability to generate test data in the database for demo purposes.

### init_db()

Creates initial database schema and commits roles and default admin/admin user to database.

### init_test_load()

Creates a editor/editor and user/user user to the database. Also creates 25 random users and 40 random poams with various dates for dashboard information.

## poams.py

Provides Admin or Editor add, update, delete poam functionality

### get_poam_table(page, count)

Queries the database for all POAMs and returns a pagination object for multiple page results

**page** - current page request parameter

**count** - number of requests to display on page

### delete_poam_byID(poam_id):

Deletes a POAM from the database and returns a successful or non-successful message

**poam_id** - primary key of poam to delete

### get_dashboard(page)

Generates the dashboard data. Calls functions to get total POAMS by threat level, POAMS past defined SLA marks, any new over the past 7 days to display in the table, and information for the trend chart.

**page** - current page request parameter for table pagination

### get_poam_count_byThreat(threat_level)

Queries database for all POAMs by threat level and returns count.

**threat_level** - High, Medium, Low threat level to query

### get_poam_count_pastSla(threat_level, sla_days)

Queries database for POAMs based on threat level and how many days past SLA defined days.

**threat_level** - High, Medium, Low threat level to query

**sla_days** - Days defined as SLA breach

### get_poams_rangeToNow(page, days)

Queries database for all poams within a defined day range and returns pagination object.

**page** - current page request parameter

**days** - number of days until today to pull POAMs for

### get_chart_months()

Determine todays month and returns previous 6 months

### get_total_poams_byMonth(months, threat_level)

Get total poams based on threat level for the month and return total.

**months** - array of months to query

**threat_level** - High, Medium, Low threat level to query

### get_poam(poam_id)

Query database for POAM by primary key and return poam object

**poam_id** - primary key of POAM

### update_poam(poam, form)

Update the POAM in the database based on form data on edit page. Returns successful or non-successful message.

**poam** - poam object to update

**form** - edit POAM form data

### add_poam(form)

Add a POAM to the database. Returns successful or non-successful message.

## user.py

Provides user functionality such as change password

### validate_and_updatePass(old, new)

Change user password. Returns successful or non-successful message.

**old** - old password

**new** - new password