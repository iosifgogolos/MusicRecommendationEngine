PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i=0
rating = PlayListRatings[0]

while(rating > 6):
    print(rating)
    i=i+1
    rating = PlayListRatings[i]
    
print("It took ", i ,"repetitions to get out of the loop.")
