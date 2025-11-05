# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging
import json

blueprint = func.Blueprint()

# merakiWebhook is the main function for receiving an http request object, similar to django views. it takes an inbound http request
# object as an argument and returns an http response object.
app = func.FunctionApp()
# app is the function app that replaces the function.json file 
# The Binding decorators below do away with having to maintain a functions.json file with attributes because we define
# them in the @app decorator
@app.function_name(name="QueueOutput1")
@app.route(route="message")
@app.queue_output(arg_name="msg", queue_name="func_queue", connection="AzureWebJobsStorage")
@blueprint.route(route="merakiWebhook", auth_level=func.AuthLevel.ANONYMOUS)
def merakiWebhook(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        shared_secret = req_body.get('sharedSecret')

    if shared_secret:
        msg.set(json.dumps(req_body))
        return func.HttpResponse(body=json.dumps(req_body), headers=headers, status_code=200)
    else:
        return func.HttpResponse(
             "Please provide correct shared secret",
             status_code=401
        )