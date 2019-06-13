list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[n]:list2[n] for n in range(0,2)}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]


answer1 = dict()
# use the person variable in your answer
for i in range(0, 3):
    answer1[person[i][0]] = person[i][1]  # we add a new key from the list to the 'answer' dictionary, and set it to equal to the second element of the sublist
    i += 1
#print(person[1][0])
print(answer1)

answer2 = {k:0 for k in ("a","i","e","i","o","u")}
print(answer2)

answer3 = {k:chr(k) for k in range(65,91)}
print(answer3)