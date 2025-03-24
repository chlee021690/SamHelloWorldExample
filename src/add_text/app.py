import json


def add_text_lambda(event, context):
    try:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': '{"message": "POST /texts"}'  # Your actual response data here
        }
    except Exception as e:
        print (repr(e))
        raise Exception(e)