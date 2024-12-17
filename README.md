# Cost of Raising a Child in Poland
#### Video: [YouTube Link] ()
#### Description:
This project helps calculate the cost of pregnancy, labour and raising a child to the age 18 years old in Poland. It allows the user to choose what form of medical care they prefer(national healthcare system(NFZ) or private). The same goes with choosing private or public schools. Cost of medical care and supplements are taken from live data and calculations of inflation goes through APIs to ensure relevance and accuracy.
### Files in the Project:
1. `project.py`: The main script containing core functionalities, including user interactions and cost calculations.
2. `tools.py`: A helper module with functions for processing data, scraping data, and storing.
3. `README.md`: Documentation for the project.
4. `requirements.txt`: A list of required Python libraries for installation (e.g., requests, pandas, etc.).

### Key features:
- **Dynamic budgeting**: Calculates the cost of pregnancy and labour based on user input. 
- **Live data integration**: Using cost that is up-to-date using APIs and scraping data.
- **Customizable scenarios**: Allows users to calculate costs for specific life stages, such as pregnancy, childbirth, or raising an already-born child.

### Design Choises:
During development we debated how to structure our project. We settled for splitting the functions in two files. The core is in the main file `project.py`. Everything that is helping main functions is stored in `tools.py` file. 
We choose not to implement APIs or scraping data with dictionaries which contains cost of child upbringing and hardcoded that data. However to ensure relevancy we implemented the APIs and made function that calculate the average inflation. Function called `get_url` using APIs is getting the yearly inflation for up to 10 years from the year before the actual year. It returns a list for the `get_inflation` function that calculates the average inflation for the 10 years period. By factoring in inflation, the project predicts the costs of raising a child over time with greater accuracy.

### Future Improvements:
- Add support for additional countries or regions.
- Include visualizations for cost breakdowns over time.
- Enhance the user interface for better accessibility and interactivity.
- Include more classes to avoid repetetive functions.