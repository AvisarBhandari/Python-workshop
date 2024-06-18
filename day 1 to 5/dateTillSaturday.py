week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
day = input("Enter the day: ").lower()

if day == 'saturday':
    print("Today is Saturday.")
else:
    index = week.index(day)
    days_left = 6 - index
    print("There are", days_left, "days left until Saturday.")
    print("Days left in the week:", ", ".join(week[index+1:]))
