#Fifa App


## instructions

* install `postgresql`
* change `postgres` user password and create db fifa:
```sh
sudo -u postgres -i
psql
# ALTER USER postgres WITH PASSWORD 'new_password';
# CREATE DATABASE fifa;
```
* change the password in `config/db.py` to match `new_password`
* create db fifa:

* install `python3-distutils`
* install `pip`
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
* install dependencies
```
pip install -r requirements.txt
```

* run `create_db.py` to create the tables.
