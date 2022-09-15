from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator


PATH_DAGS = '/home/airflow/gcs/dags/'


default_args = {
    'owner': 'nico',
    'retries': 1,
}

with DAG(
    dag_id='test_venv_v1.0.0',
    default_args=default_args,
    schedule_interval='0 7 * * THU',
    start_date=datetime(2022, 1, 1, 8, 0),
    catchup=False,
    tags=['test', 'venv'],
) as dag:

    def dag_func(*context):
        import os
        import sys
        import time
        sys.path.append(f'{PATH_DAGS}airflow-install-guide/dags')
        sys.path.append(f'{PATH_DAGS}airflow-install-guide')

        print('ENV:')
        dirs = os.listdir('/tmp')
        print(dirs)
        venvs = []
        for path in dirs:
            if os.path.isdir(f'/tmp/{path}') and path.startswith('venv'):
                venvs.append(f'/tmp/{path}')
                print(f'FOUND IT: {venvs}')
                print(os.listdir(f'{venvs[-1]}/bin'))

        print(os.environ.get('DAGS_FOLDER', 'no folder specified'))
        sys_argv_bak = sys.argv

        # Do something here
        print('This is the content of the context object: ', context)
        # Stop doing something here

        sys.argv = sys_argv_bak


    virtualenv_task = PythonVirtualenvOperator(
        task_id="test_venv",
        python_callable=dag_func,
        requirements=[],
        provide_context=True,
        system_site_packages=False,
    )