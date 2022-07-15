# autor: Patryk Wittbrodt
# WZ_INIS6 50933

# tworzenie klasy Pet
class Pet:
	# konstruktor
	def __init__(self, name, type):
		self.name = name
		self.type = type

	# metody
	def getName(self):
		return self.name

	def getType(self):
		return self.type

# tworzenie klasy Human, na podstawie której zostaną stworzone klasy PetOwner oraz Driver
class Human:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender

	def getName(self):
		return self.name

	def getSurname(self):
		return self.surname

	def getGender(self):
		return self.gender

# tworzenie klacy Vehicle, na podstawie której zostaną stworzone klasy Car oraz Motorcycle
class Vehicle:
	def __init__(self, producerName, modelName, yearOfProduction, mileage, color):
		self.producerName = producerName
		self.modelName = modelName
		self.yearOfProduction = yearOfProduction
		self.mileage = mileage
		self.color = color

	def getProducerName(self):
		return self.producerName

	def getModelName(self):
		return self.modelName

	def getYearOfProduction(self):
		return self.yearOfProduction

	def getMileage(self):
		return self.mileage

	def getColor(self):
		return self.color

# tworzenie klasy PetOwner, która dziedziczy z klasy Human
class PetOwner(Human):
	def __init__(self, name, surname, gender, pet):
		super().__init__(name, surname, gender)
		self.pet = pet

	def getPet(self):
		return self.pet

# tworzenie klasy Driver, która dziedziczy z klasy Human
class Driver(Human):
	def __init__(self, name, surname, gender, vehicle):
		super().__init__(name, surname, gender)

		self.vehicle = vehicle

	def getVehicle(self):
		return self.vehicle

# tworzenie klasy Car, która dziedziczy z klasy Vehicle
class Car(Vehicle):
	def __init__(self, producerName, modelName, yearOfProduction, mileage, color, engineCapacity, fuelType, numberOfSeats):
		super().__init__(producerName, modelName, yearOfProduction, mileage, color)

		self.engineCapacity = engineCapacity
		self.fuelType = fuelType
		self.numberOfSeats = numberOfSeats

	def getEngineCapacity(self):
		return self.engineCapacity

	def getFuelType(self):
		return self.fuelType

	def getNumberOfSeats(self):
		return self.numberOfSeats

# tworzenie klasy Motorcycle, która dziedziczy z klasy Vehicle.
# w obu tych klasach (Car i Motorcycle) występuje engineCapacity - pojemność silnika.
# w przypadku tylko tych dwóch klas możnaby było przenieść engineCapacity do Vehicle,
# jednak zdecydowałem się zostawić engineCapacity, ponieważ czysto teoretycznie
# ktoś mógłby chcieć stworzyć klasę np. Bicycle (rower), gdzie pojemność silnika nie występuje

class Motorcycle(Vehicle):
	def __init__(self, producerName, modelName, yearOfProduction, mileage, color, engineCapacity):
		super().__init__(producerName, modelName, yearOfProduction, mileage, color)

		self.engineCapacity = engineCapacity

	def getEngineCapacity(self):
		return self.engineCapacity

# tworzenie przykładowego człowieka
human1 = Human("Jan", "Kowalski", 1)

# tworzenie pojazdów które zostaną przypisane do Driver
car1 = Car("Audi", "R8", 2015, 152000, "biały", 5.2, "benzyna", 2)
car2 = Car("VW", "Passat", 2002, 255000, "srebrny", 1.9, "diesel", 5)

moto1 = Motorcycle("Kawasaki", "ZX", 2016, 181000, "czerwony", 2.5)
moto2 = Motorcycle("Zipp", "Toros", 2012, 130000, "czarny", 0.5)

# tworzenie zwierzaków które zostaną przypisane do PetOwner
pet1 = Pet("Koko", "kura")
pet2 = Pet("Nero", "pies")

# tworzenie PetOwner - właścicieli zwierzaków
petOwner1 = PetOwner("Łukasz", "Sztando", 1, pet1) # tworzymy Łukasza i przydzielamy mu kurę Koko pod opiekę
petOwner2 = PetOwner("Krzysztof", "Kononowicz", 1, pet2) # a Krzysiowi dajemy psa o imieniu Nero

# tworzenie kierowców
driver1 = Driver("Adam", "Nowak", 1, car1)
driver2 = Driver("Janusz", "Nosacz", 1, car2)
driver3 = Driver("Agata", "Kowalska", 0, moto1)
driver4 = Driver("Magda", "Szewc", 0, moto2)

# sprawdzanie działania
print("Fundamenty:")
print("human1.getName() :", human1.getName())
print("human1.getSurname() :", human1.getSurname())

print("\nTeraz sprawdzimy, czy działa dziedziczenie:")
print("Na obiekcie Car spróbujmy wywołać metodę z klasy Vehicle:")
print("car1.getProducerName() :", car1.getProducerName())
print("\nDziała jak należy. Wyświetlmy kilka przykładowych wartości:")
print("petOwner1.getName() :", petOwner1.getName())
print("petOwner1.getPet() :", petOwner1.getPet())
print("\ngetPet() zwraca obiekt, czyli wszystko w porządku. Spróbujmy coś z tego obiektu wyciągnąć:")
print("petOwner1.getPet().getName() :", petOwner1.getPet().getName())
print("\nWyciągnijmy pojazdy od kierowców:")
print("driver1.getVehicle() :", driver1.getVehicle())
print("driver3.getVehicle() :", driver3.getVehicle())
print("\nDziała przypisanie auta jak i motocyklu. Pobierzmy przykładowe wartości:")
print("driver2.getVehicle().getFuelType() :", driver2.getVehicle().getFuelType())
print("driver4.getVehicle().getMileage() :", driver3.getVehicle().getMileage())
