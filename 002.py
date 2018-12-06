# indent python code to put into an email
import glob
# glob supports unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
	print ('---------' + file_name)
	with open(file_name) as f:
		for line in f:
			print ('    ' + line.rstrip())
	print


from time import localtime

activities = {7: 'sleeping',
              9: 'commuting',
              17: 'working',
              18: 'dinner',
              20: 'commuting',
              22: 'resting'}
time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print (activities[activity_time])
        break
    else:
        print ('unknown, afk or sleeping')
