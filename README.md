# INSTALL & SETUP INSTRUCTIONS

to clone project open terminal & write: git clone https://github.com/sumitkumar1503/ecommerce,
then: cd ecommerce,
if you have got other branch than master, write: git checkout your_branch


#### 1. Create a virtual environment to isolate our package dependencies locally
pip install virtualenv  
python -m venv env 
 
source env/bin/activate for Linux/MacOS  
env\Scripts\activate.bat for Windows  

#### 2. Install requirements
pip install -r requirements.txt

#### 3. Migrate
python manage.py makemigrations
python manage.py migrate

#### 4. Create superuser
python manage.py createsuperuser  

#### 5. Run server
python manage.py runserver

#### 6. Enjoy
http://localhost:8000/  
http://localhost:8000/admin/  