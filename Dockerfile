# Use the official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./flask .

# Install Flask
RUN pip install flask


# Command to run the application
CMD ["python", "app.py"]
