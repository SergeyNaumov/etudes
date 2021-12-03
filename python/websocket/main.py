# https://fastapi.tiangolo.com/advanced/websockets/
from typing import Optional

# for websocket
from fastapi import FastAPI, WebSocketDisconnect
from fastapi import Cookie, Depends, Query, WebSocket, status

# for templates
from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db import db
from connect_manager import ConnectionManager
from lib.core import date_to_rus

app = FastAPI()
app.mount("/css", StaticFiles(directory="static/css"), name="css")
app.mount("/js",  StaticFiles(directory="static/js"), name="js")


templates = Jinja2Templates(directory="templates")
manager = ConnectionManager()

print('db:',db)
def get_name(client_id: int):
    db.query(
        query="select login from manager where id=%s",
        values=[client_id],
        onevalue=1
    )

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/favicon.ico')
async def favicon():
    return FileResponse('./static/favicon.ico')


@app.get("/chat/{client_id}", response_class=HTMLResponse)
async def get(client_id: int, request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "client_id":client_id})


@app.get("/init/{client_id}")
async def init(client_id: int):
    profile=db.query(
        query="select id, login name from manager where id=%s",
        values=[client_id],
        onerow=1
    )
    
    # Получаем все сообщения
    messages=db.query(
        query="""
            select 
                m.id, m.message,m.manager_id client_id, m.ts,
                cl.login client_name
            from
                messages m
                join manager cl ON cl.id=m.manager_id
            order by m.id desc limit 100
        """,
        values=[]
    )
    
    names_hash={}

    for m in messages:
        if not(m['client_id'] in names_hash):
            names_hash[m['client_id']]=m['client_name']
        
        del(m['client_name'])

        m['ts']=date_to_rus(m['ts'])

    messages.reverse()
    return {'messages':messages,'profile':profile,'names_hash':names_hash}


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
    token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            
            message_id=db.save(
                table='messages',
                data={
                    'manager_id':client_id,
                    'message':message
                }
            )
            message=db.query(
                query="select id,ts,manager_id client_id, message from messages where id=%s",
                values=[message_id],
                onerow=1
            )
            message['ts']=date_to_rus(message['ts'])

            client_name=get_name(client_id)
            
            # await manager.send_personal_message(
            #     message, websocket
            # )
            
            await manager.broadcast(message)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

