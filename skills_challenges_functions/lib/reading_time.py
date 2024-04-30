import math

def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for an empty text.")
    else:
        words = text.split()
        num_words = len(words)
        words_per_minute = 200
        reading_time_minutes = num_words / words_per_minute
        reading_time_minutes = math.ceil(reading_time_minutes)

        return reading_time_minutes
