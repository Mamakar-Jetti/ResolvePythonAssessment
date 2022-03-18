#Answered the questions to my best knowledge, and will be waiting for the oppurtunity to work in revolve.
#With in no time I can learn the best practices using in revolve and be a strong candidate.


#importing pandas library and reading the flights.csv dataset

import pandas as pd
df = pd.read_csv(r'C:/Users/mamakar/Downloads/data/flights.csv')


#Question 1: How many total number of days does the flights table cover?
#Solution : Function to know the total days in flights.csv

from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     
date1 = date(2013, 9, 30)
date2 = date(2019, 1, 1)
print(numOfDays(date1, date2), "days") 



#Question 2: How many departure cities (not airports) does the flights database cover?
#Solution : Function to identify no.of cities in flights table

# variable to hold the count
cnt = 0
  
# list to hold visited values
visited = []
  
# loop for counting the unique cities
for i in range(0, len(df['origin'])):
    
    if df['origin'][i] not in visited: 
        
        visited.append(df['origin'][i])
          
        cnt += 1
  
print("No.of.unique departure cities :",
      cnt)


