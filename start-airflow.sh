#!/bin/bash

# This scripts starts a local airflow instance with an postgres db and LocalExecutor (ie. enables 
# parallel execution of subtasks).

# The general format for setting airflow options via environment variables is:
# FORMAT: AIRFLOW__{section}__{key}

# Setting to LocalExecutor allows concurrent execution of jobs on a single machine.
# However, it cannot be used with SQLlite DB (which does not allow concurrent connections).
export AIRFLOW__CORE__EXECUTOR=LocalExecutor

# Assume a local instance of postgres is up and running (init-airflow.sh script has been executed successfully)
export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://<user>:<passwd>@localhost:5432/airflow_db"

# Check installation of airflow first.
airflow version 

# Start the scheduler as a deamon.
airflow scheduler&

# Start the web server on port 8080.
airflow webserver -p 8080
