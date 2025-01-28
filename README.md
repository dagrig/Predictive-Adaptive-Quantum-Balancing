# Predictive Adaptive Quantum Balancing (PAQB)

This load balancing algorithm, officially known as **"Predictive Adaptive Quantum Balancing (PAQB)"**, divides incoming tasks into smaller "quanta" and dynamically assigns them to servers based on predicted loads, available capacity, and fairness. 

The algorithm is designed for flexibility and effective workload management, ensuring no server gets overloaded while maintaining fairness and balance over time.

---

## Features

- Predicts server loads for smarter task allocation.
- Dynamically assigns smaller units of work (quanta) to optimize resource usage.
- Ensures fairness by penalizing overused servers.
- Simulates server clustering and task distribution in Python.

---

## How It Works

1. **Server Initialization**: Each server starts with a random load and a fairness penalty based on past usage.
2. **Task Quantumization**: Incoming tasks are divided into smaller units (quanta) for finer control over distribution.
3. **Prediction and Scoring**: The algorithm predicts server loads and calculates a score for each server based on:
   - Available capacity.
   - Current and predicted loads.
   - A fairness penalty.
4. **Task Assignment**: Each quantum is assigned to the server with the highest score.
5. **Dynamic Rebalancing**: Server loads are updated dynamically during the task distribution process.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-tetris.git
   cd task-tetris
