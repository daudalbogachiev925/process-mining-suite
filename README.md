Описание: платформа process mining на базе pm4py. Загрузка XES/CSV, построение DFG, Petri nets, bottleneck-анализ, conformance check, веб-UI.

Стек: Python, pm4py, FastAPI, React (или Streamlit), PostgreSQL, MinIO (S3), Docker.

# process-mining-suite

Open-source платформа process mining.

## Функции
- Загрузка event log (CSV/XES)
- Обнаружение DFG, Petri nets, BPMN
- Анализ производительности и bottleneck
- Conformance checking
- Варианты процессов
- REST API

## Использование

docker-compose up

curl -F "file=@log.csv" http://localhost:8000/api/mining/dfg

## Лицензия
Apache 2.0
