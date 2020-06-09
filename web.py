from flask import Flask, render_template, request, send_from_directory, json, make_response
import redisdb
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return """
    <script src="js/main.js"></script>
    <h2 id="status"> Status: Ready </h2>
    <form id="searchsubmit">
        <p> Value : </p>
        <input name="value" type="text" />
    </form>
    <button onclick="search()">Search</button>
    """

@app.route('/search')
def search():
    v = request.args.get('value')
    return redisdb.searchforsomething(v)


@app.route('/js/<path:path>')
def send_img(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)