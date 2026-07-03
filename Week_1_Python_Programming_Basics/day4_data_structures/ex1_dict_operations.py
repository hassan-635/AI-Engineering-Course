
person = {
    "Name": "Ali",
    "Class": "BSCS 6",
    "Section": "A"
}

print(person);

person["Class"] = "BSCS 7 A"

person["CGPA"] = 3.65;

print(person)

person["Address"] = "Kahuta"

print(person)

if "CGPA" in person:
    del person["CGPA"]

print(person)