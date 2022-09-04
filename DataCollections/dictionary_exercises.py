students = {
    "roll_no" : [4,5,3,8,12,22,15],
    "names" : ["John","Shawn","Mac","Sam","Peter","Sid","Nick"],
    "branch" : ["EC","CS","CS","EC","ME","ME","CS"],
    "cgpa" : [7.8,8.9,6.7,9.0,6.5,4.8,8.6]
    }

#find students of CS Branch
for i in range(len(students["roll_no"])):
    if students["branch"][i] == "CS":
        print(students["names"][i], students["branch"][i], students["cgpa"][i])


#find students whose CGPA > 8.0
