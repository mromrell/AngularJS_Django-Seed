===============================================
Dojo Dev Camp - Django/Angular Project Template
===============================================

A project template for a single server application using AngularJS, Django 1.6 and Heroku.

Initial setup
-------------

Create your virtual environment.
- You can do this in Pycharm by going to Preferences > Project Interpreter > Python Interpreters > then click the little Python Logo (with a V) to create a new Virtual Environment
- Apply Changes
- Go to Preferences > Project Interpreter and make sure its set to your newly created Virtual environment

Setup Pycharm
- Go to Preferences > Version Control and click on 'Add Root' on both of the red highlighted boxes.
- Then highlight the '<Project>' line and click the little minus sign to remove it (So you should only see 'ro-seed-frontend' and 'ro-seed-backend' in your directory list)

Setup Django Support in Pycharm.
- You can do this in Pycharm by going to Preferences > Django Support > click Enable Django Support
- For Django project root: select your 'ro-seed-backend' folder
- For Settings: settings/base.py
- For Manage script: manage.py
- Apply Settings and close Pycharm Preferences

In Pycharm click the little dropdown arrow in the menu and choose 'Edit Configurations'
- click the + sign > Choose 'Django Server'
-- Name it whatever you'd like
-- ensure the port is 8001
-- ensure that the Python interpreter is set to your virtual environment
-- Apply changes
- click the + sign > Choose 'Node.js'
-- Working directory should be: 'MyProject/ro-seed-frontend'
-- JavaScript File should be: 'server/web-server.js'
-- Apply changes and click OK

Go to your CLI/terminal and activate your virtual environment by navigating to the file where you created (remember the step above). Go to the <projectName>/bin folder then run '. activate' and you should see your command line prompt prefaced with (Project Name)...

In the CLI go to your 'ro-seed-backend' folder (from within your virtual environment), run "pip install -r requirements.txt"
In your front end folder, run "npm install."

Setting up your database
-------------------------

In the CLI run the following command:
```
createdb MyDatabaseName
```
- Go back to PyCharm > open dev.py and set the database name to 'MyDatabaseName' (or whatever you called it in the step above) and set the database user (on a Mac this is usually the user of the computer you are logged in with)
- Go to ro-seed-backend/apps/public and delete the 'migrations' folder
- Go back to the CLI run the following commands:
```
python manage.py schemamigration public --init
python manage.py syncdb
     // Select "no." Do not create a superuser at this time.
python manage.py migrate
python manage.py createsuperuser
```

```
// if working with others later in the project (perhaps via Github), they may make updates to the database (models.py file) in which case you'll need to update your database using the following command:
python manage.py schemamigration public --auto
python manage.py migrate
```

Deploying to Heroku
-------------------
- Create a new heroku account at heroku.com
- Open up your terminal
- Run the following commands

```
cd /path/that/will/hold/repository
git clone git@github.com:test.git # using the same name as above for an example
cd test
heroku create # this will create a new heroku app and attach it as a remote repository
```

- Copy the heroku app domain to the ALLOWED_HOSTS array in project/settings/test.py

```
git push heroku master
heroku open # run this once the previous command finishes, it may take a minute
```
