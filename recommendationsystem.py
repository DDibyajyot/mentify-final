import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["name"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("mentor_dataset.csv")
'
##Select Attributes

attributes = ['category','age,'rating']
for attribute in attributes:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['category'] +" "+row['interests']+" "+row["questions"]+" "+row["level"]
	except:
		print ("Error:", row	)

df["combined_features"] = df.apply(combine_features,axis=1)

##Create count matrix
              
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

##Find Cosine Similarity
cosine_sim = cosine_similarity(count_matrix) 
Mentee = "Parth"

##index of mentee from their name
mentee_index = get_index_from_name(mentee)

suggested_mentors =  list(enumerate(cosine_sim[mentee_index]))

## List of suggested mentors in descending order of similarity score
sorted_suggested_mentors = sorted(similar_movies,key=lambda x:x[1],reverse=True)

##Print names of best 5 mentor matches
i=0
for element in sorted_suggested_mentors:
		print(get_name_from_index(element[0])) 
		i=i+1
		if i>5:
			break
