# pause 1 - print "lille" from the nested list called travel_log
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# print(travel_log["France"][1])
# print the value for key "France" and slice the list for the 2nd item

# pause 2 - print "D" from the list "nested_list"

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# pause 3 - print "Stuttgart" from the new travel_log list

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
# print 3rd item of list which is value of key which is value of key of travel_log
