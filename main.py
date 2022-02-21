## heroku local -f Procfile.local
## uvicorn main:app --reload --host 192.168.2.136 --port 8000
# run(app, host=conf.IP_ADDRESS, port=int(conf.PORT))
from api import app, routes, models, conf
from uvicorn import run

from dev import dbutils

if __name__ == '__main__':
    dbutils.print_all_database_user_table()
    # dbutils.fill()
    # run(app, host=conf.IP_ADDRESS, port=int(conf.PORT))

