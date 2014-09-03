from flask import *
from datetime import datetime
from time import gmtime, strftime

app = Flask(__name__)
end_date = datetime.strptime('Aug 5 2014 4:00PM', '%b %d %Y %I:%M%p')


@app.route('/')
def index():
    time_delta = end_date-datetime.now()
    time_string = strftime("This counter uses %Z time.", gmtime())
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    progress_days = 100 - (float(time_delta.days) / 90.0 * 100.0)
    progress_hours = 100 - (float(hours) / 24.0 * 100.0)
    progress_minutes = 100 - (float(minutes) / 60.0 * 100.0)
    progress_seconds = 100 - (float(seconds) / 60.0 * 100.0)
    progress = [(progress_days, "Days"), (progress_hours, "Hours"),
                (progress_minutes, "Minutes"), (progress_seconds, "Seconds")]
    return render_template("index.html", progress_times=progress, days=time_delta.days, time_string=time_string)

if __name__ == '__main__':
    app.run()
