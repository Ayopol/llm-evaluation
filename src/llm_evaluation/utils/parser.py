import json


def parse_json_response(response):

    try:
        parsed = json.loads(response)
        return parsed

    except json.JSONDecodeError:
        return None
