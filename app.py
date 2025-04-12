from aiohttp import web

async def hello(request):
    html_content = """
    <html>
        <head>
            <style>
                body {
                    font-family: 'calibri','Times New Roman';
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: white; /* Set background color to white */
                    color: black; /* Set text color to black */
                    flex-direction: column; /* Align elements vertically */
                    position: relative;
                }
                .content {
                    text-align: center;
                    position: relative;
                    z-index: 2; /* Ensures text stays on top */
                }
                h1 {
                    color: black; /* Ensure h1 text is black */
                    margin-bottom: 300px; /* Add spacing between h1 and h2 */
                    text-align: center;
                     font-size: 30px;
                }
                .social-icons {
                    position: absolute;
                    bottom: 80px;
                    display: flex;
                    gap: 40px;
                    z-index: 2; /* Ensures icons stay above background */
                }
                .social-icons a {
                    text-decoration: none;
                    color: black;
                    font-size: 30px;
                }
                .background {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: url('https://miro.medium.com/v2/resize:fit:1200/1*UVNKMO-SCTeXwPp1hFgu8g.png') no-repeat center center;
                    background-size: 40%;
                    opacity: 100; /* Set opacity to 30% */
                    z-index: 1; /* Place the background behind content */
                }
            </style>
            <!-- Updated Font Awesome CDN link -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        </head>
        <body>
            <div class="background"></div>
            <div class="content">
                <h1>Hello Akash!</h1>
                <h2>Deployment of Akash web app on Akash Console</h2>
            </div>
            <div class="social-icons">
                <a href="https://discord.com" target="_blank"><i class="fab fa-discord"></i></a>
                <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
                <a href="https://youtube.com" target="_blank"><i class="fab fa-youtube"></i></a>
            </div>
        </body>
    </html>
    """
    return web.Response(text=html_content, content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app, port=8080)
