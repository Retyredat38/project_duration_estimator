Project Duration Estimator and Risk Analyzer

This tool uses Monte Carlo simulation to estimate overall project duration and assess delay risks. It reads task data from a CSV file—where each task has a minimum, most likely, and maximum duration—and then simulates many scenarios to generate a probability distribution of the total project duration.

Overview

In this prototype, you provide a CSV file with your project tasks. The tool:
- Samples task durations using a triangular distribution.
- Runs a Monte Carlo simulation (default 10,000 iterations).
- Outputs key metrics such as the mean and median project duration.
- Visualizes the distribution of completion times in a histogram.

The sample output from our test run was:
- **Mean Project Duration:** ~84.03 days
- **Median Project Duration:** ~83.93 days
- (See Figure 1 for the histogram)

Sample CSV Format

Place your CSV file in the `data/` folder. A sample CSV (`sample_tasks.csv`) should have the following structure:

```csv
Task,Min,MostLikely,Max
Define project scope,3,5,7
Gather requirements,4,6,9
Design system architecture,7,10,14
Develop prototypes,10,15,20
Test prototypes,5,8,12
Refine design,3,5,7
Implement final solution,15,20,30
Conduct user training,2,3,4
Deploy solution,1,2,3
Post-deployment support,5,7,10
