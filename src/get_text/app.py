import json


def get_text_lambda(event, context):
    try:
        term = event.get("queryStringParameters", {}).get("term", "")
        print ("term: " + term)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': '{"message": "GET /text?term="' + term + '}'  # Your actual response data here
        }
    except Exception as e:
        print (repr(e))
        raise Exception(e)
