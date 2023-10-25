# Use the official Python image as a parent image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY ./requirements.txt /app/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY ./UniSabana/ /app/UniSabana/

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django application using manage.py
CMD ["python", "UniSabana/manage.py", "runserver", "0.0.0.0:8000"]