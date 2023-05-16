
#Multi Country:
Import pandas as pd
Import matplotlib.pyplot as plt


#five year reference strings for visualizations
fiveyearperiods = ['1960', '1965', '1970',  '1975', '1980', '1985', '1990', '1995',
        '2000', '2005',  '2010', '2015', '2020']
fiveyearperiods2 = [ '1965', '1970',  '1975', '1980', '1985', '1990', '1995',
        '2000', '2005',  '2010', '2015', '2020']

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
