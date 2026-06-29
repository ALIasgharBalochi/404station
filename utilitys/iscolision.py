def calculate(train):
    train_time = train.time_to_move.split(':')
    minut = int(train_time[1])
    hour = int(train_time[0])
    time = (int(train.distance_to_station) / int(train.avarage_speed) ) * 60
    arrival = minut + time
    departure_time = arrival + int(train.stop_time)

    return {"minut": minut,"hour": hour,"arrival": arrival,"departure_time": departure_time}


def isColision(db,new_train):
    trains = db.read_all_data("trains")

    if len(trains) < 1:
        return False

    in_one_line = [train for train in trains if train.line == new_train.line]

    if len(in_one_line) < 1:
        return False
    
    calculate_t2 = calculate(new_train)
    for train in in_one_line:
        calculate_t1 = calculate(train)
        if calculate_t1["hour"] == calculate_t2["hour"]:
            if calculate_t1["arrival"]<=calculate_t2["arrival"]<=calculate_t1["departure_time"]:
                return True
            elif calculate_t1["arrival"]<=calculate_t2["departure_time"]<=calculate_t1["departure_time"]:
                return True
    return False




