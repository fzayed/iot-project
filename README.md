# IoT Alarm Clock Project - Group 12

## Table of Contents

Below is a brief description for each folder/file that was required to implement the website:

**alarmclock**: A folder that contains all the source code required to implement the website. [Link to the folder] https://github.com/fzayed/iot-project/tree/main/alarmclock

Inside the **alarmclock** folder is another folder called **base** where most of the website implementation relies. Such as:

- models.py: A file where our data models are stored and the entities are specified. [Link to the file] https://github.com/fzayed/iot-project/blob/main/alarmclock/base/models.py
- urls.py: A file that contains all the URL patterns for the project and relates different pages of the application. [Link to the file] https://github.com/fzayed/iot-project/blob/main/alarmclock/base/urls.py
- views.py: A file that handles requests and return responses. [Link to the file] https://github.com/fzayed/iot-project/blob/main/alarmclock/base/views.py
- homepage.html: A home page that the user will visit first. [Link to the file] https://github.com/fzayed/iot-project/blob/main/alarmclock/base/templates/base/homepage.html
- confirmation.html: A confirmation page that displays a confirmation message to the user. [Link to the file] https://github.com/fzayed/iot-project/blob/main/alarmclock/base/templates/base/confirmation.html


## Installation

1. Download the **alarmclock** folder.
2. Open terminal at the folder.
3. Install django by typing ***pip install django*** in the terminal.
4. Run the server by typing ***python manage.py runserver*** in the terminal.
5. Go to http://127.0.0.1:8000/ to visit the website.
