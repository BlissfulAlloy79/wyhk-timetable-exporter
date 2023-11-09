# wyhk-timetable-exporter
 
Ping does not provide the option to export the timetable as `.ics` format, guess I'll have to do it myself

It's just a simple script to request the timetable api to provide everything I need and want

## How it works

The script uses `cookies` to send requests to timetable api in order to obtain all the results

A `Token` must be provided to make things work

This means you'll have to manually login via the browser to obtain the token before running this script

Ik, ofc ik the captcha is solvable by the machine, but adding that part will only increase the complexity of this script

> The `day_cycle.ics` file simply contains only the cycle and day

> If you want the personalized lesson timetable, execution of the script is needed

The script is in early development stage, documentation is not provided yet

(I don't think there's really a need for documenting this trash script :P