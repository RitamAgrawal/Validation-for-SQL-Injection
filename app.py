from flask import Flask, request, jsonify

from api.utils.error import error_message
from api.utils.input import key_exists, is_valid_input, compare_input


app = Flask(__name__)


ascii_characters = [{"character": chr(i), "ascii": i} for i in range(256)]


@app.route('/', methods=["GET", "POST"])
def get_all_characters():
    """
    """
    return jsonify({"characters": ascii_characters})


@app.route('/api/v1/sanitized/input/', methods=["POST"])
def validate_input():
    """This method returns the result as sanitized or unsantized for valid input.

    Returns
    -------
    boolean

        {"result": "sanitized"}
        {"result": "unsanitized"}
    """
    try:
        content = request.json
    except Exception as err:
        # throws an error if input in not valid json
        print(err)
        return error_message("BAD_REQUEST")

    is_valid_key = key_exists("payload", content)
    if is_valid_key is False:
        return error_message("MISSING_PAYLOAD")

    if is_valid_input(content["payload"]):
        is_sanitized = compare_input(content["payload"])

        if (is_sanitized):
            # print(is_valid_key)
            return jsonify({
                "result": "sanitized"
            })
        else:
            return jsonify({
                "result": "unsanitized"
            })
    else:
        return error_message()


if __name__ == '__main__':
    app.run()
