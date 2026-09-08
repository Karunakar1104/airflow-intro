from airflow.sdk import dag,task
from airflow.operators.python import PythonOperator
from airflow import DAG

def first_task_func():
    return "Hello from python_task_1"

def second_task_func():
    return "Hello from python_task_2"

#with DAG(dag_id="python_operator_dag", #catchup=False) as dag:

@dag(dag_id="python_operator_dag", catchup=False)
def python_operator_dag():

    first_task = PythonOperator(
        task_id="first_task",
        python_callable=first_task_func
    )

    second_task = PythonOperator(
        task_id="second_task",
        python_callable=second_task_func
    )

    # Define the task dependencies
    first_task >> second_task

python_dag_instance = python_operator_dag()