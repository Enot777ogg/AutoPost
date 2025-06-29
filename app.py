from flask import Flask, render_template_string, redirect, url_for, request

app = Flask(__name__)

# Глобальный счетчик (в реальном проекте нужно хранить в базе или Redis)
click_count = 0

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Нажми кнопку!</title>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            padding-top: 50px;
        }
        .btn {
            font-size: 48px;
            padding: 40px 80px;
            background-color: red;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: darkred;
        }
        .message {
            margin-top: 40px;
            font-size: 36px;
            color: green;
            animation: flash 1s infinite alternate;
        }
        @keyframes flash {
            from { color: green; }
            to { color: orange; }
        }
    </style>
</head>
<body>
    <h1>Счетчик нажатий: {{ count }}</h1>
    <form method="post">
        <button class="btn" type="submit">НАЖМИ МЕНЯ</button>
    </form>
    {% if winner %}
        <div class="message">🎉 Вы нажали 10 000 раз! Вы выиграли 1 рубль! 🎉</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global click_count
    winner = False

    if request.method == "POST":
        click_count += 1
        if click_count == 10000:
            winner = True

    return render_template_string(HTML_TEMPLATE, count=click_count, winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
