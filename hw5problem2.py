employee1 = {
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"}
employee2 = {
    "name": "Leslie Knope",
    "age": 45,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": "$70,000"}
employee3 = {
    "name": "Andy Dwyer",
    "age": 63,
    "department": "Shoe Shining",
    "phone": "555-1122",
    "salary": "$50,000"}
employee4 = {
    "name": "April Ludgate",
    "age": 35,
    "department": "Administration",
    "phone": "555-3345",
    "salary": "$60,000"}
#employees is the company directory
employees = [employee1, employee2, employee3, employee4]
for employee in employees:
  print(employee["name"] ,"in", employee["department"], "can be reached at ", end = '')
  print(employee["phone"],'.', sep = '')
