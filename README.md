
# airflow-install-guide

Scripts and descriptions on how to install and run a minimum production version of airflow on a vps server.

- Get your VPS server up and running (YOUR-IP, root and passwd)
- Install system packages
-- `apt update`
-- `apt install postgresql postgresql-contrib`
-- `apt install git mc`
-- `apt install software-properties-common`
-- `add-apt-repository ppa:deadsnakes/ppa`
-- `apt install python3.9`
-- `apt install python3-pip`
-- `apt install virtualenv`
-- `apt install screen`

- Install postgresql database
-- start the postgres server `sudo systemctl start postgresql.service`
-- `sudo -i -u postgres` switch to user postgres
-- test postgres with `psql` (exit with `\q` and exit brings you back to root)
-- create user `sudo -u postgres createuser --interactive` and follow steps
-- create airflow db (change to postgres user see b.) `createdb airflow_db`
-- set a password in psql for the airflow db user `\password <user>`

- Setup Airflow
-- Clone this repo `git clone https://github.com/nicococo/airflow-install-guide.git`
-- Install airflow `pip install apache-airflow[virtualenv]`
-- Install psycopg2 `pip install psycopg2-binary`
-- Adapt scripts (set names, passwords, etc)
-- Run `./init-airflow.sh`
-- Run `./start-airflow.sh` (better use it with `screen`)
-- Check if it is available in a browser `http:\\YOUR-IP:8080`

- Security
-- Add basic airflow security 
--- Login to your airflow web UI and go to security/list users
--- Add a new user with a strong password and make `admin` inactive immidiately

-- Add basic server security
--- Create a new linux user
--- Activate SSH login only for this user (use `ssh-copy-id <user>@<YOUR-IP>`)
--- Deactivate Password authenification via `/etc/ssh/sshd_config`, set `PasswordAuthentication no`
