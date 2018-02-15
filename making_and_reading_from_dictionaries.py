person = {
	"name": "Daniel",
	"age": 28,
	"country_of_birth": "United States",
	"favorite_language": "Javascript"
}

def printPerson(person):
	print "My name is " + person["name"]
	print "My age is " + str(person["age"])
	print "My country of birth is " + person["country_of_birth"]
	print "My favorite language is " + person["favorite_language"]

printPerson(person)