from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json
from forecast import predict_field
# Create a FastAPI app
app = FastAPI()



"""
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
    "Interested_Type_of_Books": "Prayer books",
    "In_a_Relationship": "no"
}
"""


# @app.get("/predict/")
# def predict(Math_test,Programming_Concepts_test, Communication_skills_test,Working_per_day,Logic_test, 
#             Gender, Introvert, Age, Public_speaker, Interested_Type_of_Books, In_a_Relationship):
#     data = {
#     "Math_test":    Math_test,
#     "Programming_Concepts_test": Programming_Concepts_test,
#     "Communication_skills_test": Communication_skills_test,
#     "Working_per_day": Working_per_day,
#     "Logic_test": Logic_test,
#     "Gender": Gender,
#     "Introvert": Introvert,
#     "Age": Age,
#     "Public_speaker": Public_speaker,
#     "Interested_Type_of_Books": Interested_Type_of_Books,
#     "In_a_Relationship": In_a_Relationship
# }
    
#     result = predict_field(data=data)
    
#     prediction = {"result": result}
    
#     return prediction

@app.get("/predict/")
def hey(Math_test, Programming_Concepts_test, Communication_skills_test, Working_per_day,
        Logic_test, Gender, Introvert, Age,Public_speaker,Interested_Type_of_Books,In_a_Relationship):
    data =  {
            "Math_test" : float(Math_test),
            "Programming_Concepts_test" : float(Programming_Concepts_test),
            "Communication_skills_test": float(Communication_skills_test),
            "Working_per_day": float(Working_per_day),
            "Logic_test": float(Logic_test),
            "Gender": Gender,
            "Introvert": Introvert,
            "Age": int(Age),
            "Public_speaker": Public_speaker,
            "Interested Type of Books": Interested_Type_of_Books,
            "In a Realtionship?": In_a_Relationship
            
    }

    result = predict_field(data=data)
    
    if result == "Analysis&Management":
        
        prediction = {"result": result,
                    "description": "Bu İxtisas tipik olaraq müxtəlif sahələrdə mürəkkəb problemləri həll etmək üçün təhlil və idarəetmə bacarıqlarını inkişaf etdirməyə həsr olunur. Bu, məlumat toplamaq və təhlil etmək, məlumatlı qərarlar vermək və sərvətləri və layihələri effektiv şəkildə idarə etmək deməkdir."
                    }
        
    elif result == "IT":
        prediction = {"result": result,
                    "description": "IT ixtisası əsasən texnologiya və kompüter sistemləri ilə bağlıdır. Bu, kompüter proqramları, hardware, şəbəkələr və rəqəmsal sistemlərin dizaynı, inkişafı, tətbiqi və baxımı daxil olmaqla kompüter texnologiyalarının idarə olunması və təkmilləşdirilməsi ilə bağlıdır. IT mütəxəssisləri texnologiya infrastrukturunu idarə etməkdə vacib rol oynayırlar."
                    }
        
    else: 
        prediction = {"result": result,
                    "description": "Dizayn ixtisası, gözəl və funksional məhsullar və ya təcrübələr yaratmağa yönlənmiş müxtəlif yaradıcı sahələri əhatə edir. Bu grafik dizayn, sənaye dizaynı, istifadəçi interfeys (UI) dizaynı və s. daxil edir. Dizaynerlər məhsulların və xidmətlərin görünüşü, interaktiv və fiziki aspektləri üzərində işləyirlər."
                    }
    return prediction






if __name__ == "__main__":
    

    uvicorn.run(app, host="0.0.0.0", port=8006, log_level="debug")


