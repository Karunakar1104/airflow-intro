from airflow.sdk import dag, task
import os

@dag(dag_id="first_child_dag")
def first_child_dag():
    @task(task_id = "task_1")
    def task_1():
        print("Hello from task_1")

    @task(task_id = "task_2")
    def task_2():
        print("message from task_2")

    @task(task_id = "task_3")
    def task_3():
        print("message from task_3")
        #raise Exception("Intentional error in task_3 for testing purposes.")

    @task(task_id = "task_4")
    def task_4():
        # Creating a deirectory if it doesn't exist
        os.makedirs("/tmp/data", exist_ok=True)

        # Writing a message to a file
        with open("/tmp/data/output_first.txt", "w") as f:
            f.write("Hello from task_4 in the first_child_dag!")

# Define the task dependencies

    task_1() >> [task_2(), task_3()] >> task_4()

first_child_dag_instance = first_child_dag()