from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate)) # => 2019-06-25
print(now.toString(Qt.DefaultLocaleLongDate)) # => Tuesday, June 25, 2019

datetime = QDateTime.currentDateTime()

print(datetime.toString()) # => Tue Jun 25 10:34:12 2019

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate)) # => 10:34:12 AM EDT
