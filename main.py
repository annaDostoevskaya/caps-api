from api import app, routes
from uvicorn import run

if __name__ == '__main__':
    run(app, host="192.168.2.136", port=8000)
