import json

def lambda_handler(event, context):
    """
    Simple Lambda function that returns a greeting
    """
    name = event.get('name', 'World')
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello {name}! Welcome to Lambda CICD Pipeline!',
            'source': 'Lambda CICD Pipeline'
        })
    }