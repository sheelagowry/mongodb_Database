from datetime import datetime
import random
import string


def Before_1980():

	for i in range(100):
		
		name = "Tom"
		year = random.choice(range(1945, 1980))
       		month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		
		print "db.clients.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"
		

	for i in range(3900):
		

		first_names = {"Jay", "Jim", "Yom", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul", "Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren", "Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet", "Lydia", "Charles", "Pedro", "Bradley"}
		last_names = {"Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers", "Warren", "Keller"}

		first = random.sample(first_names, 1)[0]
		last = random.sample(last_names - {first}, 1)[0]

		year = random.choice(range(1945, 1980))
       		month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		print "db.clients.insert({name:"+"\""+first + " " + last+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

Before_1980()

def After_1990():

	for i in range(100):
        

		name = "Tom"
		last_names = {"Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers", "Warren", "Keller"}
		last = random.sample(last_names, 1)[0]
		year = random.choice(range(1990, 2017))
        	month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)


		print "db.clients.insert({name:"+"\""+name+ " " + last+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

	for i in range(3900):
		

		first_names = {"Jay", "Jim", "Yom", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul", "Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren", "Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet", "Lydia", "Charles", "Pedro", "Bradley"}
		last_names = {"Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers", "Warren", "Keller"}

		first = random.sample(first_names, 1)[0]
		last = random.sample(last_names - {first}, 1)[0]

		year = random.choice(range(1990, 2017))
       		month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		print "db.clients.insert({name:"+"\""+first + " " + last+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

After_1990()

def common_between_1980_1990():

	for i in range(2000):
		

		first_names = {"Jay", "Jim", "Yom", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul", "Ringo", "Ally", "Nicky", "Cam", "Ari", "Trudie", "Cal", "Carl", "Lady", "Lauren", "Ichabod", "Arthur", "Ashley", "Drake", "Kim", "Julio", "Lorraine", "Floyd", "Janet", "Lydia", "Charles", "Pedro", "Bradley"}
		last_names = {"Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers", "Warren", "Keller"}

		first = random.sample(first_names, 1)[0]
		last = random.sample(last_names - {first}, 1)[0]

		year = random.choice(range(1981, 1990))
       		month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		print "db.clients.insert({name:"+"\""+first + " " + last+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

common_between_1980_1990()


