#imported to clear the screen
import os
#function to get the name of each city
#function to get the population of each city
def getcities(numofcities,cities):
  
  for i in range(numofcities):
    cities.append(input("Enter city name\n"));
  os.system('clear');
  return cities;

def getpop(numofcities, cities, population):
  i=0;
  while i<numofcities:
    
    try:
      pop=int(input("What is the population of "+cities[i]+"?\n"));
      
      if pop<=0:
        print("Must be greater than 0.");
        os.system('clear');
        continue;
      
      population.append(pop);
      i+=1;
      
    except ValueError:
      print("Invalid input.");
      os.system('clear');
      continue;
  os.system('clear');
  return population;
 
#function to get a statistic
#var1 is the variable you are looking to return
#var2 is used to compare it to var1
#to check if the user input was proper 
#AKA the incidences should not exceed tests

def getstat(numofcities, cities, var1,var2,name):
  i=0;
  while i<numofcities:
    try:
      inputstat=int(input("What is the amount of "+name+" for "+cities[i]+"?\n"));
      
      if inputstat>var2[i] or inputstat<=0:
        print("Invalid input, must be less than or equal to "+str(var2[i])+" and greater than 0\n");
        continue;  
     
      var1.append(inputstat);
      i+=1;
    except ValueError:
      print("Invalid input.\n");
      continue;
  os.system('clear');
  return var1;   


  
