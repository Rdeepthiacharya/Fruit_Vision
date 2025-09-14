## Project Description

The system uses a trained machine learning model to classify fruits into **fresh** or **rotten** categories.  
Users can upload images of fruits through the web interface, and the model will return predictions instantly.  

Currently, the model is trained to recognize and classify the following fruits:
- Apple  
- Banana  
- Orange   

The backend is powered by Flask, handling routes, predictions, and template rendering.  
The frontend provides a clean, responsive design to make the platform user-friendly and accessible.  

This project demonstrates how machine learning can be integrated into real-world web applications to promote food safety, efficiency, and sustainability.



## Getting Started

To get started with this project, you need to have the following installed on your system:

- Python 3.10.
- pip (Python package manager).
- VS Code with the Jupyter extension or Anaconda (or any editor of your choice).

Once installed, you can clone the repository and run the application on your local machine.



## Prerequisites

Before running the application, make sure you have:

- Installed all required dependencies (`requirements.txt` is provided).  
- Downloaded a fruit dataset and divided it into train/ and test/ folders (these are excluded from the repository). 
- Train the machine learning model using the provided `Fruits Vision.ipynb` notebook.  
- Save the trained model file inside the project directory (the model file is excluded from this repo due to size).
- A system with **RAM: 8GB or higher** (recommended for model training).

The model is specifically trained for apples, bananas, and oranges (both fresh and rotten).



## Running the Application

To run the application, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it (if using one).
3. Install the required packages: pip install -r requirements.txt
4. Start the Flask server: python app.py
5. Open a web browser and navigate to: http://localhost:5000/



## Features

The application offers the following features:

- Upload fruit images for prediction
- Machine learning model for fruit classification
- Simple and responsive interface
- Real-time results
- Helps reduce food waste by detecting rotten fruits
  


## Built With

- Python Flask – Backend framework
- Machine Learning (TensorFlow / Keras) – Model training and prediction
- HTML, CSS, JavaScript – Frontend design
- Jupyter Notebook – Model training and experimentation


  
## License

This project is licensed under the MIT License - see the[License](https://github.com/Rdeepthiacharya/Fruit_Vision/blob/master/LICENSE) file for details.
