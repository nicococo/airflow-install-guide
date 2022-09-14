#!/bin/bash

# This script should only be called one time *after* the postgres database is set up and running 
# and *before* airflow scheduler and webserver is called for the first time.


# The general format for setting airflow options via environment variables is:
# export AIRFLOW__{section}__{key}

# Assume a local instance of postgres is up and running.
# - airflow is installed correctly
# - postgres should be up and running on port 5432
# - root <user> and <passwd> needs to be set in postgres
# - postgres should contain a table `airflow_db` 
export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://<user>:<passwd>@localhost:5432/airflow_db"


# Test airflow installation first.
airflow version

# Init the airflow database (create tables, etc).
airflow db init

# Create an airflow user login (name and password).
# This can be changed then later in the running airflow system 
# using the web UI.
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.org

# Create a symlink between our /dag folder and the example_dag folder in airflow
ln -sf dags/ <path>/<to>/example_dags/
