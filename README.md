
# airflow-install-guide

Scripts and descriptions on how to install and run a minimum production version of airflow on a vps server.

1. Get your VPS server up and running (YOUR-IP, root and passwd)
2. Install packages
a. `apt update`
b. `apt install postgresql postgresql-contrib`
c. `apt install git mc`
d. `apt install software-properties-common`
e. `add-apt-repository ppa:deadsnakes/ppa`
f. `apt install python3.9`
g. `apt install python3-pip`
h. `apt install virtualenv`
i. `apt install screen`

3. Postgresql
	a. start the postgres server `sudo systemctl start postgresql.service`
	b. `sudo -i -u postgres` switch to user postgres
	c. test postgres with `psql` (exit with `\q` and exit brings you back to root)
	d. create user `sudo -u postgres createuser --interactive` and follow steps
	e. create airflow db (change to postgres user see b.) `createdb airflow_db`
	f. set a password in psql for the airflow db user `\password <user>`

4. Setup Airflow
	a. Clone this repo `git clone https://github.com/nicococo/airflow-install-guide.git`
	b. Install airflow `pip install apache-airflow[virtualenv]`
	c. Install psycopg2 `pip install psycopg2-binary`
	d. Adapt scripts (set names, passwords, etc)
	e. Run `./init-airflow.sh`
	f. Run `./start-airflow.sh` (better use it with `screen`)
	g. Check if it is available in a browser `http:\\YOUR-IP:8080`

5. Security
	a. Login to your airflow web UI and go to security/list users. Add a new user with a strong password and make `admin` inactive immidiately.
	b. ssh login only

