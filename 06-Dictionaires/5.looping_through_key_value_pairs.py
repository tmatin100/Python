######### LOOPING THROUGH KEY-VALUE PAIRS #########
#dictionary is an iterable (implements __iter__)

emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com",
    "Ted": "talk@gmail.com"
}

#In the prev section we used the index with [].
#Although it works, you can do this:

for k, elem in emails.items():
    print(k, elem)

#Each iteration k will be the key and elem will be the item found at this key.

#As an example of what a hashtable can be used for, you can keep track of occurances of data:

conjunctions = {"but": 0, "or": 0, "so": 0, "and": 0, "yet": 0, "for": 0, "nor": 0} #fanboys

completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side"""

#use the .split() function to create a list name words
words = completely_original_poem.split()

print(words)

#count how many times each word in the conjuctions dictionary occurs in the words list.

for word in words:
    if word in conjunctions:
        conjunctions[word] += 1
print(conjunctions)

#use .lower string method to convert everthing to lower case 
for word in words:
    if str.lower(word) in conjunctions:
        conjunctions[str.lower(word)] += 1
print(conjunctions)


#This could easily be wrapped in a function to take a msg and words to look for, returning a dict
#concept can be used to analyze documents to quantify how vulgar they are, search for phrases, etc
#dictionaries can be used to keep track of values that are hard to calculate (memoization)