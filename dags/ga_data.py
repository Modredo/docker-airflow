from datetime import datetime, timedelta

from airflow import  DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.http_operator import SimpleHttpOperator


default_args = {
    'owner': 'Airflow',  
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 4),
    #'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("ga_data_cloudRun_2", default_args=default_args, schedule_interval=timedelta(days=1))

#send a POST to url
t1 = SimpleHttpOperator(
    task_id = "call_cloud_run_2",
    method='GET',
    endpoint='/channel',
    #headers={'channel':'UK'},
    http_conn_id='cloud_run_gcp_flask',
    xcom_push=True,
    dag=dag,
)
#on sucess write sucess

