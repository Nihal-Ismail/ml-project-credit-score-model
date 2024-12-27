# Credit Score Prediction

## Overview
This repository contains a machine learning project for predicting credit scores. The project includes code for data processing, model training, and deployment through a Streamlit web application. It is structured to make it easy to understand, use, and extend.

## Repository Structure

- **Code**: Contains Jupyter Notebook files for data analysis and model training, as well as the dataset used in the project.
- **Artifacts**: Contains the serialized model file (`.joblib`) used for predictions.
- **Main Components**:
  - `main.py`: The entry point for the Streamlit application.
  - `prediction_helpers.py`: Contains helper functions used by the application for making predictions.

## Features

- Predicts credit scores based on user-provided data.
- Streamlit application for easy user interaction.
- Includes pre-trained machine learning model saved as a `.joblib` file.
- Modular design for reusability and scalability.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-score-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd credit-score-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

## Usage

- **Dataset**: The dataset is located in the `Code` folder. It is used for training and testing the model.
- **Model**: The pre-trained model file (`.joblib`) is stored in the `Artifacts` folder and is loaded during the application runtime.
- **Streamlit Application**: Launch the app using the `main.py` file. It provides a user-friendly interface for entering data and viewing predictions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, feel free to reach out:

- **Author**: Muhammed Nihal C
- **Email**: [menihalismail@gmail.com](mailto:your-email@example.com)

---
Thank you for exploring the Credit Score Prediction project! We hope it helps you in understanding and solving credit score prediction challenges.

