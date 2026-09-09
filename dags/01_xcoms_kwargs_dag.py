from airflow.sdk import dag, task

@dag(dag_id="xcoms_kwargs_manual_dag", catchup=False)
def xcoms_kwargs_manual_dag():
    
    @task.python
    def fetch_data(ti):
        data = {"name":"Airflow", "version": 3.0}
        ti.xcom_push(key="fetch_data", value=data)
        return data
    # Pushing data to xcom manually using the return statement

    @task.python
    def process_data(ti):
        # Pulling data from xcom using the key

        pulled_data = ti.xcom_pull(key="fetch_data", task_ids="fetch_data")
        # Simulating processing on the pulled data
        processed_data = f"Processing data: {pulled_data['name']} version {pulled_data['version']}"
        print(processed_data)

    @task.bash(task_id="bash_task")
    def bash_task():
        return 'echo "This is a bash task"'

    fetch_data() >> process_data() >> bash_task()

first_dag_instance = xcoms_kwargs_manual_dag()