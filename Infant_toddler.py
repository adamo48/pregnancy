class Child_budget:
    def __init__(self, stage):
        self.stage = stage
        self.expenses = {}

    def add_expenses(self, category, cost):
        category = str(category)
        self.expenses[category] = cost   

    def total_expenses(self):
        return sum(self.expenses.values())

    def __str__(self):
        return f"{self.stage}: {self.expenses}. Total: {self.expenses}"
        
# infant((0-)wyprawka, pieluchy, mleko, butelki, smoczek, ubranka, zabawki, żłobek
# toddler(3-6) zabawki, jedzenie, żłobek/przedszkole, ubrania   
#child(7-12) hobby, zabawki, jedzenie, ubrania, szkolne wydatki
#teen(13-18) hobby, jedzenie, ubrania, szkolne wydatki

#infant = Child_budget("Niemowlę")        
#infant.add_expenses("Pieluchy", 100)
#infant.add_expenses("Mleko", 500)
#print(infant)

#wyposażenie noworodka: 
newborn = {"crib":720,
"materace":270,
"przewijak":170,
"wózek_fotelik":3500,
"pościel":85,
"pieluchy_tetrowe":25,
"kocyki":75}
#Niemowlę(0-12) 
toddler = {
    "nappies" : 2400,
    "bottle_feeding" : 5100,
    "cosmetics" : 680,
    "vaccination" : 3260,
    "clothes" : 1900,
    "chair" : 300,
    "toys" : 1700
}
#Małe dziecko(1-3)
older_toddler = {
    "food" : 4000,
    "bottle_feeding" : 1000,
    "nappies" : 1200,
    "vaccines" : 1400,
    "clothes" : 2200,
    "toys" : 2400, 
    "nursery" : 36000
}
#preschool(4-6)
preschool = {
    "public_preschool" : 7400,
    "private_preschool" : 36000,
    "clothes" : 7500,
    "food" : 4000 
}
#child(7-12)
child = {
    "public_school" : 16000,
    "private_school" : 135000,
    "additional_class" : 10000,
    "transportation" : 15000,
    "hobby" : 4500,
    "phone" : 3000,
    "computer" : 4500,
    "clothes" : 10000,
    "food" : 25000
}
#teen(13-18)
teen = {
    "public_school" : 27000,
    "private_school" : 145000,
    "additional_class" : 15000,
    "transportation" : 18000,
    "hobby" : 6000,
    "phone" : 3000,
    "computer" : 4500,
    "clothes" : 15000,
    "food" : 30000

}
infant = Child_budget("Niemowlę")  
for i in newborn:      
    infant.add_expenses(newborn.keys(), newborn.values())
print(infant)