#### 9.1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    criteria_text = ""
    if student_scores[name] > 90:
        criteria_text = "Outstanding"
    elif student_scores[name] > 80:
        criteria_text = "Exceeds Expectations"
    elif student_scores[name] > 70:
        criteria_text = "Acceptable"
    elif student_scores[name] <= 70:
        criteria_text = "Fail"
    student_grades[name] = criteria_text
    
# 🚨 Don't change the code below 👇
print(student_grades)
#### 9.2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_countryV2(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
  
def add_new_country(country, visits, cities):
    travel_log.append({"country":country, "visits":visits, "cities":cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)