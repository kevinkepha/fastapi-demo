from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>FastAPI Demo</title></head>
        <body>
            <h1>Hello from FastAPI + Docker + Nginx!</h1>
        </body>
    </html>
    """