## uvicorn main:app --reload --host 192.168.2.136 --port 8000
from api import app, routes, models, conf
from uvicorn import run

from dev import dbutils

if __name__ == '__main__':
    # dbutils.fill()

    print('\n\n\n')
    dbutils.print_all_database_cap_table()
    print('\n')
    dbutils.print_all_database_caps_brand_table()
    print('\n\n\n')


    # run(app, host=conf.IP_ADDRESS, port=int(conf.PORT))

