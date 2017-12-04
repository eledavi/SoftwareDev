##Study Buddy## Version 1.0

Developed by:  Caitlin Ard, Elena Davidson, Angela Kearns, and Ryan Adams

Description:
----------------
College is hard. College is harder when you don't have anyone to study with. This is where Study Buddy comes in! Study Buddy is an app created to help college students find and create study groups for their classes. Students are able to create accounts with their school emails and can join study groups for various classes on campus. Users can also create study groups for the classes they're taking.

What you will need:
--------------------------
Developers will require the following:

*Please note* - The current development used the Nexus 4 API 24 and was not tested against other devices with other android operating systems. 

Android Studio: (For main android app development)
Gradle Version 4.1
Android Plugin Version 3.0.1
The dependencies within the application are handled within android studio, it is important to allow android studio to install these files.
Additionally all files within StudyBuddy > myApplication folder are required for the app to run properly.  After downloading Android studio, please open the StudyBuddy.

Study-Buddy-Server: (Required for localhost) 

The current implementation of Study Buddy is not mounted on a permanent server. Please see “How to Run” section for information on how to run app on localhost.

Python Version 2.7: (below are the libraries required)
SQLAlchemy version 1.0.13
Jinja2 version 2.8
Requests version 2.13.0
Cherrypy 11.2.0

How to Run :
----------------

Small user configuration is required at this level of implementation: please follow information listed below.

1. Startup the Study-Buddy-Server:
	a. Navigate within terminal to the server located in study-buddy-server > server >
	b. Make sure you have required dependencies (requirements.txt)
	c. Then type command ‘python server.py’
2. Download Android Studio
	a. Open StudyBuddy/MyApplication within Android Studio
	b. Update and import files as Android Studio instructs (there is always a lot of this)
3. Additionally users will need to modify their ip address within the app itself:
	a. All references of String url = …. Within Android Studio will need to be replaced with the user’s current IP address at the root instead of the current project IP
4. Press the play button and set up your emulator to run Nexus 4 API 24
5. Study Away!

