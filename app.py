from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def toupperc():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = text.upper()
    return render_template('touppercase.html', result=result)

@app.route('/area_circle', methods=['GET', 'POST'])
def area_circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = 3.14159 * (radius ** 2)
        except ValueError:
            area = "Invalid input"
    return render_template('area_circle.html', area=area)

@app.route('/area_triangle', methods=['GET', 'POST'])
def area_triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
    return render_template('area_triangle.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# ===== INFIX TO POSTFIX =====
import re

def infix_to_postfix(expression):
    # Add spaces around every operator and parenthesis
    expression = re.sub(r"([+\-*/^()])", r" \1 ", expression)
    expression = expression.strip()

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for token in expression.split():
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    postfix = None
    if request.method == 'POST':
        infix_expr = request.form['infix']
        postfix = infix_to_postfix(infix_expr)
    return render_template('infix_postfix.html', postfix=postfix)

if __name__ == '__main__':
    app.run(debug=True)