from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML-шаблон с календарём
calendar_html = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
</head>
<body>
    <input type="text" id="calendar" placeholder="Выбери дату">
    <script>
        flatpickr("#calendar", {
            dateFormat: "d.m.Y",
            onChange: function(selectedDates, dateStr) {
                window.Telegram.WebApp.sendData(dateStr);  // Отправляем дату в бота
                window.Telegram.WebApp.close();  // Закрываем Web App
            }
        });
        window.Telegram.WebApp.ready();  // Сообщаем Telegram, что приложение готово
    </script>
</body>
</html>
"""

@app.route('/calendar')
def calendar():
    return render_template_string(calendar_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)