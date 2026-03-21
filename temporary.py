import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=pd.read_csv("adv.csv")

# part 1

# passing a dictionary to eliminate different anomolies in the same name of state
dict={
    "ODISHA":"ORISSA",
    "ANDAMAN AND NICOBAR ISLANDS":"ANDAMAN & NICOBAR ISLANDS",
    "JAMMU AND KASHMIR":"JAMMU & KASHMIR",
    "DADRA AND NAGAR HAVELI":"DADRA & NAGAR HAVELI",
    "WEST BANGAL":"WEST  BENGAL",
    "WESTBENGAL":"WEST  BENGAL",
    "WESTBENGAL":"WEST BANGAL",
    "DAMAN AND DIU":"DAMAN & DIU",
    "DADRA AND NAGAR HAVELI AND DAMAN AND DIU":" THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU",
    "PONDICHERRY ":"PUDUCHERRY ",
    "THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU":" THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU",
    
}

# removing some extra anomolies by manually

a["state"]=a["state"].str.upper()
a["state"]=a["state"].str.strip()
a['state']=a["state"].replace(" ","")
a['state']=a["state"].replace("WESTBENGAL","WEST BENGAL")
a["state"]=a["state"].replace("WEST  BENGAL","WEST BENGAL")
a['state']=a["state"].replace("WEST BANGAL","WEST BENGAL")
a["state"]=a["state"].replace(dict)
b=a.groupby("state")

print("STATE WISE AADHAR-ENROLMENT")
c=b.agg({"age_0_5":"sum","age_5_17":"sum","age_18_greater":"sum"})
print("\n\nThe states and Anomolies within the age of 0_5\n\n")
d=c.agg({"age_0_5":"sort_values"})
print(d)
print("\n\nThe states and Anomolies within the age of 5_17\n\n")
d1=c.agg({"age_5_17":"sort_values"})
print(d1)
print("\n\nThe states and Anomolies within the age of 18_greater\n\n")
d2=c.agg({"age_18_greater":"sort_values"})
print(d2)
print(" \n\n\nTHE THREE STATES WITH THE HIGHEST ANOMOLIES IN THE AADHAR ENROLLMENT ")
print("\n\nTop Three States With The Highest Anomolies In Age 0_5 \n\n",d.tail(3))
print("\n\nTop Three States With The Highest Anomolies In Age 5_17 \n\n",d1.tail(3))
print("\n\nTop Three States With The Highest Anomolies In Age 18_greater \n\n",d2.tail(3))

#graph plotting

a1=pd.Series([d["age_0_5"].sum(),d1["age_5_17"].sum(),d2["age_18_greater"].sum()])
plt.pie(a1,labels=["age_0_5","age_5_17","age_18_greater"],autopct="%0.1f%%",explode=[0,0,0.1])
plt.title("Percentage of Aadhar Anomolies In Different Age Groups")
plt.legend(loc="upper right")
plt.show()

# part 2

# passing a dictionary to eliminate different anomolies in the same name of district of jharkhand

print("\n\n Analysing The Border District Anomolies of Jharkhand\n\n")

jhar=a[a["state"]=="JHARKHAND"]
jhar["district"]=jhar["district"].str.upper()
jhar["district"]=jhar["district"].str.strip()
jhar['district']=jhar["district"].replace(" ","")
dict1={
    "BOKARO *":"BOKARO",
    "EAST SINGHBHUM":"EAST SINGHBUM",
    "GARHWA":"GARHWA *",
    "HAZARIBAG":"HAZARIBAGH",
    "KODARMA":"KODERMA",
    "PAKAUR":"PAKUR",
    "PALAMAU":"PALAMU",
    "SAHEBGANJ":"SAHIBGANJ",
}

# removing some extra anomolies by manually

jhar['district']=jhar["district"].replace(dict1)
jhar1=jhar.groupby("district")
jhar["pincode_2"]=jhar["pincode"].astype(str).str[:2].astype(int)
jhar2=jhar1.agg({"age_0_5":"sum","age_5_17":"sum","age_18_greater":"sum","pincode_2":"unique"})

#print(jhar2[["age_0_5","age_5_17","age_18_greater","pincode_2"]])

jhar3=jhar.groupby("pincode_2")

# summation of same two digits pincode_2 column


jhar4=jhar3.agg({"age_0_5":"sum","age_5_17":"sum","age_18_greater":"sum"})
jhar4.loc["85"]=jhar4.loc[[81,82]].sum()
jhar4["total"]=jhar4.sum(axis=1)
jhar4=jhar4.drop(81)
jhar4=jhar4.drop(82)
jhar4["total"]=jhar4["total"].astype(float)
jhar5=jhar4.rename(index={83:"Non border", "85":"Border"},columns={"pincode_2":"index"})
print(jhar5)

# graph plotting

plt.bar(jhar5.index.astype(str),jhar5["total"],color="yellow")
plt.xticks(np.arange(jhar5.shape[0]),["Non Border District","Border District"])
plt.ylabel("Total Anomolies")
plt.title("Anomolies In Border And Non Border District of Jharkhand")
plt.show()