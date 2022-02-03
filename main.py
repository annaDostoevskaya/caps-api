# uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models
from uvicorn import run

from dev import dbutils

if __name__ == '__main__':
    dbutils.print_all_database_cap_table()
    # run(app, host='192.168.2.136', port=8000)
