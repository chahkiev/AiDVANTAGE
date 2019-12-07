import pandas as pd
import numpy as np

js = {'q0':"Мужской",'q1':1,'q2':"Нет",'q3':"Нет",'q4':"Не знаю",'q5':"Нет",'q6':"Нет, никогда не курил","q7":"Не курю","q8":"Нет","q9":"Нет","q10":"Вообще не проходил","q11":"Нет","q12":"Нет","q13":"Не помню","q14":"Нет","q15":"Нет","q16":"Нет","q17":"Нет","q18":"Нет","q19":"Нет","q20":"Нет","q21":"Нет","q22":"Нет","q23":"Нет","q24":"Не знаю","q25":"Нет","q26":"Нет","q27":"Нет","q28":"Нет","q29":"Нет","q30":"Нет","q31":"Нет","q32":"Да"} 

def json_to_arr(js):
    """
    Подготавливаем данные
    """
    df = pd.DataFrame(js, index=[0])

    col_name = "q0"
    df.loc[df[col_name] == "Мужской", col_name] = 1
    df.loc[df[col_name] == "Женский", col_name] = 0

    #q1 - возраст

    col_name = "q2"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q3"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Есть или были в прошлом", col_name] = 1
    df.loc[df[col_name] == "Да, есть или были в прошлом", col_name] = 2

    col_name = "q4"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Не знаю", col_name] = 2

    col_name = "q5"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q6"
    df.loc[df[col_name] == "Да, больше 10 лет", col_name] = 1
    df.loc[df[col_name] == "Да, меньше 10 лет", col_name] = 2
    df.loc[df[col_name] == "Нет, никогда не курил", col_name] = 0

    col_name = "q7"
    df.loc[df[col_name] == "Не курю", col_name] = 0
    df.loc[df[col_name] == "Больше пачки", col_name] = 1
    df.loc[df[col_name] == "Меньше пачки", col_name] = 2

    col_name = "q8"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да, с мокротой", col_name] = 1
    df.loc[df[col_name] == "Да, сухой", col_name] = 2
    df.loc[df[col_name] == "Да, бывает с примесью или прожилками крови", col_name] = 3

    col_name = "q9"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да", col_name] = 1

    col_name = "q10"
    df.loc[df[col_name] == "В этом году", col_name] = 1
    df.loc[df[col_name] == "Больше года назад", col_name] = 0
    df.loc[df[col_name] == "Вообще не проходил", col_name] = 2

    col_name = "q11"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да, иногда  в течение последнего месяца", col_name] = 1
    df.loc[df[col_name] == "Да, постоянно, дольше 1 месяца", col_name] = 2

    col_name = "q12"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Иногда, около месяца", col_name] = 1
    df.loc[df[col_name] == "Дольше 1 месяца, стабильно", col_name] = 2
    df.loc[df[col_name] == "Да, дольше 1 месяца, стабильно", col_name] = 2

    col_name = "q13"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Не помню", col_name] = 2

    col_name = "q14"
    df.loc[df[col_name] == "Да, иногда, около месяца", col_name] = 2
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да, дольше 1 месяца, стабильно", col_name] = 1

    col_name = "q15"
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Да, полипы толстой кишки", col_name] = 1
    df.loc[df[col_name] == "Да, геморрой", col_name] = 2
    df.loc[df[col_name] == "Да, трещину заднего прохода", col_name] = 3

    col_name = "q16"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q17"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q18"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q19"
    df.loc[df[col_name] == "Да, периодически", col_name] = 1
    df.loc[df[col_name] == "Постоянно, более 1 месяца", col_name] = 2
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q20"
    df.loc[df[col_name] == "Да, постоянно больше 1 месяца", col_name] = 1
    df.loc[df[col_name] == "Да, постоянно больше 1 месяца по вечерам или в ночное время", col_name] = 2
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q21"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q22"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q23"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q24"
    df.loc[df[col_name] == "Да, существенно", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0
    df.loc[df[col_name] == "Не знаю", col_name] = 2

    col_name = "q25"
    df.loc[df[col_name] == "Да", col_name] = 1
    df.loc[df[col_name] == "Нет", col_name] = 0

    col_name = "q26"
    df[col_name] = df[col_name].map({'Да': '1', 'Нет': '0'})

    col_name = "q27"
    df[col_name] = df[col_name].map({'Да, цвет изменился':'3','Да, кровоточат':'2', 'Да, увеличились и появились новые': '1', 'Нет': '0'})

    col_name = "q28"
    df[col_name] = df[col_name].map({'Да': '1', 'Нет': '0'})

    col_name = "q29"
    df[col_name] = df[col_name].map({'Да': '1', 'Нет': '0'})

    col_name = "q30"
    df[col_name] = df[col_name].map({'Да, выделения из соска кровянистого цвета': '4','Появление уплотнений, узлов': '3','Втяжение или уплощение соска': '2','Да': '1', 'Нет': '0'})

    col_name = "q31"
    df[col_name] = df[col_name].map({'Да': '1', 'Нет': '0'})

    col_name = "q32"
    df[col_name] = df[col_name].map({'Да': '1', 'Нет': '0'})
    
    df = df.to_numpy()
    
    return df

def predict_diagnosis(answers):
    """
    Предсказываем диагноз
    """
    import pickle
    model = pickle.load(open('./DiseaseDetector/ML/trained_model_ver2.sav', 'rb'))
    diagnosis = model.predict(answers.reshape(1, -1))
    
    res = ''
    
    if diagnosis == 0:
        res = 'Низкая вероятность онкологического заболевания'
    elif diagnosis == 1:
        res = 'Онкологическое заболевание возможно и требуется проведение дополнительных процедур'
    elif diagnosis == 2:
        res = 'Высокая вероятность онкологического заболевания'
    
    return res

# if __name__ == '__main__':
#     print(predict_diagnosis(json_to_arr(js)))