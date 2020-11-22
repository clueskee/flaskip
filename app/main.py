import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
    ip_addr = flask.request.remote_addr
    return f"""
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Twoje IP</title>
  <meta name="description" content="IP">
  <meta name="PB" content="Returns ip">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
    <center>
        <H1>IP: {ip_addr} </H1>
    </center>
</body>
</html>
    """


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
