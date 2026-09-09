from airflow.sdk import dag, task

@dag(dag_id="xcoms_auto_dag", catchup=False)
def xcoms_auto_dag():
    
    @task.python
    def fetch_data(do_xcom_push: bool =True) -> dict:
        data = {"name":"Airflow", "version": 3.0}
        return data
    # Pushing data to xcom manually using the return statement

    @task.python
    def process_data(pulled_data: dict):
        # Pulling data from xcom using the key
        processed_data = f"Processing data: {pulled_data['name']} version {pulled_data['version']}"
        print(processed_data)

    @task.bash(task_id="bash_task")
    def bash_task():
        return 'echo "This is a bash task"'
    # Defining the task dependencies
    pulled_data = fetch_data()
    process_data(pulled_data) >> bash_task()

first_dag_instance = xcoms_auto_dag()