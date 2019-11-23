from django.http import HttpResponse
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render


def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'DiseaseDetector/index.html', )


def survey_questionnaire(request: HttpRequest) -> HttpResponse:
    survey_json = {
        "locale": "ru",
        "loadingHtml": "Загрузка",
        "pages": [
            {
                "name": "page1",
                "elements": [
                    {
                        "type": "text",
                        "name": "FIO",
                        "title": "ФИО",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле"
                    },
                    {
                        "type": "dropdown",
                        "name": "Doctor",
                        "title": "Выберите врача",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле",
                        "commentText": "Выберите врача",
                        "choices": [
                            {
                                "value": "1",
                                "text": "Врач 1"
                            },
                            {
                                "value": "2",
                                "text": "Врач 2"
                            },
                            {
                                "value": "3",
                                "text": "Врач 3"
                            }
                        ],
                        "otherText": "Выберите врача",
                        "optionsCaption": "Выберите врача",
                        "showOptionsCaption": False
                    },
                    {
                        "type": "dropdown",
                        "name": "Time",
                        "title": "Время приема",
                        "choices": [
                            {
                                "value": "1",
                                "text": "10:00"
                            },
                            {
                                "value": "2",
                                "text": "10:10"
                            },
                            {
                                "value": "3",
                                "text": "10:20"
                            }
                        ],
                        "showOptionsCaption": False
                    },
                    {
                        "type": "checkbox",
                        "name": "Personal info",
                        "title": "Согласие на обработку персональных данных",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле",
                        "choices": [
                            {
                                "value": "1",
                                "text": "Даю согласие на обработку персональных данных"
                            }
                        ]
                    }
                ],
                "title": "Личная информация",
                "navigationButtonsVisibility": "show"
            },
            {
                "name": "page2",
                "elements": [
                    {
                        "type": "radiogroup",
                        "name": "question1",
                        "title": "Вопрос 1",
                        "isRequired": True,
                        "choices": [
                            {
                                "value": "item1",
                                "text": "Ответ 1"
                            },
                            {
                                "value": "item2",
                                "text": "Ответ 2"
                            },
                            {
                                "value": "item3",
                                "text": "Ответ 3"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "page3",
                "elements": [
                    {
                        "type": "radiogroup",
                        "name": "question2",
                        "title": "Вопрос 2",
                        "isRequired": True,
                        "choices": [
                            {
                                "value": "item1",
                                "text": "Да"
                            },
                            {
                                "value": "item2",
                                "text": "Нет"
                            }
                        ]
                    }
                ]
            }
        ],
        "showQuestionNumbers": "off",
        "showProgressBar": "top",
        "goNextPageAutomatic": True,
        "startSurveyText": "Начать анкету",
        "pagePrevText": "Вернуться",
        "pageNextText": "Далее",
        "completeText": "Завершить"
    }

    return JsonResponse(survey_json)
