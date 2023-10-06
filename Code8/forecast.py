import pickle
import pandas as pd
import numpy as np
import json


with open('rf_model.pkl', 'rb') as model_file:
    rf_classifier = pickle.load(model_file)

with open('kmeans_model.pkl', 'rb') as model_file:
    kmeans = pickle.load(model_file)

with open('pca_model.pkl', 'rb') as model_file:
    pca = pickle.load(model_file)

with open('scaler.pkl', 'rb') as model_file:
    scaler = pickle.load(model_file)
# with open('pca_scaler.pkl', 'rb') as model_file:
#     pca_scaler = pickle.load(model_file)
    
with open("labels_weight.json", 'r') as json_file:
    label_data = json.load(json_file)
    
    
# person_array = np.array([79, 75, 96, 7.0, 10.0, "M", "no", 28, "yes", "Prayer books", "no"])

# columns = ['Math_test', 'Programming_Concepts_test', 'Communication_skills_test',
#        'Working_per_day', 'Logic_test', 'Gender', 'Introvert',
#        'Age', 'Public_speaker', 'Interested Type of Books',
#        'In a Realtionship?']

# df = pd.DataFrame([person_array], columns=columns)


data = {
    "Math_test": 79,
    "Programming_Concepts_test": 75,
    "Communication_skills_test": 96,
    "Working_per_day": 7.0,
    "Logic_test": 10.0,
    "Gender": "M",
    "Introvert": "no",
    "Age": 28,
    "Public_speaker": "yes",
    "Interested Type of Books": "Prayer books",
    "In a Realtionship?": "no"
}
# df = pd.DataFrame.from_dict(data, orient='index').T


# dummies = ['_Action and Adventure', '_Anthology', '_Art', '_Autobiographies',
#        '_Biographies', '_Childrens', '_Comics', '_Cookbooks', '_Diaries',
#        '_Dictionaries', '_Drama', '_Encyclopedias', '_Fantasy', '_Guide',
#        '_Health', '_History', '_Horror', '_Journals', '_Math', '_Mystery',
#        '_Poetry', '_Prayer books', '_Religion-Spirituality', '_Romance',
#        '_Satire', '_Science', '_Science fiction', '_Self help', '_Series',
#        '_Travel', '_Trilogy']

# df_for_pca = pd.DataFrame(columns=dummies)


# df_for_pca.loc[0] = 0
# values_to_set_to_1 = ["_Prayer books"]  
# df_for_pca.loc[0, values_to_set_to_1] = 1

# n_components = 3 
# pca_data = pca.transform(df_for_pca)
# pca_labels = pd.DataFrame(data=pca_data, columns=[f'PCA_{i+1}' for i in range(n_components)])
# df = pd.concat([df, pca_labels], axis=1)
# df.drop(columns=["Interested Type of Books"], inplace=True)



# df['Gender'] = df['Gender'].replace( ['F', 'M'], [0, 1])
# df['Introvert'] = df['Introvert'].replace( ['no', 'yes'], [0, 1])
# df['Public_speaker'] = df['Public_speaker'].replace( ['no', 'yes'], [0, 1])
# df['In a Realtionship?'] = df['In a Realtionship?'].replace( ['no', 'yes'], [0, 1])

# df['Math_test'] = pd.to_numeric(df['Math_test'], errors='coerce').astype(float)
# df['Programming_Concepts_test'] = pd.to_numeric(df['Programming_Concepts_test'], errors='coerce').astype(float)
# df['Communication_skills_test'] = pd.to_numeric(df['Communication_skills_test'], errors='coerce').astype(float)
# df['Working_per_day'] = pd.to_numeric(df['Working_per_day'], errors='coerce').astype(float)
# df['Logic_test'] = pd.to_numeric(df['Logic_test'], errors='coerce').astype(float)
# df['Age'] = pd.to_numeric(df['Age'], errors='coerce').astype(float)


# sub = df[["Math_test", "Programming_Concepts_test", "Communication_skills_test", "Working_per_day", "Logic_test"]]

# predicted_label = kmeans.predict(sub)

# df["labels"] = label_data[f"{predicted_label[0]}"]

# df[df.columns] = scaler.transform(df[df.columns])


def predict_field(data):
    df = pd.DataFrame.from_dict(data, orient='index').T
    
    
    dummies = ['_Action and Adventure', '_Anthology', '_Art', '_Autobiographies',
       '_Biographies', '_Childrens', '_Comics', '_Cookbooks', '_Diaries',
       '_Dictionaries', '_Drama', '_Encyclopedias', '_Fantasy', '_Guide',
       '_Health', '_History', '_Horror', '_Journals', '_Math', '_Mystery',
       '_Poetry', '_Prayer books', '_Religion-Spirituality', '_Romance',
       '_Satire', '_Science', '_Science fiction', '_Self help', '_Series',
       '_Travel', '_Trilogy']

    df_for_pca = pd.DataFrame(columns=dummies)


    df_for_pca.loc[0] = 0
    values_to_set_to_1 = ["_Prayer books"]  
    df_for_pca.loc[0, values_to_set_to_1] = 1

    n_components = 3 
    pca_data = pca.transform(df_for_pca)
    pca_labels = pd.DataFrame(data=pca_data, columns=[f'PCA_{i+1}' for i in range(n_components)])
    df = pd.concat([df, pca_labels], axis=1)
    df.drop(columns=["Interested Type of Books"], inplace=True)



    df['Gender'] = df['Gender'].replace( ['F', 'M'], [0, 1])
    df['Introvert'] = df['Introvert'].replace( ['no', 'yes'], [0, 1])
    df['Public_speaker'] = df['Public_speaker'].replace( ['no', 'yes'], [0, 1])
    df['In a Realtionship?'] = df['In a Realtionship?'].replace( ['no', 'yes'], [0, 1])

    df['Math_test'] = pd.to_numeric(df['Math_test'], errors='coerce').astype(float)
    df['Programming_Concepts_test'] = pd.to_numeric(df['Programming_Concepts_test'], errors='coerce').astype(float)
    df['Communication_skills_test'] = pd.to_numeric(df['Communication_skills_test'], errors='coerce').astype(float)
    df['Working_per_day'] = pd.to_numeric(df['Working_per_day'], errors='coerce').astype(float)
    df['Logic_test'] = pd.to_numeric(df['Logic_test'], errors='coerce').astype(float)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').astype(float)


    sub = df[["Math_test", "Programming_Concepts_test", "Communication_skills_test", "Working_per_day", "Logic_test"]]

    predicted_label = kmeans.predict(sub)

    df["labels"] = label_data[f"{predicted_label[0]}"]

    df[df.columns] = scaler.transform(df[df.columns])
        
        
    
    if rf_classifier.predict(df)[0] == 0:
        return "Analysis&Management"
    elif rf_classifier.predict(df)[0] == 1:
        return "Design"
    else:
        return "IT"
    
