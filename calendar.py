import re 
def calendar():
    day = input('What day? ')
    while (day < 30):
      activity = raw_input('What are you doing on that day? ')
      time = raw_input('What time is that activity? ')
      other = raw_input('What else are you doing? ')
      if (other = 'none'):
        print day
        return time + " " + activity
      else:
        time2 = raw_input('What time is that activity? ')
        print day
        return time + " " + activity + " " + time2 + " " + other

print calendar()
