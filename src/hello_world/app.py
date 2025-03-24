import json


def print_hello_world_lambda(event, context):
    try:
        print(json.dumps({"text": "Hello World"}))
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': '{"text": "Hello World"}'  # Your actual response data here
        }
    except Exception as e:
        print (repr(e))
        raise Exception(e)

    