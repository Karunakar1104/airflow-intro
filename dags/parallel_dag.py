from airflow.sdk import dag, task
import datetime
import pendulum

@dag()
#dag_id="parallel_dag",
#schedule=None,
#start_date="2026-09-01",
#end_date="2026-09-30",
#catchup=False,
#tags=["Testing dag for parallel tasks"]
def parallel_dag():

    @task.bash
    def task_bash():
        return 'echo "This is a bash task"'

    @task.python
    def api_data():
        data = {"place": "Gudivada", "Count": 3000}
        return data

    @task.python
    def db_data():
        data = {"DB": "SQLServer", "Sql Command": "select * from table"}
        return data

    @task.python
    def gcs_data():
        data = {"Bucket": "GCS", "File": "gs://bucket/file.csv"}
        return data

    @task.python
    def process_data(api_data, db_data, gcs_data):
        print("Processing data from API:", api_data)
        print("Processing data from DB:", db_data)
        print("Processing data from GCS:", gcs_data)


    task_bash = task_bash()
    api_data = api_data()
    db_data = db_data()
    gcs_data = gcs_data()
    process_data = process_data(api_data, db_data, gcs_data)

    # Define the task dependencies
    task_bash >> [api_data, db_data, gcs_data] >> process_data

parallel_dag_instance = parallel_dag()