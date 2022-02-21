## heroku local -f Procfile.local
## uvicorn main:app --reload --host 192.168.2.136 --port 8000
# run(app, host=conf.IP_ADDRESS, port=int(conf.PORT))
from api import app, routes, models, conf
from uvicorn import run


from dev import dbutils


from pydantic import BaseModel
class Test(BaseModel):
    foo: str
    bar: str


class Test2(BaseModel):
    test: Test
    baz: str


@app.get(
    "/simple_exclude_dict",
    response_model=Test2,
    response_model_exclude={"test": {"bar"}},
)
def simple_exclude_dict():
    return {
        "test": {
            "foo": "simple_exclude_dict test foo",
            "bar": "simple_exclude_dict test bar",
        },
        "baz": "simple_exclude_dict test2 baz",
    }

def test_nested_exclude_simple_dict():
    response = client.get("/simple_exclude_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "baz": "simple_exclude_dict test2 baz",
        "test": {"foo": "simple_exclude_dict test foo"},
    }

if __name__ == '__main__':
    # dbutils.print_all_database_user_table()
    run(app, host=conf.IP_ADDRESS, port=int(conf.PORT))

    # dbutils.fill()

