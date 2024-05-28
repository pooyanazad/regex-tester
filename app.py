from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        import re
        regex = request.form['regex']
        test_string = request.form['test_string']
        try:
            if re.search(regex, test_string):
                result = "Match found!"
            else:
                result = "No match found."
        except re.error:
            result = "Invalid regex pattern."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
