# OWAP TOP 10 mitigations

## A01:2021 – Broken Access Control

In order to mitigate broken access control the Flask package Flask-Login and Flask-Security have been implemented to provide checks to ensure that a user is logged in or has the appropriate role if logged in to view specific pages within the webapp. These are called by providing @login-required and @role-required on routes as needed.

## A02:2021 – Cryptographic Failures

It is assumed a proxy providing SSL termination between the user and the webapp will handle secure transmission of data. The Talisman package is used to provide secure headers when deployed in production. Password hashes in the database are being generated using Flask-Security and configured by default in the config to use pbkdf2 SHA512 with a salt as well. Session cookies are generated using a secret key which is also configured in the default configuration. 

## A03:2021 – Injection 

SQLi is mitigated by the use of Flask-SQLAlchemy package in order to provide ORM functionality and injection protection against user inputs to the system. 

## A04:2021 – Insecure Design

A secure SDLC is established to evaluate design security throughout the Webapp development. Python libraries are defined in the requirements.txt file so that they can be referrenced to applicable versions used in the Webapp. These libraries provide secure design and implementation from the beginning of the SDLC lifecycle.

## A05:2021 – Security Misconfiguration

The Webapp has been designed to ensure there are no unnecessary features enable or installed within the application. Each Python package/library is configured based on it's appropriate documentation with no default settings in place. During initial initilization a user of admin with a password of admin is created. To ensure this isn't misconfigured a function to force to change password on initial login should be required. The Talisman package provides security headers and directives. All packages are using their latest versions. 

## A06:2021 – Vulnerable and Outdated Components

The webapp does not have any dependencies that are currently unused. All the Python packages/libraries are located in the requirements.txt file so they can be referenced for version number and updated as needed. These packages/libraries are pulled from the official pip servers but a controlled repo would be preferred.

## A07:2021 – Identification and Authentication Failures 

The webapp is configured to provide generic error messages based on login attempts. Server-side session managing is provided by the Flask-Session package and stored in a file in the instances folder. It has not been implented at this time but providing multi-factor authentication, password requirements, and default admin user password change upon first login would need to be done.

## A08:2021 – Software and Data Integrity Failures

Implementation of local Python package repos to ensure digital signatures would need to be implemented. At this time the Webapp uses the default pip repo for packages. All changes to the main code branch require pull requests and 1 approver. The Webapp has been implemented in Docker so that the image hash can be compared to what is pushed to Dockerhub or any registry to ensure correct image integrity.

## A09:2021 – Security Logging and Monitoring Failures

A basic logging functionality has been implemented in the Webapp. Requests to the Webapp are logged in a format that is ingestable by your standard SIEM system. Further implementaiton would include authentication logging, and database actions. Any logs generated based on user inputs such as username or password would have the correct filtering to prevent injection into the log stream.

## A10:2021 – Server-Side Request Forgery (SSRF)

Client input is provided to the SQLAlchemy ORM package to provide basic filtering. Any HTTP redirections in the Webapp are handled through a is_url_safe function to minimize redirection attacks. The Talisman package is used to provide content security policies and limit content served by the Webapp. In addition this package requires a nonce code to be included with all Javascript calls rendered by the Webapp.