import json

def lambda_handler(event, context):
    # TODO implement
    print("=============")
    print(event)
    auth = "Deny"
    if event["authorizationToken"] == "Zaid123":
        auth = "Allow"
    print("=============")
    authRespon = {"principalId":"abcdef","policyDocument":{"Version":"2012-10-17","Statement":[{"Action":"execute-api:Invoke","Effect":auth,"Resource":"arn:aws:execute-api:us-east-1:583730671250:2uj5589ww6/*/*"}]}}

        
    print("*********************")
    return authRespon
