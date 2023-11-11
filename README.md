# wyhk-timetable-exporter
 
Ping does not provide the option to export the timetable as `.ics` format, guess I'll have to do it myself

It's just a simple script to request the timetable api to provide everything I need and want

## Screenshots

![Screenshot 2023-11-11 155223](https://github.com/BlissfulAlloy79/wyhk-timetable-exporter/assets/45236703/771711bb-952a-4fdd-805b-bdc2f54e7a6a)

![IMG_0440](https://github.com/BlissfulAlloy79/wyhk-timetable-exporter/assets/45236703/47db7378-a6a0-4611-9f82-98338358ece8)


## How it works

The script send requests with cookies to www.wahyan.edu.hk/timetables to obtain info

A `Token` from the login cookies must be provided to make things work

This means you'll have to manually login via the browser in advance to provide a working token for this script

Ik, ofc ik the captcha is solvable by the machine, ~~I'm just lazy~~ I don't want to make the process complicated :)

2 `.ics` files will be obtained using this program, `day_cycle.ics` and `lesson_timetable.ics`

`day_cycle.ics`:

It should include all the days, cycles, order and events of the day

`lesson_timetable.ics`:

Lesson timetable of each school days, including half day and full day order

## How to use

### Standalone executable

copy `main.exe` from the repo, it can be found in the `/dist/`

execute `main.exe`

a `config.json` file should be generated in the same directory

### Direct execution of source code

> If you feel insecure about executing a suspicious executable file from the internet, I suggest using this method
> 
> Please have python configured

clone the repo

```commandline
pip install -r requirements.txt
```

run the python script

```commandline
python main.py
```

a `config.json` file should be generated in the same directory as the script

### Configuration

You should see the following items in the `config.json` file

```json
{
    "YEAR": 2023,
    "TERM": 1,
    "SID": "",
    "TOKEN": ""
}
```

`YEAR`: school year

`TERM`: school term

`SID`: your student ID (e.g. 23456)

`TOEKN`: your token obtained from cookies

> **How to obtain the token from cookies**
>
> I suggest using *EditThisCookie* extension, it can be found in the chrome store
> 
> Login the timetable, open *EditThisCookie* and you should see a field named `token`
>
> ![image](https://github.com/BlissfulAlloy79/wyhk-timetable-exporter/assets/45236703/2dacb990-cea9-45f6-8fb9-5aa6c32399bb)
>
> Paste the value of this field in the `TOKEN` in `config.json`

### Export the timetable

After configuration, execute the `main.exe` or `main.py` again

> Make sure the `config.json` is in the same directory

Wait for a while, you should see in the console the program is doing its thing

And there you have it, the `.ics` files should appear in the same directory

---
This is just a trashy script done by an exhausted student who is too tired from doing papers and revisions

（；´д｀）ゞ

I am looking forward to any successors from this scu to make a browser script on Tampermonkey that simplifies the entire process

Although ik Ping won't be very happy with it (. ❛ ᴗ ❛.)
