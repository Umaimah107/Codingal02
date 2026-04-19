#import numpy as np
#import matplotlib.pyplot as plt

#data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
#courses = list(data.keys())
#values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

#plt.bar(courses, values, color = 'maroon', width = 0.4)

#plt.xlabel("Courses offered")
#plt.ylabel("no. of students enrolled")
#plt.title("students enrolled in different courses")
#plt.show()

import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25
fig = plt.subplots(figsize = (12,8))

IT = [12, 30, 1]