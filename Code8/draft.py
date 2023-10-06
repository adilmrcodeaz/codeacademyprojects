from forecast import predict_field


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



# data = {"Math_test":79.0,
#  "Programming_Concepts":75.0,
#  "Communication_skills_test":96.0,
#  "Working_per_day":7.0,
#  "Logic_test":10.0,
#  "Gender":"M",
#  "Introvert":"no",
#  "Age":28,
#  "Public_speaker":"yes",
#  "Interested Type of Books":"Prayer books",
#  "In a Realtionship?":"no"}

def predict(data):
    result = predict_field(data=data)
    
    prediction = {"result": result}
    
    return prediction


print(predict(data=data))