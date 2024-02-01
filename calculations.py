import statistics,os;

#functions to calculate the other variables
def infection(numofcities,cases,population,infectionrate):
  for i in range (numofcities):
    infectionrate.append(cases[i]*1.0/population[i]);
  return infectionrate;

def casefatalityrate(numofcities,cases,deaths,cfr):
  for i in range(numofcities):
    cfr.append((deaths[i]/cases[i])*100.0);
  return cfr;

def positivityrate(numofcities,cases,population,posrate):
  for i in range(numofcities):
    posrate.append(float((cases[i]/population[i])*100.0));
  return posrate;

def incidenceper100k(numofcities,incidences,population,incidencesper100k):
  for i in range(numofcities):
    incidencesper100k.append((incidences[i]/population[i])*100000.0);
  return incidencesper100k;


#functions 
def meanmedianmode(numofcities,var,name):
  print("The mean of "+name+" is "+str(statistics.mean(var))+"\n");
  print("The median of "+name+" is "+str(statistics.median(var))+"\n");
  try:
    print("The mode of "+name+" is "+str(statistics.mode(var))+"\n")
  except StatisticsError:
    print("There is no mode for "+name);
  anyinput=input("Press any key to continue\n");
  os.system('clear');


def printstats(var,name,numofcities,cities):
  for i in range(numofcities):
    print("The "+name+" of "+cities[i]+" is "+str(var[i]+"\n"));
