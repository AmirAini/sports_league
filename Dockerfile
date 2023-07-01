# Use the official Django 3.9-alpine base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the port on which your Django app will run (default is 8000)
EXPOSE 8000

# Define the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
