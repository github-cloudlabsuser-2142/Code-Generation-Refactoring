<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Calculator</title>
</head>
<body>
    <h1>Basic Calculator</h1>
    <form id="calculator">
        <input type="number" id="num1" placeholder="Enter first number" required>
        <select id="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" id="num2" placeholder="Enter second number" required>
        <button type="button" onclick="calculate()">Calculate</button>
    </form>
    <h2>Result: <span id="result">0</span></h2>

    <script>
        function calculate() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const operation = document.getElementById('operation').value;
            let result;

            if (isNaN(num1) || isNaN(num2)) {
                alert('Please enter valid numbers');
                return;
            }

            switch (operation) {
                case 'add':
                    result = num1 + num2;
                    break;
                case 'subtract':
                    result = num1 - num2;
                    break;
                case 'multiply':
                    result = num1 * num2;
                    break;
                case 'divide':
                    if (num2 === 0) {
                        alert('Division by zero is not allowed');
                        return;
                    }
                    result = num1 / num2;
                    break;
                default:
                    alert('Invalid operation');
                    return;
            }

            document.getElementById('result').textContent = result;
        }
    </script>
</body>
</html>