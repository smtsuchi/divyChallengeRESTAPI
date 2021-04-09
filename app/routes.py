from app import app
from flask import render_template, request
from app.models import Divvy

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    req = request.args.to_dict()
    keys = req.keys()
    if 'start' in keys and 'end' in keys:
        from_station_id = req.get('from_station_id', None)
        s = req['start']
        e = req['end']
        divvy = Divvy.query.filter(Divvy.starttime.between(s,e)).all()
        length = len(divvy)
        total_duration = 0
        for i in range(length):
            total_duration = total_duration + divvy[i].trip_duration
        average_duration = total_duration/length
        # print('start: ', divvy_start, "end: ",divvy_end)
        if from_station_id:
            filtered_divvy = w
            return {
                "average_duration": total_duration,
                "from_station_id": from_station_id,
                "from_station_name": from_station_name
                }
        return {"average_duration": average_duration}
    print(req)
    return {"A": "TEST", "B": req}