<br/>
<p align="center">
  <h3 align="center">Revolutionizing Logistics: Mastering the Art of Supply Chain Optimization</h3>

  <p align="center">
    Streamline, Optimize, Excel – Transforming Distribution Dynamics with Advanced Supply Chain Solutions
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario

In a large logistics company, managing the efficient distribution of goods is critical. The company operates globally and deals with thousands of shipments daily. Each shipment must be assigned to a carrier, but not all carriers are equally reliable. Some carriers are known to have frequent delays, which impacts customer satisfaction and overall efficiency.

The company has collected extensive data on its shipments, including the order date, the carrier used, the time it was shipped ahead or delayed, the unit quantity, and the weight of each shipment. This data is stored in a CSV file, 'Supply chain logistics problem.csv'. The challenge is to analyze this data and optimize the assignment of shipments to carriers to minimize delays.

### Solution Overview

The Python program provided addresses this challenge through several key steps:

#### 1. Data Loading and Preprocessing
- **Function**: `load_and_preprocess`
- **Purpose**: Load the dataset from a CSV file and preprocess it. This includes converting the 'Order Date' column to a datetime format and potentially other cleaning or feature engineering steps.

#### 2. Exploratory Data Analysis (EDA)
- **Function**: `perform_eda`
- **Purpose**: Perform initial exploratory analysis on the dataset to understand the distributions and relationships of key variables.

#### 3. Carrier Performance Scoring
- **Function**: `carrier_performance_scoring`
- **Purpose**: Assess each carrier's performance based on historical data, specifically focusing on their average shipping delay.

#### 4. Optimization Model
- **Function**: `optimize_shipping`
- **Purpose**: Create and solve a linear programming problem that aims to minimize shipping delays by optimally assigning shipments to carriers.

#### 5. Analysis of Results
- **Function**: `analyze_results`
- **Purpose**: Analyze and visualize the optimization results to understand the effectiveness of the assignments.

### Detailed Solution

1. **Data Preprocessing**: Prepares the dataset by converting dates and potentially applying other transformations for better analysis.

2. **EDA**: Visualizes relationships and distributions in the data to provide insights that inform the optimization model.

3. **Carrier Performance Scoring**: Each carrier is assigned a score inversely related to their average delay. Lower average delays result in higher scores, indicating better performance.

4. **Optimization Model**: 
   - Sets up a binary decision model where each shipment-carrier pair is a variable.
   - The objective function minimizes the weighted sum of shipping delays, using the carriers' scores as weights.
   - Constraints ensure that each shipment is assigned to exactly one carrier.
   - The problem is solved using a linear programming solver.

5. **Result Analysis**: 
   - The optimal carrier assignments for each shipment are extracted and added to the dataset.
   - These assignments are visualized using a count plot, showing the distribution of shipments across different carriers.
   - A summary is printed, including the total number of shipments, the number of unique carriers used, and a breakdown of carrier assignments.

### Execution and Outcome

On execution, the program processes the data, applies the optimization model, and outputs the results. The visualization and summary provide insights into how shipments can be optimally distributed among carriers to minimize delays, thereby enhancing the overall efficiency of the logistics operation. The company can use these insights to make data-driven decisions on carrier assignments, potentially improving customer satisfaction and operational efficiency.

This Python program is designed to optimize supply chain logistics, specifically focusing on assigning shipments to carriers in a way that minimizes delays. Here's a detailed breakdown of its logic and functionality:

### Imports
- **Pandas** for data manipulation and analysis.
- **NumPy** for numerical operations.
- **Matplotlib** and **Seaborn** for data visualization.
- **DateTime** for handling date and time objects.
- **SciPy**'s `linprog` and **PuLP** for linear programming and optimization.

### Functions

#### `load_and_preprocess(file_path)`
- **Purpose**: Loads and preprocesses the data from a CSV file.
- **Functionality**: Reads the CSV file into a Pandas DataFrame and converts the 'Order Date' column to a datetime format. Additional preprocessing steps (like handling missing values or feature engineering) can be added here.

#### `perform_eda(data)`
- **Purpose**: Performs exploratory data analysis (EDA) on the dataset.
- **Functionality**: Uses Seaborn's `pairplot` to create a grid of scatter plots. This helps in visually assessing relationships between the numeric columns 'Ship ahead day count', 'Ship Late Day count', 'Unit quantity', and 'Weight'.

#### `carrier_performance_scoring(data)`
- **Purpose**: Evaluates and scores carriers based on their performance.
- **Functionality**: Groups the data by 'Carrier' and calculates the mean 'Ship Late Day count' for each carrier. A score is then assigned to each carrier inversely proportional to their average delay, where a lower delay results in a higher score.

#### `optimize_shipping(data, carrier_performance)`
- **Purpose**: Optimizes the shipping assignment to carriers to minimize delays.
- **Functionality**: 
  - Sets up a linear programming problem using PuLP.
  - Creates binary variables for each shipment-carrier combination, indicating whether a shipment is assigned to a carrier.
  - The objective function aims to minimize the weighted sum of shipping delays, weighted by the inverse of the carrier score.
  - Constraints ensure that each shipment is assigned to exactly one carrier.
  - The problem is solved using PuLP's solver.

#### `analyze_results(problem, data, carrier_performance)`
- **Purpose**: Analyzes and visualizes the results of the optimization.
- **Functionality**: 
  - Extracts the optimal carrier assignment for each shipment from the solution.
  - Adds a column 'Optimal Carrier' to the dataset indicating the assigned carrier for each shipment.
  - Visualizes the distribution of shipments across carriers using a Seaborn count plot.
  - Prints a summary of the optimization results, including total shipments, number of unique carriers used, most frequently assigned carrier, and a breakdown of carrier assignments.

### Main Function: `main(file_path)`
- **Workflow**: 
  1. Loads and preprocesses the data.
  2. Performs EDA.
  3. Scores the carriers based on performance.
  4. Optimizes the shipment assignments.
  5. Analyzes and visualizes the optimization results.

### Execution
- When the script is run, the `main` function is called with the path to the CSV file containing the supply chain logistics data. The program goes through all the steps, from data loading to result analysis, and provides insights into the optimal way to assign shipments to carriers to minimize delays. 

This program is a comprehensive approach to supply chain optimization, combining data analysis, performance evaluation, and linear programming for decision-making. The visualization and summary provide a clear and actionable output for supply chain managers or analysts.

Let's break down the output for a comprehensive understanding:

### Solver Output
This part is generated by the CBC MILP (Mixed Integer Linear Programming) Solver, a component of the PuLP library. It details the process and performance of the optimization algorithm.

1. **Solver Version and Details**: Indicates the version of the CBC MILP Solver and its build date.
   
2. **Solver Execution**: Shows the command line used to execute the solver and the paths involved.

3. **Problem Reading**: Indicates that the problem named "MODEL" was read without errors, showing the number of rows (constraints), columns (variables), and elements (non-zero values in the matrix).

4. **Continuous Objective Value**: The objective value of the continuous (non-integer) relaxation of the problem, obtained very quickly (0.01 seconds). This value serves as a reference or a lower bound for the integer problem.

5. **Cut Information**: Details about the cuts (simplifications or refinements) applied to the problem. In this case, no cuts were made since there were no integer variables to process.

6. **Optimal Solution Found**: Indicates that an optimal solution was found for the problem.
   - **Objective Value**: The value of the objective function for the optimal solution, in this case, 8739.25.
   - **Enumerated Nodes and Total Iterations**: Reflects the number of nodes explored and iterations performed during the optimization. Both are zero, indicating a straightforward problem.
   - **Time Taken**: Shows both CPU and wall clock time spent on the optimization, which is very brief (0.07 seconds).

### FutureWarning
This warning is related to the use of Seaborn's `countplot`. It's advising that the way `palette` is used without `hue` is deprecated and suggesting an alternative method for future versions.

### Optimization Summary
This section summarizes the results of the optimization in a user-friendly format.

1. **Total Number of Shipments**: Indicates the total count of shipments in the dataset, 9215 in this case.

2. **Number of Unique Carriers Used**: Shows how many different carriers were selected in the optimal solution. Interestingly, only 1 unique carrier ('V444_0') was used for all shipments.

3. **Most Frequently Assigned Carrier**: Identifies the carrier most often assigned to shipments. Since only one carrier was used, it is 'V444_0'.

4. **Carrier Assignment Breakdown**: Provides a detailed count of how many shipments were assigned to each carrier. All 9215 shipments were assigned to 'V444_0'.

### Interpretation
- The solver efficiently found an optimal solution, as indicated by the quick resolution time and the lack of need for complex cuts or iterations.
- The result suggests that, under the given constraints and objective function, assigning all shipments to a single carrier ('V444_0') is the most optimal strategy. This could be due to various factors like cost, reliability, or carrier performance as encoded in the model.
- The warning about the `sns.countplot` usage indicates the need for code updates for compatibility with future versions of Seaborn.

### Considerations
- The result of using only one carrier for all shipments seems unusual and may prompt a review of the model's assumptions, constraints, and objective function. It might reflect an imbalance in the data or an oversimplification in the model.
- The solver's efficiency indicates that the problem wasn't complex for the algorithm, which could be due to the nature of the data or the simplicity of the model.
- Finally, the warning message is a reminder to keep the codebase updated with the latest best practices and library versions.

The output results consist of two visualizations generated from the supply chain optimization.

### Visualization 1: Optimal Carrier Assignments (Output_1.png)

The first visualization is a bar chart titled "Optimal Carrier Assignments." It depicts the distribution of shipments assigned to carriers after the optimization process. The X-axis represents the carriers, while the Y-axis represents the number of shipments.

Key Observations:
- There is only one carrier displayed, labeled as "V444_0".
- The bar representing this carrier reaches a count that looks to be approximately 9,200, suggesting that all shipments were assigned to this single carrier.

Interpretation:
- The result indicates that the optimization model has determined "V444_0" to be the most optimal carrier for all shipments, perhaps due to the lowest average delay or the highest score as per the model's evaluation criteria.
- The lack of variety in carrier selection could imply a potential issue with the optimization model, such as a lack of proper constraints that encourage diversity in carrier selection, or it could suggest that "V444_0" is significantly more efficient than other carriers.

### Visualization 2: Pair Plot of Key Shipping Metrics (Output_2.png)

The second visualization is a pair plot matrix, which shows the relationships between different shipping metrics: 'Ship ahead day count', 'Ship Late Day count', 'Unit quantity', and 'Weight'.

Key Observations:
- The histograms on the diagonal show the distribution of each variable. The 'Ship ahead day count' and 'Ship Late Day count' are heavily skewed towards lower values, suggesting that most shipments are not shipped much ahead or late. The 'Unit quantity' and 'Weight' show varied distributions with long tails, indicating some shipments are significantly larger or heavier than others.
- The scatter plots show the relationships between pairs of variables. There's a noticeable pattern in the 'Unit quantity' vs. 'Weight' scatter plot, suggesting a positive correlation between these two variables – as one would expect, heavier shipments tend to have a larger quantity of units.

Interpretation:
- The concentration of data points near zero for 'Ship ahead day count' and 'Ship Late Day count' suggests that the company is generally efficient with few early or late shipments.
- The positive correlation between 'Unit quantity' and 'Weight' is logical since larger quantities of goods would typically weigh more.
- The presence of outliers in the scatter plots could indicate exceptional cases where shipments are either unusually large or have been subject to significant delays.
- The lack of a discernible pattern in the scatter plots involving 'Ship ahead day count' and 'Ship Late Day count' with 'Unit quantity' and 'Weight' suggests that the amount or weight of the shipment doesn't necessarily predict shipping timeliness.

### Overall Summary

Together, these visualizations provide a comprehensive overview of the dataset and the results of the optimization model. While the optimization seems to have a clear outcome in terms of carrier selection, the pair plot reveals more nuanced relationships within the shipping data. The insights from these visualizations can inform business decisions related to logistics management, carrier negotiations, and process improvements to enhance supply chain efficiency.

## Built With

This project leverages a variety of powerful tools and libraries in Python for data processing, analysis, and optimization. Below is a comprehensive list of these technologies:

- **[Python](https://www.python.org/)** - Python is a high-level, interpreted programming language known for its ease of use and readability. It serves as the backbone of this project, providing a robust and flexible platform for data manipulation and analysis.

- **[Pandas](https://pandas.pydata.org/)** - Pandas is an open-source data analysis and manipulation tool, built on top of the Python programming language. It offers data structures and operations for manipulating numerical tables and time series, making it ideal for handling the dataset in this project.

- **[NumPy](https://numpy.org/)** - NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It enhances the performance of data operations in the project.

- **[Matplotlib](https://matplotlib.org/)** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is used in this project to plot various types of graphs for exploratory data analysis and result presentation.

- **[Seaborn](https://seaborn.pydata.org/)** - Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. This project uses Seaborn for advanced data visualization, particularly in exploratory data analysis.

- **[SciPy](https://www.scipy.org/)** - SciPy is an open-source Python library used for scientific and technical computing. It contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, among others. In this project, SciPy's optimization tools could be employed for certain types of analysis.

- **[PuLP](https://coin-or.github.io/pulp/)** - PuLP is an open-source linear programming (LP) package for Python. It enables users to describe mathematical programs and solve them. In this project, PuLP is used to set up and solve the optimization model for minimizing shipping delays.

- **[Datetime](https://docs.python.org/3/library/datetime.html)** - The datetime module supplies classes for manipulating dates and times. This project utilizes datetime to handle date-related operations in the dataset.

This blend of libraries and tools provides a comprehensive environment for tackling the complex tasks of data analysis and optimization in supply chain logistics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

1. **Python**: The project is written in Python. If you don't have Python installed, download and install it from [Python's official website](https://www.python.org/downloads/).

2. **Pip**: Pip is Python's package installer. It's used to install the libraries that the project depends on. It should come installed with Python, but if not, you can find installation instructions [here](https://pip.pypa.io/en/stable/installing/).

### Installation

1. **Clone the Repository**: To get started with this project, first clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
   Replace `your-username` and `your-repository` with your GitHub username and the repository name, respectively.

2. **Set Up a Virtual Environment** (Optional but recommended):
   - Navigate to the project directory:
     ```bash
     cd your-repository
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```bash
       source venv/bin/activate
       ```

3. **Install Required Libraries**:
   - Ensure you are in the project directory where the `requirements.txt` file is located.
   - Install the required libraries using pip:
     ```bash
     pip install pandas numpy matplotlib seaborn pulp
     ```

### Running the Application

1. **Prepare Your Dataset**: Ensure you have the dataset 'Supply chain logistics problem.csv' in your project directory or adjust the file path in the code accordingly.

2. **Execute the Program**:
   - Run the main program using Python:
     ```bash
     python main.py
     ```
   - Replace `main.py` with the name of the Python script if it's different.

3. **View the Results**: After running the program, you should see the outputs in the terminal, including the exploratory data analysis plots and the optimization summary.

### Testing

- To test the application, you can use different datasets that follow the same format or modify the parameters in the optimization model to see how the results vary.

---

This 'Getting Started' section aims to guide users through setting up and running the project, ensuring a smooth experience for developers and analysts looking to utilize or contribute to the project.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Supply-Chain-Optimization-Streamlining-Logistics-And-Distribution/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Supply-Chain-Optimization-Streamlining-Logistics-And-Distribution/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Supply-Chain-Optimization-Streamlining-Logistics-And-Distribution/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
