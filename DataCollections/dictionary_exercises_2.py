students = [
    {"name" : "John", "branch" : "EC", "roll_no":4, "cgpa":7.8},
    {"name" : "Shawn", "branch" : "CS", "roll_no":6, "cgpa":6.8},
    {"name" : "Mac", "branch" : "CS", "roll_no":12, "cgpa":7.9},
    {"name" : "Sam", "branch" : "EC", "roll_no":14, "cgpa":8.7},
    {"name" : "Peter", "branch" : "ME", "roll_no":6, "cgpa":9.5},
    {"name" : "Sid", "branch" : "ME", "roll_no":11, "cgpa":6.3},
    {"name" : "Nick", "branch" : "CS", "roll_no":9, "cgpa":5.5}
    ]

for i in range(len(students)):
    if students[i]["branch"] == "CS":
        print(students[i]["name"], students[i]["branch"], students[i]["cgpa"])
