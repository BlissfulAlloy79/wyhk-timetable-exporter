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
COOKIE: dict = {"token": ""}


CFG_DEFAULT = {
    "YEAR": 2023,
    "TERM": 1,
    "SID": "",
    "TOKEN": "",
}


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
        print(TTABLE_URL)
        # calendar = icalendar.Calendar()
        # calendar.add('prodid', "-//WYHK TIMETABLE EXPORTER//BlissfulAlloy79//")
        # calendar.add('version', '2.0')


def event_create(date: str, cycle: str, day: str):
    event = icalendar.Event()
    event.add('summary', f"Day {day}, Cycle {cycle}")
    d = datetime.strptime(date, '%Y-%m-%d').date()
    event.add('dtstart', d)
    event.add('dtend', d)
    event.add('dtstamp', d)

    # calendar.add_component(event)


def main():
    req = requests.get(CAL_URL, cookies=COOKIE)
    print(req.status_code)

    if req.status_code != 200:
        print("Failed")
    else:
        cal = req.json()

        for i in cal:
            # print(i)
            if i["Type"] != "Cycle Day" or i["Display"] != "F":
                pass
            else:
                event_create(date=i["Date"].split('T')[0], cycle=i["Cycle"], day=i["Day"])

        # print(calendar)

        with open('day_cycle.ics', 'wb') as f:
            f.write(calendar.to_ical())


if __name__ == "__main__":
    initiate()




