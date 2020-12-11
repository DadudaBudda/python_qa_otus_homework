import json
import os

import jsonschema


def validate_jsonschema(data, schema_file):
    schema_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', 'schema')
    file = os.path.join(schema_dir, schema_file)
    with open(file) as json_schema:
        return jsonschema.validate(instance=data,
                                   schema=json.load(json_schema))


def test_schema_todos(session, base_url):
    response = session.get(url=f'{base_url}')
    validate_jsonschema(data=response.json(), schema_file='todos.json')


def test_schema_todo(session, base_url):
    response = session.get(url=f'{base_url}/1')
    validate_jsonschema(data=response.json(), schema_file='todo.json')
