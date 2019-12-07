const main = async () => {
    const response = await fetch('/survey_questionnaire.json');
    const survey_questionnaire = await response.json();
    const survey = new Survey.Model(survey_questionnaire);
    $("#surveyContainer").Survey({
        model: survey,
        onComplete: async (survey) => {
            await fetch('/survey_response/', {
                method: 'POST',
                body: JSON.stringify(survey.data), /* Данные получаются в формате: {"q0":"Мужской","q1":1,"q2":"Нет","q3":"Нет","q4":"Не знаю","q5":"Нет","q6":"Нет, никогда не курил","q7":"Не курю","q8":"Нет","q9":"Нет","q10":"Вообще не проходил","q11":"Нет","q12":"Нет","q13":"Не помню","q14":"Нет","q15":"Нет","q16":"Нет","q17":"Нет","q18":"Нет","q19":"Нет","q20":"Нет","q21":"Нет","q22":"Нет","q23":"Нет","q24":"Не знаю","q25":"Нет","q26":"Нет","q27":"Нет","q28":"Нет","q29":"Нет","q30":"Нет","q31":"Нет"} */
                headers: {'Content-Type': 'application/json'}
            });
        }
    });
    Survey.StylesManager.applyTheme("bootstrap");
};

// change_diagnos.onclick = function() {
//     alert('Клик!');
// };

main()
    .then((text) => {
        console.log(text);
    })
    .catch(err => {
        console.log(err);
    });

