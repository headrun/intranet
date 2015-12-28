# intranet

Install GIT

Install python2.7

Install MYSQL

Install python-virtualenv

Do git clone: "git clone https://github.com/headrun/intranet.git"

cd clone dir

virtualenv Headrun_Intra

source Headrun_Intra/bin/activate

pip install -r requirements.pip

Look into settings.py and Make some changes reg DB and debug...etc

python manage.py makemigrations 

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:
