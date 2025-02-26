from flask import Flask, request, render_template_string

app = Flask(__name__)

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
                window.Telegram.WebApp.sendData(dateStr);
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
