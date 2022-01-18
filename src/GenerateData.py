import random
import string
import time
import datetime
import mysql.connector

fullNames = []
phoneNumbers = []
emails = []
passwords = []
streets = []
postals = []

locationID = []
breederID = []
breedID = []
parentID = []
litterID = []
petID = []

breeders = []
users = []
locations = []
breeds = []

description = []
colour = []
weight = []
sex = []
price = []
birth = []
posted = []
dateAdopted = []
dateClosed = []
pBirth = []
pSex = []
parentDescription = []

pets = []
listings = []
parents = []
litters = []

# Initialize intermediate variables for data generation
def randomIndex(start, size):
	return random.randint(start, size-1)

def initializeNames():
	fnames = []
	lnames = []

	# Fill fnames with common male first names
	with open('BoyNames.txt', 'r') as file:
		line = file.readline()
		line = file.readline()  # Skip header
		while line:
			line = line.strip()
			if line != '':
				fnames.append(line)
			line = file.readline()

	# Continuing populating fnames with common female first names
	with open('GirlNames.txt', 'r') as file:
		line = file.readline()
		line = file.readline()  # Skip header
		while line:
			line = line.strip()
			if line != '':
				fnames.append(line)
			line = file.readline()

	# Fill lnames with common last names
	with open('LastNames.txt', 'r') as file:
		line = file.readline()
		line = file.readline()  # Skip header
		while line:
			line = line.strip().lower().capitalize()
			if line != '':
				lnames.append(line)
			line = file.readline()

	# Randomly connect first and last names
	while len(lnames) > 0:
		first = fnames.pop(randomIndex(0, len(fnames)))
		last = lnames.pop(randomIndex(0, len(lnames)))
		fullNames.append(first + " " + last)

def initializePhoneNumbers(limit):
	while len(phoneNumbers) < limit:
		number = "416" + str(randomIndex(1000000, 9999999))
		if number not in phoneNumbers:
			phoneNumbers.append(number)	

def initializeEmails():
	clients = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@outlook.com']

	for name in fullNames:
		nameSplit = name.split()
		emailAddr = nameSplit[0] + '.' + nameSplit[1] + str(randomIndex(1, 9999)) + clients[randomIndex(0,len(clients))] 
		emails.append(emailAddr)

def initializePasswords(limit, stringLength = 10):
    characters = string.ascii_letters + string.digits
    while len(passwords) < limit:
        _password =  ''.join(random.choice(characters) for i in range(stringLength))
        passwords.append(_password)

def initializeStreets():
    with open('StreetNames.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                streets.append(line)
                line = file.readline()

def initializePostals():
    base = ['M4W', 'M5J', 'M5X', 'M5V', 'M5T', 'M5S', 'M5L', 'M5K', 'M5H', 'M4X', 'M5G', 'M5E', 'M5C', 'M5B', 'M5A', 'M4Y', 'M6G']
    letters = string.ascii_letters
    digits = string.digits
    while len(postals) < 2500:
        postal = base[randomIndex(0, len(base))]
        postal = postal + (random.choice(letters)).upper() + (random.choice(digits)) + (random.choice(letters)).upper()
        if(postal not in postals):
            postals.append(postal)

#PARENT birthdate 50
def initializeParentBirthdate(limit):
    i = 0
    while i < limit:
        pBirth.append(getRandomDate("2012-1-1", "2019-4-1"))
        i += 1

# PARENT description 50
def initializeParentDescription(limit):
    list4 = ["healthy","good with kids"]
    list5 = ["energetic","calm","playful"]
    list6 = ["shy","friendly","affectionate"]

    i = 0
    while i < limit:
        parentDescription.append(random.choice(list4)+ ", " + random.choice(list5)+ ", " + random.choice(list6))
        i += 1

# generate random dates def
def getRandomDate(startDate, endDate):
    randomGenerator = random.random()
    dateFormat = '%Y-%m-%d'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

#LITTER birtdate 400
def initializeBirthdate(limit):
    i = 0
    while i < limit:
        birth.append(getRandomDate("2019-1-1", "2019-11-20"))
        i += 1

# LITTERdescription 2000
def initializeDescriptions(limit):
    list1 = ["good","well behaved","updated vaccinations"]
    list2 = ["energetic","calm","playful"]
    list3 = ["shy","friendly","rambunctious"]

    i = 0
    while i < limit:
        description.append((random.choice(list1)+ ", " + random.choice(list2)+ ", " + random.choice(list3)))
        i += 1

# PET colour 2000
def initializeColour(limit):
    col = ["black","grey", "golden brown", "light brown", "dark brown", "white"]
    
    i = 0
    while i < limit:
        colour.append(random.choice(col))
        i += 1

# PET weight 2000
def initializeWeight(limit):
    i = 0
    while i < limit:
        weight.append(round(random.uniform(2.0,10.0), 2))
        i += 1

# PET sex 2000
def initializeSex(limit):
    sexChoice = [0,1]
    i = 0
    while i < limit:
        sex.append(random.choice(sexChoice))
        i += 1

# PET price 2000
def initializePrice(limit):
    priceChoice = [60,70,80,90,100,120,140,160,180,240,260,300,420,560]
    i = 0
    while i < limit:
        price.append(random.choice(priceChoice))
        i += 1

#  PET date adopted 2000
def initializeAdopted(limit):
    i = 0
    while i < limit:
        dateAdopted.append(dateClosed[i])
        i += 1

# LISTING datePosted 2000
def initializePosted(limit):
    i = 0
    while i < limit:
        posted.append(random.choice(birth))
        i += 1



#  Build data for inserting into database
def buildUsers(limit):
    initializeNames()
    initializePhoneNumbers(limit)
    initializeEmails()
    initializePasswords(limit)

    while len(users) < limit:
        nameIndex = randomIndex(0, len(fullNames))
        user = [fullNames.pop(nameIndex), phoneNumbers.pop(randomIndex(0, len(phoneNumbers))), emails.pop(nameIndex), passwords.pop(randomIndex(0, len(passwords))), locationID.pop()]  #locationID
        if len(fullNames) <= 0:
            initializeNames()
            initializeEmails()
        if user not in users:
            users.append(user)

def buildBreeders(limit):
    # Limit should be less than 2000
    initializeNames()
    initializePhoneNumbers(limit)
    initializeEmails()
    initializePasswords(limit)

    i = 0
    while i < limit:
        breeder = [fullNames[i], phoneNumbers[i], emails[i], passwords[i], locationID.pop()]
        breeders.append(breeder)
        i = i + 1

def buildLocations(limit):
    initializePostals()
    initializeStreets()

    while len(locations) < limit:
        loc = ['Ontario', 'Toronto', streets.pop(randomIndex(0, len(streets))), str(randomIndex(10, 9999)), postals.pop(randomIndex(0, len(postals)))]
        if len(postals) <= 0:
            initializePostals()
        if len(streets) <= 0:
            initializeStreets()
        if loc not in locations:
            locations.append(loc)

def buildBreeds():
    with open('DogBreeds.txt', 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                breed = [line]
                breeds.append(breed)
            line = file.readline()

def buildParents(limit):
    initializeParentBirthdate(limit)
    initializeParentDescription(limit)

    petNames = []
    with open('PetNames.txt', 'r') as file:
        line = file.readline()
        line = file.readline()  # Skip header
        while line:
            line = line.strip()
            if line != '':
                petNames.append(line)
            line = file.readline()


    i = 0
    while i < limit:
        _breedID = breedID[randomIndex(0, len(breedID))]
        parent = [_breedID, petNames[randomIndex(0, len(petNames))], pBirth[i], parentDescription[i], 1, breederID[i]]
        parents.append(parent)
        i = i + 1
        parent = [_breedID, petNames[randomIndex(0, len(petNames))], pBirth[i], parentDescription[i], 0, breederID[i-1]]
        parents.append(parent)
        i = i + 1

def buildLitters(limit):
    initializeBirthdate(limit)
    initializeDescriptions(limit)
    i = 0
    parentindex = randomIndex(0, len(parentID))
    while i < limit:
        _parents = []
        if parentindex % 2 == 0:
            _parents = [parentID[parentindex], parentID[parentindex+1]]
        else:
            _parents = [parentID[parentindex], parentID[parentindex-1]]
        parentindex = randomIndex(0, len(parentID))

        mycursor.execute("SELECT breed_id FROM Parent WHERE parent_id = '" + str(_parents[0]) + "';")
        _breedID = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT breeder_id FROM Parent WHERE parent_id = '" + str(_parents[0]) + "';")
        _breederID = mycursor.fetchall()[0][0]

        litter = [_breedID, birth[i], _parents[0], _parents[1], _breederID, description[i]]
        litters.append(litter)
        i = i + 1

def buildPets(limit):
    #initializeAdopted(limit)
    initializeColour(limit)
    initializeSex(limit)
    initializePrice(limit)
    initializeWeight(limit)

    petsPerLitter = limit / len(litterID)

    i = 0
    litterIndex = 0
    while i < limit:
        pet = [colour[i], weight[i], price[i], sex[i], None, litterID[litterIndex], None]
        pets.append(pet)
        i = i + 1
        if i % petsPerLitter == 0:
            litterIndex += 1

def buildListings(limit):
    initializePosted(limit)
    #initializeClosed(limit)

    i = 0
    while i < limit:
        litterIndex = randomIndex(0, len(litterID))
        closedDate = datetime.datetime.strptime(posted[i], '%Y-%m-%d') + datetime.timedelta(days=14)
        listing = [litterID[litterIndex], posted[i], closedDate, "Litter for sale"]
        listings.append(listing)
        i = i + 1



buildLocations(3500)
buildBreeds()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="pawprint"
)

mycursor = mydb.cursor()

for location in locations:
    sql = "INSERT INTO Location (province, city, street, address_number, postal_code) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, location)
    mydb.commit()
    mycursor.execute("SELECT location_id FROM Location ORDER BY location_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    locationID.append(myresult[0][0])

buildUsers(3000)
buildBreeders(500)

sql = "INSERT INTO User (name, phone_number, email, password, location_id) VALUES (%s, %s, %s, %s, %s)"
mycursor.executemany(sql, users)
mydb.commit()

for breeder in breeders:
    sql = "INSERT INTO Breeder (name, phone_number, email, password, location_id) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, breeder)
    mydb.commit()
    mycursor.execute("SELECT breeder_id FROM Breeder ORDER BY breeder_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    breederID.append(myresult[0][0])

for breed in breeds:
    sql = "INSERT INTO Breed (breed_name) VALUES (%s)"
    mycursor.execute(sql, breed)
    mydb.commit()
    mycursor.execute("SELECT breed_id FROM Breed ORDER BY breed_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    breedID.append(myresult[0][0])

buildParents(50)
for parent in parents:
    sql = "INSERT INTO Parent (breed_id, name, birth_date, description, sex_m, breeder_id) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, parent)
    mydb.commit()
    mycursor.execute("SELECT parent_id FROM Parent ORDER BY parent_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    parentID.append(myresult[0][0])

buildLitters(400)
for litter in litters:
    sql = "INSERT INTO Litter (breed_id, birth_date, parent_1_id, parent_2_id, breeder_id, description) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, litter)
    mydb.commit()
    mycursor.execute("SELECT litter_id FROM Litter ORDER BY litter_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    litterID.append(myresult[0][0])

buildPets(2000)
for pet in pets:
    sql = "INSERT INTO Pet (colour, weight, price, sex_m, date_adopted, litter_id, adopter_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, pet)
    mydb.commit()
    mycursor.execute("SELECT pet_id FROM Pet ORDER BY pet_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    petID.append(myresult[0][0])

buildListings(400)
sql = "INSERT INTO Listing (litter_id, date_posted, date_closed, title) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql, listings)
mydb.commit()
