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
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .flatpickr-calendar {
            background: #2a2a2a;
            border: 1px solid #444;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            width: 350px;
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
        #confirm-btn {
            margin-top: 20px;
            padding: 12px 24px;
            background-color: #007bff;
            border: none;
            border-radius: 8px;
            color: white;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3);
        }
        #confirm-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="flatpickr-container">
        <input type="text" id="calendar" placeholder="Выбери дату">
    </div>
    <button id="confirm-btn" disabled>Подтвердить</button>
    <script>
        let selectedDate = '';
        const calendar = flatpickr("#calendar", {
            dateFormat: "d.m.Y",
            defaultDate: new Date(),
            theme: "dark",
            onChange: function(selectedDates, dateStr) {
                if (selectedDates.length > 0) {
                    selectedDate = dateStr;
                    document.getElementById("confirm-btn").disabled = false;
                    console.log("Выбрана дата (формат flatpickr):", dateStr); // Отладка формата
                }
            }
        });
        document.getElementById("confirm-btn").addEventListener("click", function() {
            if (selectedDate) {
                console.log("Отправка даты (формат для бота):", selectedDate); // Отладка перед отправкой
                window.Telegram.WebApp.sendData(selectedDate);
                window.Telegram.WebApp.close();
            } else {
                console.log("Дата не выбрана");
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
