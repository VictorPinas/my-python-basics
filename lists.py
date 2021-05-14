# lists, tuples and sets
# lists and tuples allow us to work with sequencial data
# and sets are unordered sequences of values
# lists have more functionallity than the other data types

# lists
# courses = ['History', 'Math', 'Physics', 'Comp. Science']
# nums = [1, 5, 2, 4, 3]
# courses.reverse()
# courses.sort()
# sorted_courses = sorted(courses)
# courses.sort(reverse=True)
# nums.sort(reverse=True)
# nums.sort()
# courses.remove('Math')
# courses.pop()
# popped = courses.pop()
# print(popped)
# courses_2 = ['Art', 'Education']
# courses.append('Art')
# courses.insert(0, 'Art')
# courses.insert(0, courses_2)
# courses.extend(courses_2)
# print(len(courses))
# print(courses)
# print('Art' in courses)
# print('Math' in courses)
# print(sorted_courses )
# print(nums)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(courses[0])
# print(courses[3])
# print(courses[-1])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

# for item in courses:
    # print('Math' in courses)

# for item in courses:
    # print(item)

# for course in courses:
    # print(course)

# for index, course in enumerate(courses):
    # print(index, course)

# for index, course in enumerate(courses, start=1):
    # print(index, course)

# it is interesting turn our list into a string separeted by a certain value
# this is done using the 'join' operator
# course_str = ', '.join(courses)
# course_str = ' - '.join(courses)
# new_list = course_str.split(' - ')
# print(course_str)
# print(new_list)

# tuples and sets
# tuples cannot be modified
# Mutable
#list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
# when you print set values many times, it shows up different values
# because sets really don't care about order
# some of the uses of sets is either when a value is part of the set and
# to remove duplicate values, because sets throw away duplicates
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses)
# print('Math' in cs_courses)
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))


# Empty Lists
# empty_list = []
# empty_list = list()

# Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()
