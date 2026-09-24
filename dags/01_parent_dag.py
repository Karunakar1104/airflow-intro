from airflow.sdk import dag, task
from first_child_dag import first_child_dag
from second_child_dag import second_child_dag
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
#from airflow.providers.standard.operators.trigger_dagrun.TriggerDagRunOperator

@dag(dag_id="parent_dag")
def parent_dag():
    trigger_first_child_dag = TriggerDagRunOperator(
        task_id="trigger_first_child_dag",
        trigger_dag_id="first_child_dag",
        wait_for_completion=True,
        poke_interval=10,
    )

    trigger_second_child_dag = TriggerDagRunOperator(
        task_id="trigger_second_child_dag",
        trigger_dag_id="second_child_dag",
        wait_for_completion=True,
        poke_interval=10,
    )

    trigger_first_child_dag >> trigger_second_child_dag

parent_dag_instance = parent_dag()