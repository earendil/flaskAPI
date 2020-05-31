from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/total', methods=["POST"])
def total():
    """ End point that adds a received list of integers, passed as a json dictionary with key "numbers" and
        value as an array of integers.
        :returns a json containing the sum of integers.

        Example  input: { "numbers": [1, 2, 3] }
        Example output: { "total": 6 }
        Example request:
        curl http://localhost:5000/total -d '{"numbers": [1, 2, 3] }'  -H 'Content-Type: application/json'
    """

    post_data = request.get_json()
    list_of_numbers = post_data["numbers"]

    return jsonify(total=sum(list_of_numbers))


if __name__ == '__main__':
    app.run(debug=True)
