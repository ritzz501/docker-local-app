from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Docker Local App</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 0; background: #f3f6fb; color: #172b4d; }
          main { max-width: 720px; margin: 10vh auto; padding: 40px; background: white;
                 border-radius: 14px; box-shadow: 0 8px 28px #172b4d18; }
          h1 { color: #1456a0; }
          .status { display: inline-block; padding: 8px 12px; border-radius: 20px;
                    background: #e4f7ec; color: #16723b; font-weight: bold; }
        </style>
      </head>
      <body>
        <main>
          <span class="status">Container is running</span>
          <h1>Hello from Docker!</h1>
          <p>This web application is running locally inside a Docker container.</p>
          <p><strong>Project:</strong> Build and Run Docker App Locally</p>
        </main>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
