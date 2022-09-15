from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator


PATH_DAGS = '/home/airflow/gcs/dags/'


default_args = {
    'owner': 'nico',
    'retries': 1,
}

with DAG(
    dag_id='test_playwright_venv_v1.0.0',
    default_args=default_args,
    schedule_interval='0 7 * * THU',
    start_date=datetime(2022, 1, 1, 8, 0),
    catchup=False,
    tags=['test', 'playwright', 'venv'],
) as dag:

    def dag_func(*context):
        import os
        import sys
        import time
        sys.path.append(f'{PATH_DAGS}airflow-install-guide/dags')
        sys.path.append(f'{PATH_DAGS}airflow-install-guide')

        print('CONTEXT:')
        print(context)
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
        failed = True
        max_tries = 5
        venvs_ind = 0
        if len(venvs) > 0:
            while failed and max_tries >=0:
                try:
                    #os.system(f'source {venvs[venvs_ind]}/bin/activate; playwright install')
                    os.system(f'sudo {venvs[venvs_ind]}/bin/playwright install-deps')
                    os.system(f'{venvs[venvs_ind]}/bin/playwright install')
                    res = os.system(f'{venvs[venvs_ind]}/bin/playwright')
                    import playwright
                    if res == 0 or res == 256:
                        failed = False
                except Exception:
                    print('Playwright not installed yet...')
                time.sleep(5)
                max_tries -= 1
                venvs_ind += 1
                if venvs_ind == len(venvs):
                    venvs_ind = 0
        else:
            print('ERROR could not find venv.')

        # Do something here
        print('This is the content of the context object: ', context)
        # Stop doing something here

        sys.argv = sys_argv_bak


    virtualenv_task = PythonVirtualenvOperator(
        task_id="test_playwright_venv",
        python_callable=dag_func,
        requirements=["playwright"],
        provide_context=True,
        system_site_packages=False,
    )