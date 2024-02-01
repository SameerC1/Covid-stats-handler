from getvariables import getpop, getstat,getcities,getinput;
from calculations import infection, casefatalityrate,positivityrate,incidenceper100k,meanmedianmode;
from statfunctions import printstats,framework;

#variables to be collected
cities=[];
population=[];
cases=[];
tests=[];
incidences=[];
deaths=[];
#variables to be calculated
infectionrate=[];
cfr=[];
posrate=[];
incidencesper100k=[];
names=["cases","tests this week","incidences this week","fatalities","Infection rate","case fatality rate", "positivity rate this week", "incidences this week per 100k people"];
#do while loop to get amount of cities, between 1-5.
#if there is a value error, python will continue
#from beginning of the loop
print("Hello, welcome to the COVID-19 Response advisor\n")
while True:
  try:
    numofcities=int(input(("How many cities will there be? Max amount is 5.\n")));
    if numofcities<1 or numofcities>5:
      print("Enter a number between 1 and 5");
      continue;
    break;
  except ValueError:
    print("Enter an integer from 1-5")
    continue;

getcities(numofcities,cities)
getpop(numofcities,cities,population)

 #function used to collect variables
cases=getstat(numofcities, cities, cases,population,names[0]);
tests=getstat(numofcities, cities, tests,population,names[1]);
incidences=getstat(numofcities, cities, incidences,tests,names[2]);
deaths=getstat(numofcities, cities, deaths,cases,names[3]);

#functions to calculate other variables
infectionrate=infection(numofcities,cases,population,infectionrate);
cfr=casefatalityrate(numofcities,cases,deaths,cfr);
posrate=positivityrate(numofcities,cases,population,posrate);
incidencesper100k=incidenceper100k(numofcities,incidences,population,incidencesper100k);


#block of code to ask user what they want to see
#with the data
userinput=0;


#while loop for the last part of the project
while True:
  
  #asks user for statistic, then prints the 
  #statistic that is requested
  userinput=getinput(userinput);
  if userinput==1:
    userinput=int(input(("Which statistic would you like to see?\n1.Cases\n2.tests this week\n3.incidences this week\n4.deaths\n5.infection rate\n6.case fatality rate\n7.positivity rate\n8.incidences this week per 100,000 people.\n")))
    match userinput:
      case 1:
        printstats(cases,names[0],numofcities,cities)
      case 2:
        printstats(tests,names[1],numofcities,cities);
      case 3:
        printstats(incidences,names[2],numofcities,cities);
      case 4:
        printstats(deaths,names[3],numofcities,cities);
      case 5:
        printstats(infectionrate,names[4],numofcities,cities);
      case 6:
        printstats(cfr,names[5],numofcities,cities);
      case 7:
        printstats(posrate,names[6],numofcities,cities);
      case 8:     
        printstats(incidencesper100k,names[7],numofcities,cities);
    
  
  elif userinput==2:
    framework(incidencesper100k,cities,numofcities);
  
  elif userinput==3:
    userinput=int(input(("Which statistic would you like to see the mean, median, and mode of?\n1.Cases\n2.tests this week\n3.incidences this week\n4.deaths\n5.infection rate\n6.case fatality rate\n7.positivity rate\n8.incidences this week per 100,000 people.\n")))
    match userinput:
      case 1:
        meanmedianmode(numofcities,cases,names[0]);
      case 2:
        meanmedianmode(numofcities,tests,names[1]);
      case 3:
        meanmedianmode(numofcities,incidences,names[2]);
      case 4:
        meanmedianmode(deaths,cases,names[3]);
      case 5:
        meanmedianmode(infectionrate,cases,names[4]);
      case 6:
        meanmedianmode(cfr,cases,names[5]);
      case 7:
        meanmedianmode(posrate,cases,names[6]);
      case 8:     
        meanmedianmode(incidencesper100k,cases,names[7]);


  elif userinput>3 or userinput<1:
      print("Goodbye!");
      exit();
