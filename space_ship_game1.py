import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
fuel=500
hull=100
storm_data=[]
shield_data=[]
print("Welcome to the game of Safe landing of Hull@")
print("choose the shield power(1-100) \n\n")
try:
 for el in range(1,11):
     storm=np.random.randint(1,101)
    #print(storm)
     print("Level :",el)
     shield=int(input("Enter:"))
     storm_data.append(storm)
     shield_data.append(shield)
     if(storm>shield):
      hull_loss=storm-shield
      fuel_loss=(fuel-(2*hull_loss))
      print("Shield->",shield," Hull damages with:",hull_loss)
      hull-=hull_loss
      print("Fule remaining:",fuel_loss,"& Hull_loss:",hull,"\n\n")
     if(hull<=0):
      print("Your Hull is Fully Damaged!")
      print("--------Game over---------")
      break
     if(storm<shield):
      hull_gain=shield-storm
      fuel_gain=(fuel-(2*hull_gain))
      print("Shield->",shield," Hull Heals with:",hull_gain)
      hull+=hull_gain
      print("Fuel remaining:",fuel_gain,"& Hull_gain:",hull,"\n\n")
      if(el==10 & hull>0):
       break

 print("Hull Successfully landed@")
 dict ={
   "shield data":shield_data,
   "storm data":storm_data
 }
 flight_data=pd.DataFrame(dict)
 flight_data["round"]=np.arange(1,el+1,1)
 plt.figure(figsize=(15,15))
 plt.title("Trajectory of Shiled and Storm")
 plt.style.use("dark_background")
 sns.lineplot(data=flight_data,x="round",y="shield data",color="red",markers="o",label="shield intensity")
 sns.lineplot(data=flight_data,x="round",y="storm data",color="green",markers="s",label="storm intensity")
 plt.fill_between(
   flight_data["round"],
   flight_data["shield data"],
   flight_data["storm data"],
   where=(flight_data["shield data"]<flight_data["storm data"]),
   interpolate=True,
   color="red",
   alpha=0.2,
   label="danger zone"
 )
 plt.fill_between(
   flight_data["round"],
   flight_data["shield data"],
   flight_data["storm data"],
   where=(flight_data["shield data"]>flight_data["storm data"]),
   interpolate=True,
   color="green",
   alpha=0.2,
   label="safe zone"
 )
 plt.legend()
 plt.show()
except ValueError:
  print("\nPlease enter numbers only!")
