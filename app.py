from flask import Flask, render_template, request

app = Flask(__name__)

def infix_to_postfix(expression):
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
    
    return " ".join(output)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            area = 3.14159 * (radius ** 2)
        except ValueError:
            area = "Invalid input"
    return render_template('circle.html', area=area)

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            area = 0.5 * base * height
        except ValueError:
            area = "Invalid input"
    return render_template('triangle.html', area=area)

@app.route('/infix_postfix', methods=['GET', 'POST'])
def infix_postfix():
    postfix_result = None
    if request.method == 'POST':
        infix_expr = request.form.get('infix', '')
        postfix_result = infix_to_postfix(infix_expr)
    return render_template('infix_postfix.html', result=postfix_result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
