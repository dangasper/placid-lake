# placid-lake

## Purpose
The purpose of this webapp is to create a basic POAM tracker that will allow users to add open vulnerabilities for tracking and provide a dashboard for quick reporting functions.

## Design
This webapp is created using the Python Flask framework and a Model-View-Controller-ish layout. Multiple different python packages have been included to provide additional functionality to the application. Within the app folder will the configs which will load these packages for the webapp to utlize. The controllers folder will contain all functions relating to database executions. Within the models folder is the database schemas. The routes folder is to provide the paths which will call the controller functions, and render the webpages from the static and templates folder.

## File descriptions
You can find a description of each file and associated functions if applicable at the following:

[configs](docs/CONFIGS.md)

[controllers](docs/CONTROLLERS.md)

[models](docs/MODELS.md)

[routes](docs/ROUTES.md)

[templates](docs/TEMPLATES.md)


## Security considerations
You can find a list of mitiagations to the OWASP TOP 10 [here](docs/OWASP.md)