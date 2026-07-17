from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# A standard Python function that will act as our extraction script
def download_data():
    print("SUCCESS: Downloading orders from Shopify API into AWS S3...")

with DAG(
    dag_id="pod_daily_sales_automation",
    start_date=datetime(2026, 7, 15),
    schedule="@daily",
    catchup=False,
    tags=["pod_business", "production"],
    
) as dag:

    # Task 1: Replaced with a PythonOperator
    extract_orders = PythonOperator(
        task_id="extract_shopify_orders",
        python_callable=download_data
    )

    # Task 2: Replaced with a BashOperator
    transform_data = BashOperator(
        task_id="dbt_run_sales_models",
        bash_command="echo 'SUCCESS: Running dbt models in the warehouse...'"
    )

    # Task 3: Replaced with a BashOperator
    notify_team = BashOperator(
        task_id="send_success_email",
        bash_command="echo 'Pipeline complete! Emailing the team.'"
    )

    extract_orders >> transform_data >> notify_team