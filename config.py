import os
basedir = os.path.abspath(os.path.dirname(__file__))

# dotemv file looks like :
# FLASK_APP=run.py
# FLASK_ENV=development
# DATABASE_URL= ### INSERT DATABASE URL HERE ###

class Config():
    FLASK_APP=os.environ.get('FLASK_APP')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') #sqlite///c:\Documents\coding-temple-feb-2021\week5\feb_intro_to_flask
    SQLALCHEMY_TRACK_MODIFICATIONS = False
