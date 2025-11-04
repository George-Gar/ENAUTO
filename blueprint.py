# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging
import json

blueprint = func.Blueprint()


@blueprint.route(route="merakiWebhook", auth_level=func.AuthLevel.ANONYMOUS)
def merakiWebhook(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        shared_secret = req_body.get('sharedSecret')

    if shared_secret:
        return func.HttpResponse(body=json.dumps(req_body), headers=headers, status_code=200)
    else:
        return func.HttpResponse(
             "Please provide correct shared secret",
             status_code=401
        )