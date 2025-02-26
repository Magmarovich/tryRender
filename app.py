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
            overflow: hidden;
        }
        .flatpickr-calendar {
            background: #2a2a2a;
            border: 1px solid #444;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            width: 350px;
            margin: 0 auto;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .flatpickr-month {
            background: #2a2a2a;
            color: #fff;
            font-size: 20px;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .flatpickr-weekdays {
            background: #2a2a2a;
            color: #aaa;
            font-weight: bold;
            padding: 10px 0;
        }
        .flatpickr-weekday {
            text-align: center;
        }
        .flatpickr-days {
            padding: 10px;
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
            margin: 5px;
            border-radius: 10px;
            display: inline-block;
            cursor: pointer;
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
        }
        .flatpickr-prev-month:hover, .flatpickr-next-month:hover {
            background: #555;
        }
    </style>
</head>
<body>
    <div class="flatpickr-container">
        <div id="calendar"></div> <!-- Прямая инициализация календаря без input -->
    </div>
    <script>
        let selectedDate = '';
        const calendar = flatpickr("#calendar", {
            inline: true, // Открываем календарь сразу, без поля ввода
            defaultDate: new Date(),
            dateFormat: "d.m.Y",
            theme: "dark",
            onChange: function(selectedDates, dateStr) {
                if (selectedDates.length > 0) {
                    selectedDate = dateStr;
                    console.log("Выбрана дата (формат flatpickr):", dateStr);
                    if (window.Telegram && window.Telegram.WebApp) {
                        window.Telegram.WebApp.sendData(dateStr);
                        window.Telegram.WebApp.close();
                    } else {
                        console.error("Telegram.WebApp не доступен");
                    }
                }
            }
        });
        window.Telegram.WebApp.ready();
        console.log("WebApp инициализирован");
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
