#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
def make_chocolate(small, big, goal):
	if (big*5 + small) < goal:
		return(-1)
	if goal%5 > small:
		return(-1)
	if goal//5 > big:
		return(goal-big*5)
	else:
		return(goal-((goal//5)*5))
print(make_chocolate(4, 1, 9))
print(make_chocolate(5, 1, 10))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
print(make_chocolate(6, 2, 7))
print(make_chocolate(6, 1, 11))
