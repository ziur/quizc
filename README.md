# ComQuizz
ConQuizz is a console application that allows create and fill quizzes.
 
## Current features
 * Create quiz
   * Supports the next kind of questions:
     * Text
     * Numeric
     * Date
     * Pick one option (similar to a radio input element in HTML)
     * Pick many options
   * It is possible to mark a question as required, additionally the supported date format for answers is mm/dd/yyyy
 * Fill quiz
 
## Pending features to implement
### Validations
We want to support other kind of validations for question's answer, some of them are:
   * Text validations
     * Min length
     * Max length
     * Only uppercase text
   * Numeric validations
     * Min and max value

### Persistence
Currently all the information is stored on memory, that means quizzes are lost after finishing the application. 
Sometime ago, a member of the dev team did a reasearch about persisting information in a JSON file, you can check and run the json_persistence.py file which was the result of the research.
   * Given the json_persistence.py, try to reuse that code to implement the quiz persistance in a JSON file and also load a quiz given a JSON file.

### Menu
We don't like how the action menu (menu.py) is implemented, it has too much IFs; there should be a better way to implement that functionality. Sometime ago, Luis tried to refactor that code but it is incomplete, the menu2.py contains his work; take a look to it and try to finish the refactoring.

### Unit testing
There are some unit tests that will help you during the refactoring, it will be great if you can include more scenarios.

