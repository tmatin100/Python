######### ADD DATA TO DICTIONARY #########

emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com" , 
    "tim": "g@example.com", 
}

#How to add data (3 ways here):

#indexing
emails["josh"] = "josh@j.com"
print(emails)

#update function
emails.update( {"josh": "evennewer@email.com"})
print(emails)

#Weird variation
emails.update(josh = "new@email.com")
print(emails)

#Key must be hashable
emails[5] = "test"
emails[(1, 2)] = "yep"
#emails[[5, 3]] = "nope" #list is not hashable (mainly becuase it's mutable)

print(emails)




