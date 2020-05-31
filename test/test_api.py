import json


def test_total_simple(test_client):

    response = test_client.post(
        "/total",
        data=json.dumps(dict(numbers=[1, 2, 3])),
        content_type="application/json"
    )

    assert json.loads(response.data) == {"total": 6}


def test_total_large(test_client):

    response = test_client.post(
        "/total",
        data=json.dumps(dict(numbers=list(range(10000001)))),
        content_type="application/json"
    )

    assert json.loads(response.data) == {"total": 50000005000000}
