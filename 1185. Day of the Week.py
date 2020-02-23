class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def leapYear(year):
            return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
        
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # start from today's day, i.e. today (2020/02/23) is sunday
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        # days passed from 1971/01/01
        def daysPassed(year, month, day):
            days = 0
            for i in range(1971, year):
                days += 365 + leapYear(i)
            days += sum(daysInMonth[:month - 1])
            days += day
            if month > 2: days += leapYear(year) # don't forget this
            return days
        
        today = daysPassed(2020, 2, 23)
        query = daysPassed(year, month, day)
        return week[(query - today) % 7] # not today - query
