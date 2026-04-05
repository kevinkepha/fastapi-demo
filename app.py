from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
        return """
        <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>FastAPI Tube</title>
                <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
                <style>
                    body { background-color: #181818; color: #fff; }
                    .navbar { background-color: #202020; }
                    .logo { font-size: 2rem; font-weight: bold; color: #FF0000; }
                    .search-bar { max-width: 500px; }
                    .video-card { background: #232323; border: none; }
                    .autodeploy-banner { background: #ffeb3b; color: #222; font-weight: bold; text-align: center; padding: 1.5rem; border-radius: 1rem; margin-bottom: 2rem; font-size: 1.5rem; }
                </style>
            </head>
            <body>
                <nav class='navbar navbar-expand-lg navbar-dark'>
                    <div class='container-fluid'>
                        <span class='logo me-3'>FastAPI Tube</span>
                        <form class='d-flex search-bar mx-auto'>
                            <input class='form-control me-2' type='search' placeholder='Search' aria-label='Search'>
                            <button class='btn btn-outline-light' type='submit'>Search</button>
                        </form>
                        <button class='btn btn-danger'>Sign In</button>
                    </div>
                </nav>
                <div class='container mt-5'>
                    <div class='autodeploy-banner'>🚀 Auto-deployment is working! (Visible change at: {date})</div>
                    <div class='row g-4'>
                        <div class='col-md-4'>
                            <div class='card video-card'>
                                <img src='https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg' class='card-img-top' alt='Video'>
                                <div class='card-body'>
                                    <h5 class='card-title'>Welcome to FastAPI Tube!</h5>
                                    <p class='card-text'>Experience blazing fast web apps with Python and FastAPI. This is a YouTube-inspired demo styled with Bootstrap 5.</p>
                                </div>
                            </div>
                        </div>
                        <div class='col-md-4'>
                            <div class='card video-card'>
                                <img src='https://img.youtube.com/vi/3JZ_D3ELwOQ/hqdefault.jpg' class='card-img-top' alt='Video'>
                                <div class='card-body'>
                                    <h5 class='card-title'>Why FastAPI?</h5>
                                    <p class='card-text'>FastAPI is modern, fast, and easy to use. Build APIs like a pro and deploy anywhere!</p>
                                </div>
                            </div>
                        </div>
                        <div class='col-md-4'>
                            <div class='card video-card'>
                                <img src='https://img.youtube.com/vi/tPEE9ZwTmy0/hqdefault.jpg' class='card-img-top' alt='Video'>
                                <div class='card-body'>
                                    <h5 class='card-title'>Get Started</h5>
                                    <p class='card-text'>Clone this repo, run the app, and start building your own YouTube-style platform in minutes!</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'></script>
            </body>
        </html>
        """.replace("{date}", "April 6, 2026")