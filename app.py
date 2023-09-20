from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

@app.route('/print/<string_param>')
def print_string(string_param):
    # Print the string in the console
    print(f"Printed String: {string_param}")
    # Display the string in the web browser
    return f"<p>Printed String: {string_param}</p>"

@app.route('/count/<int:int_param>')
def count(int_param):
    # Generate a list of numbers in the range of the parameter
    numbers = '\n'.join(str(num) for num in range(1, int_param + 1))
    return f"<pre>{numbers}</pre>"

@app.route('/math/<float_param1>/<operation>/<float_param2>')
def math(float_param1, operation, float_param2):
    # Convert the input parameters to float
    num1 = float(float_param1)
    num2 = float(float_param2)

    # Perform the specified operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return f"<p>Result of {num1} {operation} {num2} = {result}</p>"

if __name__ == '__main__':
    app.run(debug=True)
