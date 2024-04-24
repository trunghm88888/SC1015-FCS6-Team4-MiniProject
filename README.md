# SC1015-FCS6-Team4
# Heart Failure Classification Project

## Overview
This repository contains code and resources for a machine learning project aimed at predicting heart failure based on clinical data. The goal of the project is to build and deploy a classification model that can accurately predict the likelihood of heart failure in patients.

## Dataset
The dataset used for this project is the [Heart Failure Prediction Dataset](https://www.kaggle.com/fedesoriano/heart-failure-prediction) by [Federico Soriano](https://www.kaggle.com/fedesoriano) available on Kaggle. It contains 11 clinical features along with a binary target variable indicating whether the patient died or not.

## Project Structure
- `data/`: Directory to store the dataset.
- `EDA.ipynb`: Notebook for `Exploratory Data Analysis`.
- `ml_notebooks/`: Directory containing notebooks for `Machine Learning` tasks.
  - `helper_functions.py`: Python file containing helper functions.
  - `setup.ipynb`: Notebook for initial project setup.
  - `knn.ipynb`: Notebook for `K-Nearest Neighbors` model.
  - `svm.ipynb`: Notebook for `Support Vector Machine` model.
  - `tree_based.ipynb`: Notebook for `Tree-based` models.
- `README.md`: Project overview, instructions, and documentation.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/trunghm88888/SC1015-FCS6-Team4-MiniProject.git
    cd SC1015-FCS6-Team4-MiniProject
    ```

## Usage
1. Run the Jupyter notebook `EDA.ipynb` for `Exploratory Data Analysis`.
2. Run the Jupyter notebooks in the `ml_notebooks/` directory for `Machine Learning` models training, and evaluation.

## Conclusion
- `K-Nearest Neighbors` and `Support Vector Machine` gives very similar result: `False Positive Rate` ~ 12%, `False Negative Rate` ~ 10%.
- For `Tree-based` models, `RandomForest` does best at `False Positive Rate` ~ 12%, `False Negative Rate` ~ 10% with default hyper-params, `LightGBM` best result is `False Positive Rate` ~ 10%, `False Negative Rate` ~ 15%.
- Seems like `False Negative Rate` ~ 10% is the limit of what you could get from this dataset, other simpler methods (like Logistic Regression) and more complex methods (Deep Neural Network) should be used to confirm this.
- The dataset is very old, with a newer dataset with better clinical measurements we could get better result, the aim is to bring the `False Negative Rate` (the important stat) to below 5%, although introducing a lower cut-off point for Negative might help temporarily.

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

## Contributors
- [Hoang Minh Trung](https://github.com/trunghm88888): Data Preprocessing and Machine Learning.
- [Aviral](https://github.com/Aviral00001): Exploratory Data Analysis.
- [Prasanna](https://github.com/Prasntu21): Exploratory Data Analysis.
