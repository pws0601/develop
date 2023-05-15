import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator

dag=DAG(
    dag_id="stocksense",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@hourly",
)

get_data=BashOperator(
    task_id="get_data",
    bash_command=(
        "curl -o /tmp/ex/wikipageviews.gz "
        "https://dumps.wikimedia.org/other/pageviews/"
        "{{ execution_date.year }}/" # 이중중괄호는 런타임 시에 삽입될 변수를 나타냄
        "{{ execution_date.year }}-"
        "{{ '{:02}'.format(execution_date.month) }}/"
        "pageviews-{{ execution_date.year }}"
        "{{ '{:02}'.format(execution_date.month) }}"
        "{{ '{:02}'.format(execution_date.day) }}-"
        "{{ '{:02}'.format(execution_date.hour) }}0000.gz"
    ),
    dag=dag,
)