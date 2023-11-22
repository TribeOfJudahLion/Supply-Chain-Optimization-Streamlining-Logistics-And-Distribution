import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from scipy.optimize import linprog
from pulp import LpProblem, LpMinimize, LpVariable, lpSum


# Load and preprocess data
def load_and_preprocess(file_path):
    data = pd.read_csv(file_path)
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    # Feature Engineering: Add any additional preprocessing steps here
    return data


# Exploratory Data Analysis (EDA)
def perform_eda(data):
    sns.pairplot(data, vars=['Ship ahead day count', 'Ship Late Day count', 'Unit quantity', 'Weight'])
    plt.show()


# Carrier Performance Scoring
def carrier_performance_scoring(data):
    carrier_performance = data.groupby('Carrier').agg({'Ship Late Day count': 'mean'}).reset_index()
    carrier_performance['Score'] = 1 / (1 + carrier_performance['Ship Late Day count'])
    return carrier_performance


# Optimization Model
def optimize_shipping(data, carrier_performance):
    problem = LpProblem("Minimize_Shipping_Delays", LpMinimize)

    # Variables: Assign shipments to carriers
    shipment_vars = LpVariable.dicts("Shipment", (data.index, carrier_performance['Carrier']), 0, 1, cat='Binary')

    # Objective Function: Minimize the weighted sum of shipping delays
    problem += lpSum(
        [shipment_vars[i][c] * carrier_performance.loc[carrier_performance['Carrier'] == c, 'Score'].values[0]
         for i in data.index for c in carrier_performance['Carrier']])

    # Constraints
    # Each shipment must be assigned to exactly one carrier
    for i in data.index:
        problem += lpSum([shipment_vars[i][c] for c in carrier_performance['Carrier']]) == 1

    # Solve
    problem.solve()
    return problem


# Analyze the results
def analyze_results(problem, data, carrier_performance):
    optimal_carriers = {}
    for v in problem.variables():
        if v.varValue > 0:
            # Properly unpack the variable name
            _, shipment, carrier = v.name.split('_', 2)
            optimal_carriers[int(shipment)] = carrier

    data['Optimal Carrier'] = data.index.map(optimal_carriers)

    # Professional visualization of the optimal carrier assignments
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Optimal Carrier', data=data, palette='viridis')
    plt.title('Optimal Carrier Assignments')
    plt.xlabel('Carrier')
    plt.ylabel('Number of Shipments')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Summary of Results
    print("\n--- Optimization Summary ---")
    print(f"Total number of shipments: {len(data)}")
    print(f"Number of unique carriers used: {data['Optimal Carrier'].nunique()}")
    print(f"Most frequently assigned carrier: {data['Optimal Carrier'].mode()[0]}")
    print("\nCarrier Assignment Breakdown:")
    print(data['Optimal Carrier'].value_counts())


# Main function
def main(file_path):
    data = load_and_preprocess(file_path)
    perform_eda(data)
    carrier_performance = carrier_performance_scoring(data)
    problem = optimize_shipping(data, carrier_performance)
    analyze_results(problem, data, carrier_performance)


if __name__ == "__main__":
    file_path = 'Supply chain logisitcs problem.csv'
    main(file_path)
