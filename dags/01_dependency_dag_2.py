from airflow.sdk import dag, task
from airflow.utils.triggerrule import TriggerRule

@dag(dag_id="dependency_dag_2")
def dependency_dag_2():
    
    @task(task_id = "task_1")
    def task_1():
        print("Hello from task_1")

    @task(task_id = "task_2")
    def task_2():
        print("message from task_2")

    @task(task_id = "task_3")
    def task_3():
        print("message from task_3")
        raise Exception("Intentional error in task_3 for testing purposes.")

    @task(task_id = "task_4", trigger_rule=TriggerRule.ALL_DONE)
    def task_4():
        print("message from task_4")

# Define the task dependencies

    task_1() >> [task_2(), task_3()] >> task_4()

first_dag_instance = dependency_dag_2()