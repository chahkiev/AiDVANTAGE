// var surveyJSON = { title: "Tell us, what technologies do you use?", pages: [
//     { name:"page1", questions: [ 
//         { type: "radiogroup", choices: [ "Yes", "No" ], isRequired: true, name: "frameworkUsing",title: "Do you use any front-end framework like Bootstrap?" },
//         { type: "checkbox", choices: ["Bootstrap","Foundation"], hasOther: true, isRequired: true, name: "framework", title: "What front-end framework do you use?", visibleIf: "{frameworkUsing} = 'Yes'" }
//      ]},
//     { name: "page2", questions: [
//       { type: "radiogroup", choices: ["Yes","No"],isRequired: true, name: "mvvmUsing", title: "Do you use any MVVM framework?" },
//       { type: "checkbox", choices: [ "AngularJS", "KnockoutJS", "React" ], hasOther: true, isRequired: true, name: "mvvm", title: "What MVVM framework do you use?", visibleIf: "{mvvmUsing} = 'Yes'" } ] },
//     { name: "page3",questions: [
//       { type: "comment", name: "about", title: "Please tell us about your main requirements for Survey library" } ] }
//    ]
//   };

var surveyJSON = {
    "pages": [
    {
    "name": "page1",
    "elements": [
    {
    "type": "text",
    "name": "question1",
    "title": "ФИО"
    },
    {
    "type": "dropdown",
    "name": "question2",
    "title": "Выберите врача",
    "defaultValue": "item1",
    "choices": [
    {
    "value": "item1",
    "text": "Врач 1"
    },
    {
    "value": "item2",
    "text": "Врач 2"
    },
    {
    "value": "item3",
    "text": "Врач 3"
    }
    ]
    },
    {
    "type": "dropdown",
    "name": "question3",
    "title": "Время приема",
    "choices": [
    {
    "value": "item1",
    "text": "10:00"
    },
    {
    "value": "item2",
    "text": "10:10"
    },
    {
    "value": "item3",
    "text": "10:20"
    }
    ]
    },
    {
    "type": "checkbox",
    "name": "question4",
    "title": "Согласие на обработку персональных данных",
    "choices": [
    {
    "value": "item1",
    "text": "Даю согласие на обработку персональных данных"
    }
    ]
    }
    ]
    }
    ]
    };

var survey = new Survey.Model(surveyJSON);
  $("#surveyContainer").Survey({
      model:survey,
      onComplete:sendDataToServer
  });

function sendDataToServer(survey) {
    var resultAsString = JSON.stringify(survey.data);
    alert(resultAsString); //send Ajax request to your web server.
  }