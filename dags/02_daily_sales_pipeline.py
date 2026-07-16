from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Define the DAG with a daily schedule
with DAG(
    dag_id="pod_daily_sales_automation",
    start_date=datetime(2026, 7, 15),
    schedule="@daily",
    catchup=False,
    tags=["pod_business", "production"],
) as dag:

    # Task 1: A placeholder for our future data extraction script
    extract_orders = EmptyOperator(
        task_id="extract_shopify_orders"
    )

    transform_data = EmptyOperator(
        task_id= "dbt_run_sales_models"
    )