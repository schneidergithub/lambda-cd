import json

print('loading function')

def lambda_handler(event, context):
    #transactionName = event['queryStringParameters']['name']

    transactionName = "testcommit3"
    print('transactionName=' + transactionName)

    transactionResponse = {}
    transactionResponse['transactionName'] = transactionName
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject