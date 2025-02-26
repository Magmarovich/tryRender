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
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .flatpickr-container {
            width: 350px;
        }
        .flatpickr-calendar {
            background: rgba(42, 42, 42, 0.9);
            border: 1px solid #444;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            width: 100%;
            height: 400px;
            margin-top: 20px;
            overflow: hidden;
            max-width: 100%;
            max-height: 100%;
        }
        .flatpickr-month {
            background: #2a2a2a;
            color: #fff;
            font-size: 20px;
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #444;
        }
        .flatpickr-weekdays {
            background: #2a2a2a;
            color: #aaa;
            font-weight: bold;
            padding: 10px 0;
            border-bottom: 1px solid #444;
        }
        .flatpickr-weekday {
            text-align: center;
            font-size: 16px;
        }
        .flatpickr-days {
            padding: 10px;
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 5px;
            height: calc(100% - 80px);
            overflow: hidden;
        }
        .flatpickr-day {
            background: none;
            border: 2px solid transparent;
            color: #fff;
            font-size: 18px;
            width: 40px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            margin: 0;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .flatpickr-day:hover {
            border-color: #28a745;
        }
        .flatpickr-day.selected {
            border-color: #28a745;
            background: #28a745;
            color: #fff;
        }
        .flatpickr-prev-month, .flatpickr-next-month {
            color: #fff;
            background: #3a3a3a;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 16px;
        }
        .flatpickr-prev-month:hover, .flatpickr-next-month:hover {
            background: #555;
        }
        .flatpickr-day.disabled {
            color: #666;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <div class="flatpickr-container">
        <div id="calendar"></div>
    </div>
    <script>
        let selectedDate = '';
        const calendar = flatpickr("#calendar", {
            inline: true,
            defaultDate: new Date(),
            dateFormat: "d.m.Y",
            theme: "dark",
            onChange: function(selectedDates, dateStr) {
                if (selectedDates.length > 0) {
                    selectedDate = dateStr;
                    console.log("Выбрана дата:", selectedDate);
                    if (window.Telegram && window.Telegram.WebApp) {
                        window.Telegram.WebApp.sendData(selectedDate);
                        window.Telegram.WebApp.close();
                    } else {
                        console.error("Telegram.WebApp недоступен. Пожалуйста, откройте это в Telegram Web App.");
                        // Для отладки: отправляем данные через форму (если WebApp недоступен)
                        alert("Дата выбрана для тестирования: " + selectedDate);
                    }
                }
            }
        });
        // Проверка доступности Telegram.WebApp
        if (window.Telegram && window.Telegram.WebApp) {
            window.Telegram.WebApp.expand(); // Увеличиваем Web App на полный экран
            window.Telegram.WebApp.ready();
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
