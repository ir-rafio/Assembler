# Assembler
Assembler is a Python-based project that facilitates the creation of the best possible teams for programming competitions, such as ICPC (International Collegiate Programming Contest). It leverages machine learning techniques to analyze CodeForces user data and forms optimal teams based on various factors, including the users' *rating, number of problems solved, number of contests, problem difficulty, problem diversity, recent activity, and performance during contests*.

## Key Features
- **Integration with CodeForces API:** Assembler seamlessly connects with the CodeForces API to retrieve user data, including ratings, submissions, and contest history.
- **Skill-based Team Formation:** The tool utilizes a modified version of the *k-medoids clustering algorithm* to intelligently assemble teams that maximize collective skills and increase the chances of success in programming competitions.
- **Customizable Team Size:** Assembler supports custom team size configurations, allowing you to specify the number of members per team according to the competition requirements.
- **Iterative Optimization:** The algorithm employs an iterative optimization process to search for the best team combinations, ensuring the teams generated are as optimal as possible.
- **Data Preprocessing:** Assembler performs data preprocessing tasks, including feature scaling and normalization, to ensure fairness and comparability of user data during team formation.
- **Utilizes Powerful Libraries:** The project is built using popular Python libraries, including Numpy, Pandas, and Scikit-learn, to enable efficient data manipulation, analysis, and machine learning capabilities.

## Installation
1. Clone the repository:
```shell
git clone https://github.com/rafio-iut/Assembler.git
```
2. Install the required dependencies using pip:
```shell
pip install -r requirements.txt
```

## Usage
1. Add your CodeForces handles to the 'handles.txt' file, with each handle separated by a newline.
2. Open the 'main.py' file and set the values of the variables `teamCount` and `teamSize` according to your requirements. These variables determine the number of teams to be formed and the size of each team, respectively.
3. Run the 'main.py' script:
```shell
python main.py
```
4. The Assembler program will fetch the user data for the provided handles and generate the best possible teams for the programming competition based on the specified team count and team size.
5. The generated teams will be displayed on the console output.

## Requirements
- Python 3.x
- Numpy
- Pandas
- Scikit-learn

## Contributing
Contributions to Assembler are welcome! If you'd like to contribute, you can follow these steps:
1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure they are thoroughly tested.
4. Submit a pull request, clearly describing the changes and their purpose.

## Acknowlegdments
- The Assembler project is built upon the *CodeForces API* (https://codeforces.com/api) and utilizes its data for team formation.
- I express my gratitude to the developers and contributors of *Numpy, Pandas, and Scikit-learn* for their powerful and versatile libraries.