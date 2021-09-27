######### LOOPING THROUGH KEYS #########

#dictionary is an iterable (implements __iter__)

emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com",
    "Ted": "talk@gmail.com"
}

#k is a variable but k by convention for key
for k in emails:
    print(k)

#You can use the key to get the element 
#Not ideal.
#One reason being the key has to be hashed to get the value associated with it.
#(but will show better way in next section)
for k in emails:
    print("index", k, "is", emails[k])