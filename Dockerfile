# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application source code from Jenkins workspace to the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your Python application
CMD ["python", "Tic_Tac_Toe.py"]
