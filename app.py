from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

calendar_html = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
    <style>
        /* Ваши стили */
    </style>
</head>
<body>
    <div class="flatpickr-container">
        <div id="calendar"></div>
    </div>
    <script>
        // Инициализация календаря
        const calendar = flatpickr("#calendar", {
            inline: true,
            defaultDate: new Date(),
            dateFormat: "d.m.Y",
            theme: "dark",
            onChange: function(selectedDates, dateStr) {
                if (selectedDates.length > 0) {
                    console.log("Выбрана дата:", dateStr);

                    // Проверка, что Web App запущен в Telegram
                    if (window.Telegram && window.Telegram.WebApp) {
                        // Отправляем данные в Telegram
                        window.Telegram.WebApp.sendData(dateStr);
                        console.log("Данные отправлены в Telegram:", dateStr);

                        // Закрываем Web App
                        window.Telegram.WebApp.close();
                    } else {
                        console.error("Telegram.WebApp недоступен. Пожалуйста, откройте это в Telegram Web App.");
                    }
                }
            }
        });

        // Инициализация Web App
        if (window.Telegram && window.Telegram.WebApp) {
            window.Telegram.WebApp.expand(); // Развернуть Web App на весь экран
            window.Telegram.WebApp.ready(); // Готовность Web App
            console.log("WebApp инициализирован");
        } else {
            console.warn("Telegram WebApp API не найден. Убедитесь, что вы используете это в Telegram.");
        }
    </script>
</body>
</html>
"""

@app.route('/calendar')
def calendar():
    return render_template_string(calendar_html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
