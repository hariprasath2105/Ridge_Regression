# House Price Estimation using Ridge Regression

This project predicts **median house value** based on selected housing features using the **California Housing dataset**.  
It uses **Ridge Regression** for modeling and is deployed as an interactive **Gradio** web app.

---

## Project Structure

```
house-price-ridge/
│
├── model.py 
├── app.py 
├── model.pkl 
├── scaler.pkl 
└── README.md
```

---
## Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| scikit-learn   | Machine Learning     |
| Pandas         | Data manipulation    |
| NumPy          | Numeric operations   |
| Gradio         | Web-based UI         |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF6B81?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## How It Works
1. **Data Source**  
   The model uses the **California Housing dataset** provided by `sklearn.datasets`.

2. **Feature Selection**  
   The top 4 most correlated features with the target (`MedHouseVal`) are selected:
   - `MedInc` → Median income in the block (in $10,000s)  
   - `AveRooms` → Average number of rooms per household  
   - `AveOccup` → Average number of household members  
   - `HouseAge` → Median age of houses in the block

3. **Model**  
   A **Ridge Regression** model is trained on scaled features.

4. **Deployment**  
   The trained model is deployed using **Gradio** with a simple, styled interface.

---

## Installation

### 1. Install Dependencies
```bash
pip install flask scikit-learn pandas numpy
```

### 2. Train the Model (if not already)
```bash
python model.py
```

### 3. Run the Gradio App
```bash
python app.py
```

Then visit: [http://127.0.0.1:7860]

---

## Sample UI

**Input**:
```
| Feature                      | Example Value |
| ---------------------------- | ------------- |
| Median Income (MedInc)       | 5.0           |
| Average Rooms (AveRooms)     | 6.0           |
| Average Occupants (AveOccup) | 3.0           |
| House Age (HouseAge)         | 20            |
```
<img width="1292" height="477" alt="image" src="https://github.com/user-attachments/assets/8a9ded2c-f9c0-4465-83f8-a8f65bb713d1" />


**Output**:
```
Predicted Value (in $100k units): 2.35
Predicted Value (USD): $235,000
```
<img width="1278" height="452" alt="image" src="https://github.com/user-attachments/assets/3d4f71d9-43b5-4ba3-8a62-b7b49ab3df63" />

---
