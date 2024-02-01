#python file for the functions used
#to use the data
import time,os;


#prints stat that is needed
def printstats(var,name,numofcities,cities):
  for i in range(numofcities):
    print("The "+name+" of "+cities[i]+" is "+str(var[i])+"\n");
    time.sleep(2);
  anyinput=input("Press any key to continue\n");
  os.system('clear');
  
    except ValueError:
      print("Invalid number");
      continue;

#function to determine what step of the framework each city
#should use, credits go to
#https://toronto.ctvnews.ca/here-s-how-ontario-s-colour-coded-covid-19-system-works-1.5172308
#for the framework
def framework(incidencesper100k,cities,numofcities):
  for i in range(numofcities):
    if incidencesper100k[i]<10:
      print(cities[i]+" should follow the prevent stage. This city must focus on education and spreading awareness about safety measures.\n");
    elif 10<=incidencesper100k[i]<25:
      print(cities[i]+ " should follow the protect stage. This city should put additional health measures in public high risk settings, like resturaunts.\n");
    elif 25<=incidencesper100k[i]<=40:
      print(cities[i]+ " should follow the restrict stage. This city should enhance restrictions to slow the spread of COVID 19.\n");
    elif incidencesper100k[i]>40:
      print(cities[i]+ " should follow the control stage. This city should implement severe restrictions to stifle the spread of COVID 19.\n");
    else:
      print("This is an error message, if you see this please contact sameerc4402152@gmail.ca about this error.");
      time.sleep(20);
      exit();
    time.sleep(2);
  anyinput=input("Press any key to continue\n");
  os.system('clear');
