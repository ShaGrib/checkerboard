from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base_page():
    return render_template('index.html', num1 = 8, num2 = 8)

@app.route('/<int:numx>')
def by_x_page(numx):
    return render_template('index.html', num1 = numx, num2 = 8)

@app.route('/<int:numx>/<int:numy>')
def by_x_y_page(numx,numy):
    return render_template('index.html', num1 = numx, num2 = numy)

if __name__ == '__main__':
    app.run(debug = True)