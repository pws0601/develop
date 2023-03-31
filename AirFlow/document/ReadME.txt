## Apache Airflow docker 설치

docker pull apache/airflow\
docker run -it \
-p 8090:8080 \
-v /Volumes/SourceFiles/devSource/develop/AirFlow/DAG/:/opt/airflow/dags/ \
--entrypoint=/bin/bash \
--name airflow \
apache/airflow:latest \
-c '( \
    airflow db init && \
    airflow users create \
    --username admin \
    --password admin \ 
    --firstname Anonymous \
    --lastname Admin \
    --role Admin \
    --email pws0601@hyosung.com \
); \
airflow webserver & \
airflow scheduler \
'

## airflow webserver 가동
airflow webserver --port 8090

## airflow scheduler 가동
airflow scheduler

https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=10&offset=10