# Introduction to Machine Learning

This repository contains resources and code for learning the basics of Machine Learning (ML) and Deep Learning (DL) using the Iris dataset. It includes Jupyter notebooks for hands-on practice and a Streamlit app for deploying a trained model.

## Contents

- `ml-intro.ipynb`: Introduction to Machine Learning concepts and hands-on exercises using the Iris dataset.
- `dl-intro.ipynb`: Introduction to Deep Learning concepts and practical implementation using TensorFlow.
- `iris.csv`: The Iris dataset used for training and testing models.
- `iris_model.pkl`: Pre-trained ML model for Iris species classification.
- `app.py`: Streamlit app for interactive Iris species prediction.

## Getting Started

### Prerequisites
- Python 3.8+
- Recommended: Use a virtual environment (`venv` or `conda`)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/shobhit1109/ml-intro-iris-ui.git
   cd ai-literacy-ML-DL
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # On Windows PowerShell
   # Or
   source .venv/bin/activate        # On macOS/Linux
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not present, install manually:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn tensorflow streamlit joblib
   ```

## Usage

### Jupyter Notebooks
Open `ml-intro.ipynb` or `dl-intro.ipynb` in Jupyter Notebook or VS Code and run the cells to learn and experiment with ML/DL concepts.

### Streamlit App
To run the Iris species prediction app:
```bash
streamlit run app.py
```
This will launch a web interface where you can input flower features and get predictions.

## Project Structure
- Data loading and preprocessing using pandas
- ML model training and evaluation using scikit-learn
- DL model implementation using TensorFlow
- Model deployment using Streamlit

## License
This project is for educational purposes.
