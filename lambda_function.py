# Import necessary packages
import json
import math
from time import gmtime, strftime
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource("dynamodb")

# Use the DynamoDB object to select our table
table = dynamodb.Table('table1')

# Store the current time in a human-readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Extract the two numbers from the Lambda service's event object
    math_result = int(event['Number 1']) * int(event['multiplied by'])  # Change here for multiplication

    # Write result and time to the DynamoDB table using the instantiated object and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(math_result),
            'LatestGreetingTime': now
        }
    )

    # Return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps(f"Your result is {str(math_result)}")
    }
