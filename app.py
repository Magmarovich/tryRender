from flask import Flask, request, render_template_string

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
        }
        .flatpickr-day {
            color: #fff;
        }
        .flatpickr-day.selected {
            background: #007bff;
            border-color: #007bff;
        }
        .flatpickr-day:hover {
            background: #555;
        }
        #confirm-btn {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            color: white;
            cursor: pointer;
            font-size: 16px;
        }
        #confirm-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <input type="text" id="calendar" placeholder="Выбери дату">
    <button id="confirm-btn" disabled>Подтвердить</button>
    <script>
        let selectedDate = '';
        flatpickr("#calendar", {
            dateFormat: "d.m.Y",
            onChange: function(selectedDates, dateStr) {
                selectedDate = dateStr;
                document.getElementById("confirm-btn").disabled = false;
            },
            theme: "dark"
        });
        document.getElementById("confirm-btn").addEventListener("click", function() {
            if (selectedDate) {
                window.Telegram.WebApp.sendData(selectedDate);
                window.Telegram.WebApp.close();
            }
        });
        window.Telegram.WebApp.ready();
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
