class Child_budget:
    def __init__(self, stage):
        self.stage = stage
        self.expenses = {}

    def add_expenses(self, category, cost):
        category = str(category)
        self.expenses[category] = cost  

    def __str__(self):     
        return (f"{self.expenses.items()}, total:{self.expenses.values()}")
  

#wyprawka noworodka: 
newborn = {
    "crib" : 720,
    "mattress" : 270,
    "changing_table" : 170,
    "stroller_set" : 3500,
    "linen" : 85,
    "cloth_diapers" : 25,
    "blanket" : 75
    }
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
#infant = Child_budget("Niemowlę")  
#for keys, values in newborn.items():      
#    infant.add_expenses({keys},{values})
#for key, value in newborn.items():  
#     print(f"{key}: {value}")
#print(f"Total:{sum(newborn.values())}")        
     

def calc_newborn():
    infant = Child_budget("Newborn")  
    for keys, values in newborn.items():      
        infant.add_expenses({keys},{values})
    for key, value in newborn.items():  
        print(f"{key}: {value}")
    total_newborn = sum(newborn.values())
    return total_newborn

def calc_toddler():
    small_child = Child_budget("Toddler")  
    for keys, values in toddler.items():      
        small_child.add_expenses({keys},{values})
    for key, value in toddler.items():  
        print(f"{key}: {value}")
    total_toddler = sum(toddler.values())
    return total_toddler

def calc_older_toddler():
    small_child_2 = Child_budget("Toddler 4-6")  
    for keys, values in older_toddler.items():      
        small_child_2.add_expenses({keys},{values})
    for key, value in older_toddler.items():  
        print(f"{key}: {value}")
    total_older_toddler = sum(older_toddler.values())
    return total_older_toddler 

def calc_preschool():
    preschooler = Child_budget("Preschooler")  
    for keys, values in preschool.items():      
        preschooler.add_expenses({keys},{values})
    for key, value in preschool.items():  
        print(f"{key}: {value}")
    total_preschool = sum(preschool.values())
    return total_preschool 

def calc_child():
    a_child = Child_budget("Child")  
    for keys, values in child.items():      
        a_child.add_expenses({keys},{values})
    for key, value in child.items():  
        print(f"{key}: {value}")
    total_child = sum(child.values())
    return total_child

def calc_teen():
    teenager = Child_budget("Teenager")  
    for keys, values in teen.items():      
        teenager.add_expenses({keys},{values})
    for key, value in teen.items():  
        print(f"{key}: {value}")
    total_teen = sum(teen.values())
    return total_teen

stage_of_child = input("Do you currently have a child? Type yes|no ").lower()
private=input("Do you want to calculate cost of private schools? Type yes|no ").lower()
if stage_of_child=="yes":
    what_stage=int(input("Input age of a child in years: "))
    if what_stage<1:
        if private =="yes":
            del preschool["public_preschool"]
            del child["public_school"]
            del teen["public_school"]
            print(f'Total: {calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen()}')
        else:
            del preschool["private_preschool"]
            del child["private_school"]
            del teen["private_school"]
            print(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
    elif 0<what_stage<4:
        if private =="yes":
            del preschool["public_preschool"]
            del child["public_school"]
            del teen["public_school"]
            print(calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
        else:
            del preschool["private_preschool"]
            del child["private_school"]
            del teen["private_school"]
            print(calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
    elif 3<what_stage<7:
        if private =="yes":
            del preschool["public_preschool"]
            del child["public_school"]
            del teen["public_school"]
            print(calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
        else:
            del preschool["private_preschool"]
            del child["private_school"]
            del teen["private_school"]
            print(calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
    elif 6<what_stage<13:
        if private =="yes":
            del child["public_school"]
            del teen["public_school"]
            print(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
        else:
            del child["private_school"]
            del teen["private_school"]
            print(calc_child()+calc_teen())
    elif 12<what_stage<19:
        if private =="yes":
            del teen["public_school"]
            print(calc_teen())
        else:
            del teen["private_school"]
            print(calc_teen())               
elif stage_of_child == "no":
    if private =="yes":
            del preschool["public_preschool"]
            del child["public_school"]
            del teen["public_school"]
            print(f'Total: {calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen()}')
    else:
            del preschool["private_preschool"]
            del child["private_school"]
            del teen["private_school"]
            print(calc_newborn()+calc_toddler()+calc_older_toddler()+calc_preschool()+calc_child()+calc_teen())
           
        



    
