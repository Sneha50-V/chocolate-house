# Chocolate House

Welcome to the Chocolate House! This is a simple Python application that allows users to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions with allergy concerns.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add, update, and delete seasonal flavors.
- Manage ingredient inventory.
- Collect customer flavor suggestions and allergy concerns.

## Technologies Used

- Python
- Flask
- SQLite
- Bootstrap for front-end styling

# Step 1: Navigate to Your Project Directory

Use the cd command to change your directory to the location of your Chocolate House project. For example:

cd C:\Users\91761\OneDrive\Desktop\chocolate1

# Step 2: Create a Virtual Environment

To create a virtual environment, use the following command:

python -m venv env

This command creates a new directory named env in your project folder, which contains the Python interpreter and libraries for your virtual environment.

# Step 3: Activate the Virtual Environment

.\env\Scripts\activate

After activation, your command prompt should change to indicate that the virtual environment is active, typically showing (env) at the beginning of the line.

# Step 4: Install Required Packages

While in the activated virtual environment, install the necessary packages for your project using pip:

This command will install Flask and Flask-SQLAlchemy, which are required for your application to run.

# Step 5: Run the Application

Now that you have installed the required packages, you can run your application. Use the following command:

python app.py

# Step 6: Open Your Browser

Once the application is running, you will see output indicating that the server is running, such as:

Running on http://127.0.0.1:5000
Open a web browser and navigate to http://127.0.0.1:5000 to access your Chocolate House application.

# DOCKER
Docker file
Use the official Python image from the Docker Hub
FROM python:3.9
Set the working directory in the container
WORKDIR /app
Copy the requirements file to the working directory
COPY requirements.txt .
Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
Copy the rest of the application code to the container
COPY . .
Set the environment variable for Flask
ENV FLASK_APP=app.py
Expose the port the app runs on
EXPOSE 5000
Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

# Build the Docker image with the following command:

docker build -t chocolate-house .

# After the image is built, you can run your Docker container with the following command:

docker run -p 5000:5000 chocolate-house

## Docker Setup

This project can be built and run using Docker.

### Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed on your machine.

### Building the Docker Image

1. Navigate to the root directory of the project.
2. Build the Docker image with the following command:

docker build -t chocolate-house .
   
# Run the Docker container using the command:

docker run -p 5000:5000 chocolate-house

### Step 5: Verify Everything Works

1. After updating your README, run through the Docker build and run steps to ensure everything is functioning as expected.
2. Commit your changes to the README and Dockerfile to your Git repository.

### Conclusion

By following these steps, you will have successfully set up a Docker-based build and run environment for your project, and you will have updated your README file with clear instructions for users on how to use Docker to run the application.
