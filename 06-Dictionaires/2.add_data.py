######### RETRIEVE DATA FROM DICTIONARY ##########
#Next up we gonna talk about retrieving data from a dictionary
#Unlike lists which goes through an itteration for data retreival process, 
#dictionaries are very usefull for fast data look ups and 
#fast data inserts. This is an example of 0(1) aka. constant time, on 
# Big O notation 


emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com" , 
    "tim": "g@example.com", 
}

print(list(emails))
print(sorted(emails))
#print(emails[0]) # NOPE!
print(emails["Caleb"])

#Since data is not nicely sequenced
#we may want to check before we try grabbing stuff

if("Caleb" in emails):
    print("Emailing", emails["Caleb"])

#This may seem bad because we first check to see if its in
#Then we do another line to get the value
#but this is different than a list where we iterate to find the element
#The key is goes through hash to calculate index. Either there or not
#This is O(1)

#You may still not like the casing and in that situation there is a method

print(emails.get("Ryan")) #Returns none if not found
print(emails.get("Ryan", "Not found")) #optional return arg if not found

