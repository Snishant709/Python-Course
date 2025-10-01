import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#load the source data
source=pd.read_excel("/workspaces/Python-Course/numpy/project/indian_employee_data.xlsx")
df=pd.DataFrame(source)
print(df)

#get the unique values from the column City
print("Unique records in City column is " ,df['City'].unique())


#get the counts for all the values in city but storing only 5 from last that is lowest to highest
#city_values=df['City'].value_counts().tail(5)
city_values=df['City'].value_counts()
print("Unique records in City column is " ,city_values)


#plotting the bar chart
x_value=city_values.index #we are getting the name of city here 
y_value=city_values.values #we are getting the counts of that city
print("'X' axis values ",x_value,"\n","'Y' axis values \n",y_value)
#we will now 1st increase size of the figure
plt.figure(figsize=(25,8))#giving height , width
#rotate the label
plt.xticks(rotation=90,fontsize=15)
plt.yticks(rotation=45,ha="right",fontsize=15)

plt.bar(x_value,y_value,width=0.3,color='skyblue', edgecolor='black')#by default width is 1 
#but the ploting is not perfect the labels are overlapping so below things we can do
# allign the labels vertically,decrease the size of font ,increase the size of visual
plt.xlabel("City",fontsize=20)
plt.ylabel("Counts",fontsize=20)
plt.tight_layout()  # prevents label cutoff
plt.savefig("bar.png")


#by using the sb library we can draw the bar chart more easily then matplotlib
sb.countplot(x='City',data=df,order=df["City"].value_counts().index,color="skyblue")
plt.savefig("bar_using_seaborn.png")
#but it will take all the properties of the plt which is defined above

# so in simple word the seaborn library helps to reduce the line of code to draw any visual
# as compared to the library matplotlib 