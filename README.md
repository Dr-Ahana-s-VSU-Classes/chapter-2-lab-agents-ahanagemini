[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/g0VCZRk4)
# 🤖 Assignment: Reflex Vacuum Agent (Figure 2.8)

In this assignment, you will implement the **Reflex-Vacuum-Agent** algorithm described in the textbook (*Artificial Intelligence: A Modern Approach, 4th Edition*).

## 📖 Reference Material
You can view the logic for this agent here:
*   **[AIMA Figure 2.8 Pseudocode (PDF)](https://berkeley.edu)**
    *   *Note: Open the PDF and scroll to **page 7** to find the Reflex-Vacuum-Agent.*


## 🛠 Command Line Workflow

### 1. Clone your personal repository
```bash
git clone <your-personal-repo-url>
cd <your-repo-folder>
```

---

## 📋 Your Task
1. **Open** `agent.py`.
2. **Implement** the logic for `ReflexVacuumAgent(percept)` based on Figure 2.8:
   - If status is **Dirty**, return **'Suck'**.
   - If location is **A**, return **'Right'**.
   - If location is **B**, return **'Left'**.

---

### 2. Run the local tests
Run this script to verify your logic before submitting:
```bash
python3 test_agent.py
```

### 3. Submit your work
```bash
git add agent.py
git commit -m "Completed Figure 2.8"
git push origin main
```

---

## ✅ Submission Checklist
- [ ] `test_agent.py` prints "✅ All Figure 2.8 tests passed!"
- [ ] Your code is pushed to the **main** branch of your GitHub repository.
