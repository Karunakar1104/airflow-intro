from airflow.sdk import dag, task
import datetime

@dag(
        dag_id="schedule_dag",
        start_date=datetime.datetime(2026, 9, 1),
        schedule="@daily",
        catchup=False
        )

def schedule_dag():

    @task(task_id = "task_1")
    def task_1():
        print("Hello from task_1")

    @task(task_id = "task_2")
    def task_2():
        print("message from task_2")

# Define the task dependencies
    task_1() >> task_2()
    
first_dag_instance = schedule_dag()