import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('worldbank_pop.csv', index_col = "Series Name")

#cleaning data
data = data.transpose()
data.drop('Series Code', inplace = True)
data.drop('Country Code', inplace = True)
data.drop('Country Name', inplace = True)

#cleaning years
new_index = []
for year in data.index:
    new_index.append(year[:4])
data.index = new_index

#five year reference strings for visualizations
fiveyearperiods = ['1960', '1965', '1970',  '1975', '1980', '1985', '1990', '1995',
        '2000', '2005',  '2010', '2015', '2020']
fiveyearperiods2 = [ '1965', '1970',  '1975', '1980', '1985', '1990', '1995',
        '2000', '2005',  '2010', '2015', '2020']

#urban population graphic

#drop null values (only one)
urbanpop = data['Urban_population'].drop('2022') 

#plot:
plt.plot(data.drop('2022').index, urbanpop.astype(int), color = '#2E22BA')
plt.title("Urban Population", pad = 12.0, fontsize = 20)
plt.ylabel("Population (millions)",labelpad = 12.0)
plt.xlabel("Year", labelpad = 12.0)
plt.xticks(rotation = 45, ticks = fiveyearperiods )
plt.yticks(ticks = [100000000,200000000,300000000,400000000,500000000,600000000,700000000,800000000], labels = ['100','200','300','400','500','600','700','800'])

#save image as png
plt.savefig('UrbanPop.png', dpi = 600, facecolor = 'white')
plt.figure(clear = True)
#population growth graphic:

#drop null 
urbanpopgrowth = data['Urban_pop_pctgrowth'].drop('2022').drop('1960')

#plot:
plt.plot(data.drop('2022').drop('1960').index, urbanpopgrowth, color = '#2E22BA')
plt.title("Urban Population Growth", pad = 12.0, fontsize = 20)
plt.ylabel("Percent Change",labelpad = 12.0)
plt.xlabel("Year", labelpad = 12.0)
plt.xticks(rotation = 45, ticks = fiveyearperiods2 )
plt.savefig('UrbanPopGrowth.png', dpi = 600, facecolor = 'white')

plt.figure(clear = True)
#Urban pop percentage:
urbanpoppct = data['Urban_population_pct'].drop('2022')
#plot:
plt.plot(data.drop('2022').index, urbanpoppct.astype(float), color = '#2E22BA')
plt.title("Urbanization Level ", pad = 12.0, fontsize = 20)
plt.ylabel("Percentage of population residing in urban areas",labelpad = 12.0)
plt.xlabel("Year", labelpad = 12.0)
plt.xticks(rotation = 45, ticks = fiveyearperiods )
plt.savefig('UrbanPopPct.png', dpi = 600, facecolor = 'white')

plt.figure(clear = True)

#importing data as a pandas dataframe
worlddata = pd.read_csv('worldpop.csv',index_col = "Country Name")
worlddata = worlddata.transpose() #I want observations to be years

#Getting a list of country names from the original file
worlddata_raw = pd.read_csv('worldpop.csv')
Countries = worlddata_raw['Country Name']

#cleaning unnecessary rows
worlddata.drop('Series Name', inplace = True)
worlddata.drop('Country Code', inplace = True)
worlddata.drop('Series Code', inplace = True)

#formatting year index
new_worldindex = []
for year in worlddata.index:
    new_worldindex.append(year[:4])
worlddata.index = new_worldindex

#Creating Visualization of world data
plt.plot(worlddata.index, worlddata)
plt.figlegend(Countries, loc = (.18,.30))
plt.title("Urbanization Level by Country", pad = 12.0, fontsize = 20)
plt.ylabel("Percentage of population residing in urban areas", labelpad = 12.0)
plt.xlabel("Year", labelpad = 12.0)
plt.xticks(rotation = 45, ticks = fiveyearperiods )

#saving as a png
plt.savefig('WorldUrbanPop.png', dpi = 600, facecolor = 'white')


