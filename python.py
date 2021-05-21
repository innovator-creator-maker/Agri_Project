#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt 



#reading the data set
df = pd.read_csv("Monthly_data_cmo.csv")



#reading ahmednagar's dataset
a = df.head(51)
#a



#removing some columns taken as anomalies
#syntax : drop(labels, axis, index, columns, level, inplace, errors)
anomaly_free = a.drop(["state_name","arrivals_in_qtl","date"], axis=1)
anomaly_free
#dropping "state_name","arrivals_in_qtl","date"



#removing some rows taken as anomalies
anomaly_free_2 = anomaly_free.drop([8,9,10,11,12,13,14,15,16,17,24,26,27,28,36,42,43], axis=0)
#anomaly_free_2



#dataset with the data of ahmednagar in both year 2015 and 2016
data15_16 = anomaly_free_2.sort_values('Year')
#data15_16



#dataset with only 2016 data
data16 = data15_16.loc[data15_16['Year'] == 2016]
#data16

#dataset with only 2015 data
data15 = data15_16.loc[data15_16['Year'] == 2015]
#data15




#comparing the data of 2016 and 2015 with common vegetables
#added the vegetables common in both the year
com_data = pd.merge(data15,data16, on="Commodity")
#com_data



#Getting the increase or decrease of minimum and maximum prices respectively
com_data['min_price_dif'] = com_data['min_price_y'] - com_data['min_price_x']
com_data['max_price_dif'] = com_data['max_price_y'] - com_data['max_price_x']
com_data['modal_price_dif'] = com_data['modal_price_y'] - com_data['modal_price_x']
#com_data



#Visualising the combined data set of 2015 and 2016



#Ploting the graph showing the increase in minimum 
#and maximum prices of common vegetables from 2015 to 2016

#this graph represnts by how much the minimum price of
#vegetables is varying from year 2015 to 2016

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(com_data.Commodity, com_data.min_price_dif)
plt.plot(com_data.Commodity, com_data.max_price_dif)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("increase or decrease",fontsize = 10)
plt.title("this graph represnts by how much the minimum and maximum price of vegetables is varying from year 2015 to 2016")
plt.legend(['min price','max price'],fontsize = 10)

#Ploting the graph showing the increase or decrease
#in modal prices of common vegetables from 2015 to 2016

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(com_data.Commodity, com_data.modal_price_dif)
plt.title("Ploting the graph showing by how much the increase or decrease in modal prices of common vegetables from 2015 to 2016",fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("increase or decrease",fontsize = 10)
plt.legend("modal_price",fontsize = 10)
plt.show()

#graph showing the minimum and maximum
#price of each commodity in both 2015 and 2016

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(com_data.Commodity,com_data.min_price_y,'o')
plt.plot(com_data.Commodity,com_data.min_price_x,'o')
plt.legend(['Min price in 2016','Min price in 2015'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize = 10)
plt.title("graph showing the minimum price of each commodity in both 2015 and 2016",fontsize = 10)
plt.show()

#graph showing the maximum price of each commodity in both 2015 and 2016

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(com_data.Commodity,com_data.max_price_y,'o')
plt.plot(com_data.Commodity,com_data.max_price_x,'o')
plt.legend(['max price in 2016','max price in 2015'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize = 10)
plt.title("graph showing the maximum price of each commodity in both 2015 and 2016",fontsize = 10)
plt.show()





#Visualising the dataset of only 2016





#printing out the dataset
data16

#ploting the graph showing the max price and min price of each commodity in 2016

plt.figure(figsize=(16,5))
plt.plot(data16.Commodity,data16.min_price)
plt.plot(data16.Commodity,data16.max_price)
plt.xticks(rotation=90)
plt.legend(['min price in 2016','max price in 2016'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize = 10)
plt.title("graph showing the max price and min price of each commodity in 2016",fontsize = 10)
plt.show()

#ploting the graph showing the modal price of each commodity in 2016

plt.figure(figsize=(16,5))
plt.plot(data16.Commodity,data16.modal_price)
plt.xticks(rotation=90)
plt.legend(['modal price'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize = 10)
plt.title("graph showing the modal price of each commodity in 2016",fontsize = 10)
plt.show()





#Visualising the dataset of only 2015





#printing the data set
data15

#ploting the graph showing the max price and min price of each commodity in 2016

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(data15.Commodity,data15.min_price)
plt.plot(data15.Commodity,data15.max_price)
plt.legend(['min price in 2015','max price in 2015'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize =10)
plt.title("graph showing the max price and min price of each commodity in 2015",fontsize = 10)
plt.show()

#ploting the graph showing the modal price of each commodity in 2015

#plt.figure(figsize=(13,8))
plt.xticks(rotation=90)
plt.plot(data15.Commodity,data15.modal_price)
plt.legend(['modal price'],fontsize = 10)
plt.xlabel("Name",fontsize = 10)
plt.ylabel("prices",fontsize = 10)
plt.title("graph showing the modal price of each commodity in 2015",fontsize = 10)
plt.show()







