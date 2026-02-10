import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.columns)

print(df.isnull().sum())
print(df.isna().sum())

df=df.dropna(subset=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',     
       'release_year', 'rating', 'duration', 'listed_in', 'description'])
print(df.isnull().sum())
print(df.isna().sum())

# Q-how many Movies vs TV Shows?
# bar chart 
print(df['type'].unique())
type_count=df['type'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(type_count.index,type_count.values,color=['skyblue','lightgreen'])
plt.title("number of movies vs tv shows on netflix")
plt.xlabel('TYPE')
plt.ylabel('COUNNT')
plt.tight_layout()
plt.savefig("netflix_barchart.png")
plt.show()

#Q-what is the percentage of each content rating
# pie chart
rating_counts=df['rating'].value_counts(normalize=True)*100
print(rating_counts)
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%')
plt.title('percentage of content rating')
plt.tight_layout()
plt.savefig("netflix_piechart.png")
plt.show()

##Q-what is the distribution of movies duration?
# histogram 
movie_df=df[df['type']=='Movie'].copy()
print(movie_df)

movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
print(movie_df['duration_int'])

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=20,color='orange',edgecolor='black')
plt.title('distribuion of movie duration')
plt.xlabel("durtion in minute")
plt.ylabel('number of movies')
plt.tight_layout()
plt.savefig('netflix_histogram.png')
plt.show()

# top 10 countries with the highest number of shows 
# barh :-
print(df.columns)
country_df=df['country'].value_counts().head(10)
print(country_df)

plt.figure(figsize=(8,6))
plt.barh(country_df.index,country_df.values,color=['red','orange'])
plt.ylabel("COUNTRY")
plt.xlabel("Number")
plt.title("TOP 10 COUNTRIES WITH THE HIGHEWS NUMBER :-")
plt.tight_layout()
plt.savefig('netflix_barh.png')
plt.show()

# relationship between realese year and number of show :-
# SCATTER PLOT

release_count=df['release_year'].value_counts().sort_index()
print(release_count)

plt.figure(figsize=(8,6))
plt.scatter(release_count.index,release_count.values,color="green",alpha=0.6)
plt.title("Release Year vs Number Of show")
plt.xlabel('Year')
plt.ylabel('NUmber Of Shows')
plt.tight_layout()
plt.grid()
plt.savefig("netflix_scatter.png")
plt.show()

# compare multiple plots together (movies vs tv show by year)
# subplots

subplot_df=df.groupby(['release_year','type']).size().unstack().fillna(0)
print(subplot_df)

fig,ax=plt.subplots(1,2,figsize=(12,5))

# first subplot : movies
ax[0].plot(subplot_df.index,subplot_df["Movie"],color='lightgreen')
ax[0].set_title("Movies released per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number Of movies")

# second subplot : TV 
ax[1].bar(subplot_df.index,subplot_df["TV Show"],color='skyblue')
ax[1].set_title("TV Show released per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number Of TV")

fig.suptitle("COMPARISON OF MOVIES VS TV SHOW BY YEAR")
plt.tight_layout()
plt.savefig('netflix_subplot.png')
plt.show()

# how was the realese number of changed over the year

release_vcount=df['release_year'].value_counts().sort_index()
# print(release_vcount)
plt.figure(figsize=(8,6))
plt.plot(release_vcount.index,release_vcount.values,color='red')
plt.xlabel('YEAR')
plt.ylabel("COUNTS")
plt.title("release number of change over the year")
plt.tight_layout()
plt.savefig('netflix_plot.png')
plt.show()