# N-Queens AI Algorithms

This project explores different artificial intelligence optimization techniques to solve the **N-Queens problem**.

Three algorithms were implemented and evaluated:

- Hill Climbing
- Simulated Annealing
- Genetic Algorithm

The algorithms were tested with large problem sizes:

N = 32, 64, 128

---

## Problem Description

The N-Queens problem consists of placing **N queens on an N×N chessboard** such that no two queens attack each other.

This means no two queens can share:

- the same row
- the same column
- the same diagonal

---

## Implemented Algorithms

### Hill Climbing

Local search algorithm that iteratively improves the current solution by selecting a neighbor with lower cost.

Characteristics:

- fast convergence
- may get stuck in local minima

---

### Simulated Annealing

Probabilistic technique inspired by thermodynamics that allows occasional worse moves to escape local minima.

Key parameters:

- temperature schedule
- cooling rate
- iteration limits

---

### Genetic Algorithm

Population-based evolutionary algorithm.

Key elements:

- chromosome representation of board states
- fitness function based on attacking queens
- crossover operator
- mutation operator
- selection strategy

---

## Experiments

Each algorithm was executed **5 times** for each problem size:

N = 32  
N = 64  
N = 128  

Metrics analyzed:

- execution time
- quality of the solution
- convergence behavior

---

## Example Representation

A solution is represented as a vector where the index represents the column and the value represents the row of a queen.

Example:

```
[4, 2, 7, 3, 6, 8, 5, 1]
```

---

## Technologies

- Python
- Numpy 
- Matplotlib  

---

## Project Structure

```
n-queens-ai-algorithms
│
├── hill_climbing.py
├── simulated_annealing.py
├── genetic_algorithm.py
├── experiments.py
├── report.pdf
└── README.md
```

---

## Results

The experiments showed different behaviors among the algorithms:

- Hill Climbing often converges quickly but may get stuck in local minima
- Simulated Annealing can escape local minima through probabilistic jumps
- Genetic Algorithms tend to explore the solution space more broadly

<img width="576" height="455" alt="nqueens_algorithm_comparison" src="https://github.com/user-attachments/assets/82f10821-bf0a-477b-a2d7-bcbe1d667195" />


---

## Educational Context

This project was developed as part of the Artificial Intelligence course at the Federal University of Mato Grosso (UFMT).

