import requests
import json

urlBaseClass = 'http://bellevuecollege.edu/classes/All/'
urlJsonSuffx = '?format=json'

# All Courses
responseAll = requests.get('{}{}'.format(urlBaseClass,urlJsonSuffx))

# All Computer Science Courses
# responseCourses = requests.get('http://www.bellevuecollege.edu/classes/All/CS/?format=json')

responseJson = responseAll.json()
# {'CoursePrefixes': ['ACCT'], 'Slug': 'ACCT', 'Title': 'Accounting'}
print(responseJson)
# Initialize class dictionary and json keys
classDict = {}
keyPrefix = 'CoursePrefixes'
keySubjects = 'Subjects'
keyCourses = 'Courses'
keyCourseID = 'CourseID'
keyTitle = 'Title'
keySlug = 'Slug'

print("Sorting through class offerings...")
for items in responseJson[keySubjects]:
    if items[keyPrefix] in list(classDict.keys()):
        # if the class dictionary already contains the slug
        # print(items[keyPrefix])
        test = items[keyPrefix]
    else:
        # add the slug and create a new class list
        classDict[items[keySlug]] = []
        # print(items[keySlug])

# Get the class list for each slug
print("Pulling class data for each slug...")
for slugs in list(classDict.keys()):
    responseSlug = requests.get('{}{}{}'.format(urlBaseClass, slugs, urlJsonSuffx))

    # Not all slugs have corresponding pages 
    if responseSlug.status_code == 200:
        responseSlugJson = responseSlug.json()
        print(responseSlugJson)
        f = open("test.txt", "a")
        f.write(json.dumps(responseSlugJson))
        f.write("\n")
        f.close()
        for slugClass in responseSlugJson[keyCourses]:
            classDict[slugs].append((slugClass[keyCourseID], slugClass[keyTitle]))
            # print(slugClass[keyCourseID] + ' ' + slugClass[keyTitle])
    else:
        print('Failed to get proper response for class slug: {}'.format(slugs))

# response[Courses] CourseID, Title

# Print out the API Json response 
print(responseAll.text)


# All Course subjects   http://bellevuecollege.edu/classes/All/?format=json
# Courses by subject    http://bellevuecollege.edu/classes/All/ slug /?format=json
# Quarter offering      http://bellevuecollege.edu/classes/ quarter /?format=json
# Section offerings     http://bellevuecollege.edu/classes/ quarter / subject /?format=json (subject might be slug)