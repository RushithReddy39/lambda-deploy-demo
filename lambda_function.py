import os

def lambda_handler(event, context):
    greeting = os.environ.get('GREETING_MESSAGE', 'Hello, World!')
    return {
        'statusCode': 200,
        'body': greeting
    }

#This is to just test the git
