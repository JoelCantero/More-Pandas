import pandas as pd

def answer_one():
    energy = pd.read_excel('Energy Indicators.xls', 
        header=None, 
        names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'], 
        skiprows=18,
        na_values='...', 
        nrows=227,
        usecols="C:F")\
        .set_index('Country')\
        .rename(index={
            "Australia1": "Australia",
            "China2": "China",
            "France6": "France",
            "Iran (Islamic Republic of)": "Iran",
            "Italy9": "Italy",
            "Japan10": "Japan",
            "Republic of Korea": "South Korea", 
            "Spain16": "Spain",
            "United States of America20": "United States",
            "United Kingdom of Great Britain and Northern Ireland19": "United Kingdom",
            "Bolivia (Plurinational State of)": "Bolivia"})
    energy['Energy Supply'] = energy['Energy Supply'].apply(lambda x: 1000000*x)
    GDP = pd.read_csv('world_bank.csv',
        header=0,
        skiprows=4)\
        .replace({
            "Korea, Rep.": "South Korea",
            "Iran, Islamic Rep.": "Iran",
            "Hong Kong SAR, China": "Hong Kong"
            })\
        .rename(columns={'Country Name': 'Country'})\
        .set_index('Country')
    ScimEn = pd.read_excel('scimagojr-3.xlsx').set_index('Country')
    
    return pd.concat([ScimEn.query("Rank <= 15")[['Rank','Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index']],
        energy,
        GDP[['2006', '2007', '2008', '2009', '2010', '2011', '2012','2013', '2014', '2015']]], axis=1, join='inner')

dataframe = answer_one()

def answer_two():
    return pd.concat([ScimEn[['Rank','Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index']],
        energy,
        GDP[['2006', '2007', '2008', '2009', '2010', '2011', '2012','2013', '2014', '2015']]], axis=1, join='inner').shape[0] - answer_one().shape[0]


# ## Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[ ]:


def answer_three():
    Top15 = answer_one()
    rows = ['2006', '2007', '2008', 
        '2009', '2010', '2011', 
        '2012','2013', '2014', '2015']
    return Top15[rows].mean(axis=1).rename('avgGDP').sort_values(ascending=False)


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[ ]:


def answer_four():
	top6country = answer_three().iloc[[5]].first_valid_index()
    return answer_one().loc[top6country]['2015'] - answer_one().loc[top6country]['2006']


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[ ]:


def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[ ]:


def answer_six():
    Top15 = answer_one()
    return (Top15.sort_values(by='% Renewable', ascending=False).iloc[0].name,
    	Top15.sort_values(by='% Renewable', ascending=False).iloc[0]['% Renewable'])


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[ ]:


def answer_seven():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[ ]:


def answer_eight():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[ ]:


def answer_nine():
    Top15 = answer_one()
    return "ANSWER"


# In[ ]:


def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[ ]:


#plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[ ]:


def answer_ten():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[ ]:


def answer_eleven():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[ ]:


def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[ ]:


def answer_thirteen():
    Top15 = answer_one()
    return "ANSWER"


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:


def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[ ]:


#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!

