import azure.functions as func
import logging
import json
import random

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="playermarker", auth_level=func.AuthLevel.ANONYMOUS)
def playermarker(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        marker = req_body.get('marker')
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    if marker not in ['O', 'X']:
        return func.HttpResponse("Marker must be 'O' or 'X'", status_code=400)

    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'

    return func.HttpResponse(
        body=f'{{"player1": "{player1}", "player2": "{player2}"}}',
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="aiplayerchoice", auth_level=func.AuthLevel.ANONYMOUS)
def aiplayerchoice(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        board = req_body.get('board')
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)
    
    choice = random.randrange(1, 10)

    while board[choice] != '':
        choice = random.randrange(1, 10)
    
    
    return func.HttpResponse(
        json.dumps({'choice': choice}),
        mimetype="application/json",
        status_code=200
    )