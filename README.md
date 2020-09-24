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
 
## New Implemented features

### Question types
Added support for a new question type called *NUMERIC*, and associate the next validations *REQUIRED* and *MIN* to it. 

### Validations
   * Text validations
     * Max length
     * Only uppercase text
  * Numeric validations
     * Max

### Enhance the _Show Quiz_ menu action
Now shows title and answer more user friendly.  

### Menu
 menu.py refactored using class functions and a "switcher".

## Pending features to implement

### Persistence
Currently all the information is stored on memory, that means quizzes are lost after finishing the application. 
Sometime ago, a member of the dev team did a research about persisting information in a JSON file, you can check and run the json_persistence.py file which was the result of the research.
   * Given the json_persistence.py, try to reuse that code to implement the quiz persistence in a JSON file and also load a quiz given a JSON file.
   Don't forget to include the respective action menu for this.


### Unit testing
There are some unit tests that will help you during the refactoring, it will be great if you can include more scenarios. Additionally, there are some test that are failing, there is something wrong in those fields, please fix them.

