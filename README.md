# ComQuizz
ConQuizz is a console application that allows create and fill quizzes.
 
## Current features
 * Create quiz
   * Supports the next kind of questions:
     * Text
     * Date
     * Pick one option (similar to a radio input element in HTML)
   * Each question type has its own associated validations, for example:
     * The question type *TEXT* supports the validations *REQUIRED* and *MIN_LENGTH*
   * Given a created quiz, it is possible to fill the values for its questions   
 
## Pending features to implement
### Question types
Add support for a new question type called *NUMERIC*, and associate the next validations *REQUIRED* and *MIN* to it. 
Remember that you need to convert the values to int
### Validations
We want to support other kind of validations for question's answer, some of them are:
   * Text validations
     * Max length
     * Only uppercase text
     
Because there will be the new question type *NUMERIC* we want to add the support for a *MAX* validation  
### Enhance the _Show Quiz_ menu action
We want to enhance this action because currently the question information is not usefully, please enhance that logic to show the question title and answer.  

### Persistence
Currently all the information is stored on memory, that means quizzes are lost after finishing the application. 
Sometime ago, a member of the dev team did a research about persisting information in a JSON file, you can check and run the json_persistence.py file which was the result of the research.
   * Given the json_persistence.py, try to reuse that code to implement the quiz persistence in a JSON file and also load a quiz given a JSON file.
   Don't forget to include the respective action menu for this.

### Menu
We don't like how the action menu (menu.py) is implemented, it has too much IFs; there should be a better way to implement it, try to provide a better alternative that helps in the maintainability .

### Unit testing
There are some unit tests that will help you during the refactoring, it will be great if you can include more scenarios. Additionally, there are some test that are failing, there is something wrong in those fields, please fix them.

