import json


def test_total(test_client):

    response = test_client.post(
        "/total",
        data=json.dumps(dict(numbers=[1, 2, 3])),
        content_type="application/json")

    assert json.loads(response.data) == {"total": 6}
