from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base_page():
    return render_template('index.html', num1 = 8, num2 = 8, color1 = "black", color2 = "red")

@app.route('/<int:numx>')
def by_x_page(numx):
    return render_template('index.html', num1 = numx, num2 = 8, color1 = "black", color2 = "red")

@app.route('/<int:numx>/<int:numy>')
def by_x_y_page(numx, numy):
    return render_template('index.html', num1 = numx, num2 = numy, color1 = "black", color2 = "red")

@app.route('/<int:numx>/<int:numy>/<string:color1>/<string:color2>')
def by_x_y_color_page(numx, numy, color1, color2):
    return render_template('index.html', num1 = numx, num2 = numy, color1 = color1, color2 = color2)

if __name__ == '__main__':
    app.run(debug = True)