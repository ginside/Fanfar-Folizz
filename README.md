Fanfar-Folizz
=============

Django based web site

#install

## prerequisites: python 2.7.3+ , pip
svn checkout https://fanfar-folizz.googlecode.com/svn/trunk/ fanfar-folizz
cd fanfar-folizz
python -m pip install -r requirements.txt
python manage.py syncdb
## find a way to set MEDIA_URL according to base url of site
python manage.py collectstatic
##declare FANFAR_BASE_URL EnvVar?
