const main = async () => {
    const response = await fetch('/survey_questionnaire.json');
    const survey_questionnaire = await response.json();
    const survey = new Survey.Model(survey_questionnaire);
    $("#surveyContainer").Survey({
        model: survey,
        onComplete: (survey) => {
            const resultAsString = JSON.stringify(survey.data);
            console.log(resultAsString); // send Ajax request to your web server.
        }
    });
    Survey.StylesManager.applyTheme("bootstrap");
};

main()
    .then((text) => {
        console.log(text);
    })
    .catch(err => {
        console.log(err);
    });
