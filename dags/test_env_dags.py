from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="01_environment_check_verified",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["bootcamp", "setup"],
) as dag:

    verify_env = EmptyOperator(
        task_id="verify_environment_setup"
    )

    confirm_env = EmptyOperator(
        task_id = "confirm_uv_installation"
    )