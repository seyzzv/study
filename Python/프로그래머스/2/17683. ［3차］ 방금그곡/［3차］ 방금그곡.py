def replace_notes(sheet):
    sheet = sheet.replace("C#", "c")
    sheet = sheet.replace("D#", "d")
    sheet = sheet.replace("F#", "f")
    sheet = sheet.replace("G#", "g")
    sheet = sheet.replace("A#", "a")
    sheet = sheet.replace("B#", "b")
    sheet = sheet.replace("E#", "e")
    return sheet


def solution(m, musicinfos):
    m = replace_notes(m)
    best_music = None
    max_duration = -1

    for info in musicinfos:
        start_time, end_time, title, sheet = info.split(",")

        start_h, start_m = map(int, start_time.split(":"))
        end_h, end_m = map(int, end_time.split(":"))
        duration = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        sheet = replace_notes(sheet)

        sheet_len = len(sheet)
        if duration <= sheet_len:
            played_melody = sheet[:duration]
        else:
            played_melody = sheet * (duration // sheet_len) + sheet[: duration % sheet_len]

        if m in played_melody:

            if duration > max_duration:
                max_duration = duration
                best_music = title

    return best_music if best_music else "(None)"