from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        rating = request.form.get('rating')
        return render_template('feedback.html', name=name, email=email, message=message, rating=rating)
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)