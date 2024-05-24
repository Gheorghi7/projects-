from playsound import playsound 
import datetime 

alarmHour = int(input('Enter hour: '))
alarmMin = int(input('Enter min: '))
#alarmAm = input('AM/PM: ')

#if alarmAm == 'pm':
#    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print('Playing...')
        playsound("zvuk-lyagushki-korotkiy-28632.mp3")




