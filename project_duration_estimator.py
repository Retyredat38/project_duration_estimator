import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def triangular_sample(min_val, mode, max_val, size=1):
    """Generate samples from a triangular distribution."""
    return np.random.triangular(min_val, mode, max_val, size)

def simulate_project_duration(tasks_df, num_simulations=10000):
    total_durations = []
    for _ in range(num_simulations):
        total = 0
        for _, row in tasks_df.iterrows():
            # Sample duration for each task using the triangular distribution
            duration = triangular_sample(row['Min'], row['MostLikely'], row['Max'], size=1)[0]
            total += duration
        total_durations.append(total)
    return np.array(total_durations)

def plot_simulation_results(durations, target_duration=None):
    plt.figure(figsize=(10,6))
    plt.hist(durations, bins=50, alpha=0.75, color='skyblue', edgecolor='black')
    plt.title("Project Completion Time Distribution")
    plt.xlabel("Total Duration (days)")
    plt.ylabel("Frequency")
    
    if target_duration:
        plt.axvline(target_duration, color='red', linestyle='--', label=f"Target: {target_duration} days")
        plt.legend()
    
    plt.show()

def main():
    # Load tasks data from CSV
    tasks_df = pd.read_csv(sample_tasks.csv)
    print("Task Data:")
    print(tasks_df)
    
    # Run Monte Carlo simulation
    durations = simulate_project_duration(tasks_df, num_simulations=10000)
    mean_duration = np.mean(durations)
    median_duration = np.median(durations)
    
    print(f"\nMean Project Duration: {mean_duration:.2f} days")
    print(f"Median Project Duration: {median_duration:.2f} days")
    
    # Plot the results (set a target duration if desired, e.g., 20 days)
    plot_simulation_results(durations, target_duration=20)
    
    # Optionally, save the simulation results to a CSV
    results_df = pd.DataFrame(durations, columns=["Total Duration"])
    results_df.to_csv("simulation_results.csv", index=False)
    print("Simulation results saved to 'simulation_results.csv'.")

if __name__ == "__main__":
    main()
