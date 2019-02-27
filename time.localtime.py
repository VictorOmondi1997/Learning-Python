from time import localtime

activities = {
	8: 'Waking Up',
	9: 'Coding',
	10: 'Learning',
	12: 'Taking Lunch',
	14: 'AfterNoon Lesson',
	22: 'Watch Movies',
	1: 'Sleeping'
}

timeNow=localtime()
hour=timeNow.tm_hour

for activityTime in sorted(activities.keys()):
	if hour<activityTime:
		print(activities[activityTime])
		break
	else:
		print('Unknown, AFK or Sleeping')