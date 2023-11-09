import requests
import json
import os
import icalendar
from datetime import datetime

# constants
YEAR: int = 2023
TERM: int = 1
SID: str = ""
TOKEN: str = ""
CAL_URL = "https://www.wahyan.edu.hk/timetable-api/api/calendar"
TTABLE_URL: str = ""
EVENT_URL: str = "https://www.wahyan.edu.hk/timetable-api/api/student-events?date="
COOKIE: dict = {"token": ""}
CALENDAR: list
TIMETABLE: list
FDAY_START: list = ["08:15", "08:55", "09:50", "10:30", "11:25", "12:05", "14:05", "14:10", "14:20", "15:00"]
FDAY_END: list = ["08:55", "09:35", "10:30", "11:10", "12:05", "12:45", "14:10", "14:20", "15:00", "15:40"]


CFG_DEFAULT = {
    "YEAR": 2023,
    "TERM": 1,
    "SID": "",
    "TOKEN": "",
}

day_cal = icalendar.Calendar()
lsn_cal = icalendar.Calendar()


def initiate():
    global YEAR, TERM, SID, TOKEN, TTABLE_URL, COOKIE
    if not os.path.exists('./config.json'):
        print("config.json not found, creating...")
        with open("config.json", 'w') as f:
            json.dump(CFG_DEFAULT, f, indent=4)
        print("config.json initiated, please complete the info")
        exit()
    else:
        with open("config.json", 'r') as f:
            cfg: dict = json.load(f)
        YEAR, TERM, SID, TOKEN = cfg.values()
        TTABLE_URL = f"https://www.wahyan.edu.hk/timetable-api/api/student-timetable?year={YEAR}&term={TERM}&student={SID}"
        COOKIE["token"] = TOKEN

        day_cal.add('prodid', "-//WYHK TIMETABLE EXPORTER//BlissfulAlloy79//")
        day_cal.add('version', '2.0')
        lsn_cal.add('prodid', "-//WYHK TIMETABLE EXPORTER//BlissfulAlloy79//")
        lsn_cal.add('version', '2.0')


def day_event_create(date: str, cycle: str, day: int):
    event = icalendar.Event()
    event.add('summary', f"Day {day}, Cycle {cycle}")
    d = datetime.strptime(date, '%Y-%m-%d').date()
    event.add('dtstart', d)
    event.add('dtend', d)
    event.add('dtstamp', d)

    day_cal.add_component(event)


def lesson_event_create(date: str, day: int):
    global FDAY_START, FDAY_END
    tdy = TIMETABLE[day - 1]
    for i in range(10):
        event = icalendar.Event()
        event.add('summary', tdy[f"P{i+1}_Subj"])
        event.add('dtstart', datetime.strptime(f"{date} {FDAY_START[i]}", '%Y-%m-%d %H:%M'))
        event.add('dtend', datetime.strptime(f"{date} {FDAY_END[i]}", '%Y-%m-%d %H:%M'))
        event.add('dtstamp', datetime.strptime(f"{date} {FDAY_START[i]}", '%Y-%m-%d %H:%M'))
        lsn_cal.add_component(event)


def main():
    global CALENDAR, TIMETABLE
    initiate()

    cal_req = requests.get(CAL_URL, cookies=COOKIE)
    ttable_req = requests.get(TTABLE_URL, cookies=COOKIE)
    print(cal_req.status_code)
    print(ttable_req.status_code)

    if cal_req.status_code != 200:
        print("Calendar request failed")
    if ttable_req.status_code != 200:
        print("Timetable requests failed")
    else:
        CALENDAR = cal_req.json()
        TIMETABLE = ttable_req.json()

        for i in CALENDAR:
            if i["Type"] != "Cycle Day" or i["Display"] != "F":
                pass
            else:
                date = i["Date"].split('T')[0]
                day = i["Day"]
                day_event_create(date=date, cycle=i["Cycle"], day=day)
                lesson_event_create(date=date, day=day)

        with open('day_cycle.ics', 'wb') as f:
            f.write(day_cal.to_ical())
        with open('lesson_timetable.ics', 'wb') as f:
            f.write(lsn_cal.to_ical())


if __name__ == "__main__":
    main()




