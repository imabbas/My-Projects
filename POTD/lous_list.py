# Aadil Abbas (aa4zw)

import urllib.request




def instructors(department):
    link = 'http://stardock.cs.virginia.edu/louslist/Courses/view/'
    link = link + department
    stream = urllib.request.urlopen(link)
    instructors = []
    for line in stream:
        decoded = line.strip().decode('UTF-8')
        course = decoded.split(';')
        instructors.append(course[4])
        instructors = list(set(instructors))
        instructors.sort()
    return instructors



def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    link = 'http://stardock.cs.virginia.edu/louslist/Courses/view/'
    link = link + dept_name
    stream = urllib.request.urlopen(link)
    course = []
    new_course=[]
    final_course=[]
    for line in stream:
        decoded = line.strip().decode('UTF-8')
        entry = decoded.split(';')
        course.append(entry)

    if has_seats_available is not False:
        for entry in course:
            if int(entry[15]) < int(entry[16]):
                new_course.append(entry)
            if level is not False:
                string=str(level)
                position = int(string[0])
                if position==int(entry[1][0]):
                    final_course.append(entry)
    return final_course

























