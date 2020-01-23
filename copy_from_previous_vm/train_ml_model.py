import pandas as pd
import numpy as np

def read_dataset_csv():
    """
    Чтение .csv датасета
    """
    # Ужаляем столбец Unnme: 0
    df = pd.read_csv('post_dataframe.csv', index_col='Unnamed: 0')
    df_d = df['Диагноз'].values
    for i in range(len(df_d)):
        if df_d[i] == 2:
            df_d[i] = 1
    df['Диагноз'] = df_d[:]
    return df

def train_model():
    """
    Тренировка модели на прочитанном датасете
    """
    df_train = read_dataset_csv()[:]
    df_test = read_dataset_csv()[:]

    TRAIN_TEST_RATIO = 0.65
    train_number = round(df_train.shape[0] * TRAIN_TEST_RATIO)
    print(train_number)

    # train
    X_train = df_train.drop(['Диагноз'], axis=1).iloc[:train_number]
    y_train = df_train['Диагноз'].iloc[:train_number].values

    # test
    X_test = df_test.drop(['Диагноз'], axis=1).iloc[train_number:]
    y_test = df_test['Диагноз'].iloc[train_number:].values

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.naive_bayes import BernoulliNB
    
    # Random Forest будет эффективен в случае большого датасета, пока не рабочий
    # random_forest = RandomForestRegressor().fit(X_train, y_train)
    bernoulli = BernoulliNB().fit(X_train, y_train)

    print("\nNaive Baies:\nTrain: {}".format(bernoulli.score(X_train, y_train)))
    print("Test: {}".format(bernoulli.score(X_test, y_test)))
    import pickle
    pickle.dump(bernoulli, open('trained_model.sav', 'wb'))

def save_trained_model(model):
    """
    Сохранение натренированной модели
    """
    import pickle
    pickle.dump(model, open(trained_model, 'wb'))

# def predict_diagnosis(answers):
#     """
#     Предугадывание диагноза
#     """
#     import pickle
#     model = pickle.load(open('trained_model.sav', 'rb'))
#     diagnosis = model.predict(answers.reshape(1, -1))
#     return diagnosis


if __name__ == '__main__':
    train_model()