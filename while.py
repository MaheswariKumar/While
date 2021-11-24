#Chapter-7
#While loop
#introduction
num = 1
while num <= 5:
	print(num)
	num += 1

#letting user to quit 
prompt = "hi enter something: "
prompt += "enter to quit: "
msg = ""
while msg != "quit":
	msg = input(prompt)
	#if condition will print only when user not using quit word 
	if msg != "quit":
		print(msg)

#flag variable
active = True
while active:
	msg = input("enter: ")
	if msg == "quit":
		active = False
	elif msg == "mahi":
		active = False
	else:
		print(msg)
#Using break to exit loop
while True:
	visit = input("enter: ")
	if visit == "chennai":
		break
	else:
		print("I have visited " + str(visit))

#Using continue in Loop
my_num = 0
while my_num < 10:
	my_num += 1
	if my_num % 2 == 0:
		continue
	print(my_num)

#Avoiding infinite loops

#Ass-1
order = ""
while order != "done":
	order = input("enter your order: ")
	if order != "done":
		print("your " + str(order) + " added")

#Ass-2
age = ""
while True:
	age = int(input("enter your age: "))
	if age == 3:
		print("free")
	elif age < 45:
		print("$3 doller")
	elif age >= 50:
		break

#Ass-3
active = True
while active:
	seats = int(input("enter your seats: "))
	if seats == 5:
		break
	elif seats == 7:
		active = False
	else:
		print("add members, seats are available")

#Using a while Loop with Lists and Dictionaries
#moving one item from one lsit another list
un_confirm = ["mahi", "prithi", "sumathi"]
confirm = []
while un_confirm:
	new = un_confirm.pop()
	print("these names are should be verify: " + str(new))
	confirm.append(new)

print("The following names are verified: ")
for confirms in confirm:
	print(confirms)

#removing all insatances of value in the list(several occurances of value)
pets = ["cat", "dog", "parrot", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
	pets.remove("cat")

print(pets)

#filling dict using while loop
responses = {}
polling_active = True
while polling_active:
	name = input("enter the name: ")
	response = input("tell your fav hills: ")
	responses[name] = response

	repeat = input("you want to take again poll: \n YES or NO: ")
	if repeat == "NO":
		polling_active = False

for name, response in responses.items():
	print(str(name) + " fav hills is: " + str(response))

#Ass-1
sandwich_order = ["panner", "onion","mushroom"]
finished = []
while sandwich_order:
	new = sandwich_order.pop()
	print("I made your " + str(new) + " sandwich")
	finished.append(new)

print("Finally ready with your sandwich_order: \n")
for finished_1 in finished:
	print(finished_1)

#Ass-2
sandwich_order = ["panner", "chicken", "onion", "chicken", "mushroom", "chicken"]
finished = []

while "chicken" in sandwich_order:
	sandwich_order.remove("chicken")
print("chicken sandwich is not available right now: \n")
print("your finished order will endup without chicken sandwich \n")
print(sandwich_order)

while sandwich_order:
	new = sandwich_order.pop()
	print("I made your " + str(new) + " sandwich")
	finished.append(new)

print("Finally ready with your sandwich_order: \n")
for finished_1 in finished:
	print(finished_1)

#Ass-3
poll = {}
active = True
while active:
	name = input("name plz: ")
	fav_plc = input("enter your fav plc: ")

	poll[name] = fav_plc

	repeat = input("if you want to take poll again : \n yes or no: ")
	if repeat == "no":
		active = False

for name, fav_plc in poll.items():
	print(str(name) + ":" + str(fav_plc))