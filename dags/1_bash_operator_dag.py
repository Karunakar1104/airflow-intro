from airflow.sdk import dag,task
airflow.providers.standard.operators.python.PythonOperator
airflow.providers.standard.operators.bash.BashOperator

@dag(dag_id="bash_operator_dag" ,catchup=False)

def bash_operator_dag():

# Modern way of defining a BashOperator task using the @task decorator

      @task.bash(task_id="bash_task")
      def bash_task():
            return "echo 'Hello from bash_task'"

      @task.bash(task_id="bash_task_2")
      def bash_task_2():
            return "echo 'Hello from bash_task_2'"

# Modern way of defining a PythonOperator task using the @task decorator

      @task.python(task_id="python_task")
      def python_task():
            return "Hello from python_task"
      
#The traditional way of defining a BashOperator task

      tradition_way_of_bash = BashOperator(
            task_id="tradition_way_of_bash",
            bash_command="echo 'Hello from modern_bash_task'",
      )

#The traditional way of defining a PythonOperator task

      tradition_way_of_python = PythonOperator(
            task_id="tradition_way_of_python",
            python_callable=lambda: print("Hello from tradition_way_of_python"),
      )

      bash_task() >> bash_task_2() >> python_task() >> tradition_way_of_bash
      tradition_way_of_bash >> tradition_way_of_python

first_dag_instance = bash_operator_dag()