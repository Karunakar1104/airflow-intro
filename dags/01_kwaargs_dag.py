from airflow.sdk import dag, task

@dag(dag_id="kwargs_dag", catchup=False)
def kwargs_dag():
    
    @task.python
    def fetch_data(**kwargs):
        ti = kwargs['ti']
        print("Printing the kwargs in fetch_data task:", kwargs)
        data = {"name": "Airflow", "version": 3.0}
        ti.xcom_push(key="fetched_data", value=data)

    @task.python
    def process_data(**kwargs):
        ti = kwargs['ti']
        print("Printing the kwargs in process_data task:", kwargs)
        #Printing the task_id to show how to access them from kwargs
        print("Pulling data from XCom in process_dag:",kwargs['dag'].dag_id)
        #Printing the task_id to show how to access them from kwargs
        print("Pulling data from XCom in process_task:",kwargs['task'].task_id)

        processed_data = ti.xcom_pull(key="fetched_data", task_ids="fetch_data")
        pulled_data = f"processed {processed_data['name']} version {processed_data['version']}"
        print(pulled_data)

    @task.bash
    def bash_task(**kwargs):
        return 'echo "This is a bash task returning data is {{ ti.xcom_pull(key=\'fetched_data\', task_ids=\'fetch_data\') }}"'

    fetch_data() >> process_data() >> bash_task()

first_dag_instance = kwargs_dag()