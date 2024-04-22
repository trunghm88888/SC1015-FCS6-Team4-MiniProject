# SC1015-FCS6-Team4
# Heart Failure Classification Project

## Overview
This repository contains code and resources for a machine learning project aimed at predicting heart failure based on clinical data. The goal of the project is to build and deploy a classification model that can accurately predict the likelihood of heart failure in patients.

## Dataset
The dataset used for this project is the [Heart Failure Prediction Dataset](https://www.kaggle.com/fedesoriano/heart-failure-prediction) by [Federico Soriano](https://www.kaggle.com/fedesoriano) available on Kaggle. It contains 12 clinical features along with a binary target variable indicating whether the patient died or not.

## Project Structure
- `data/`: Directory to store the dataset.
- `EDA.ipynb`: Notebook for exploratory data analysis.
- `ml_notebooks/`: Directory containing notebooks for machine learning tasks.
  - `helper_functions.py`: Python file containing helper functions.
  - `setup.ipynb`: Notebook for initial project setup.
  - `knn.ipynb`: Notebook for K-Nearest Neighbors model.
  - `svm.ipynb`: Notebook for Support Vector Machine model.
  - `tree_based.ipynb`: Notebook for tree-based models.
- `README.md`: Project overview, instructions, and documentation.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/trunghm88888/SC1015-FCS6-Team4-MiniProject.git
    cd SC1015-FCS6-Team4-MiniProject
    ```

## Usage
1. Run the Jupyter notebook `EDA.ipynb` for exploratory data analysis.
2. Run the Jupyter notebooks in the `ml_notebooks/` directory for machine learning models training, and evaluation.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Reference
Federico Soriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Date Retrieved] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.

Janosi,Andras, Steinbrunn,William, Pfisterer,Matthias, and Detrano,Robert. (1988). Heart Disease. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X.