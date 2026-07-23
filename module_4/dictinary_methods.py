student={
    "name": "Md.Fahimur Rahman",
    "ID": "0802510405101022",
    'University': "Bangladesh Army University of Science and Technology",
    "asigned courses": ["DSA","JAVA","STATIS"],
    "Course marks":{
        "DSA": 25,
        "STATIS": 85,
        "JAVA" : 25,
    }
}
# print(student.keys())
# print(list (student.values()))
tuples = list (student.items())
# print(tuples[2])
# print(student.get("name 2"))
# print(student["name2"]) #return errr
student.update({
    "Department": "CSE"
})
student.update({
    "city" : "Bogura"
})
new_dict ={"name" :"Md.Adnan Sami Fuad"}
student.update(new_dict)
print(student)
