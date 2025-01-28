---

### **`paqb.py`**

```python
import random

# Define the server class
class Server:
    def __init__(self, name):
        self.name = name
        self.current_load = 0  # Current load in percentage (0-100%)
        self.predicted_load = 0  # Predicted load in percentage
        self.available_capacity = 100  # Max capacity is 100%
        self.fairness_penalty = 0  # Fairness penalty (historical overuse)

    def __repr__(self):
        return f"{self.name}: Current Load={self.current_load}%, Predicted Load={self.predicted_load}%, Fairness Penalty={self.fairness_penalty}%"

# Simulate prediction model (simple random-based for demo purposes)
def predict_server_load(server):
    # Predict future load based on current load and random variation
    server.predicted_load = min(100, server.current_load + random.randint(-10, 20))

# Calculate server "score" to determine where to assign task quanta
def calculate_server_score(server):
    if server.available_capacity == 0:
        return 0  # No capacity left
    return server.available_capacity / (server.predicted_load + server.current_load + server.fairness_penalty + 1)

# Distribute task quanta using Task Tetris logic
def distribute_task_quanta(servers, quanta):
    assignments = {server.name: 0 for server in servers}
    for _ in range(quanta):
        # Predict loads for all servers
        for server in servers:
            predict_server_load(server)
        
        # Calculate scores for all servers
        scores = {server: calculate_server_score(server) for server in servers}
        
        # Select the server with the highest score
        best_server = max(scores, key=scores.get)
        
        # Assign one quantum to the best server
        assignments[best_server.name] += 1
        best_server.current_load += 1  # Simulate increase in load
        best_server.available_capacity -= 1  # Reduce available capacity

        # Fairness penalty increases for overused servers
        best_server.fairness_penalty += 0.1

    return assignments

# Simulate a cluster of servers
def simulate_paqb():
    # Create 4 servers
    servers = [
        Server("Server 1"),
        Server("Server 2"),
        Server("Server 3"),
        Server("Server 4"),
    ]

    # Simulate initial loads for each server
    for server in servers:
        server.current_load = random.randint(10, 50)  # Random initial load
        server.fairness_penalty = random.uniform(0, 5)  # Random fairness penalty

    print("Initial Server States:")
    for server in servers:
        print(server)
    print()

    # Define an incoming task with 20 quanta
    task_quanta = 20
    print(f"Distributing {task_quanta} task quanta...\n")

    # Distribute the task quanta using Task Tetris
    assignments = distribute_task_quanta(servers, task_quanta)

    print("Final Server States:")
    for server in servers:
        print(server)
    print()

    print("Quantum Assignments:")
    for server_name, count in assignments.items():
        print(f"{server_name}: {count} quanta")

# Run the simulation
if __name__ == "__main__":
    simulate_paqb()
