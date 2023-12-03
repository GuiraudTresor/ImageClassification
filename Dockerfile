# Use an official base image with your desired operating system and version
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy 
COPY /Test_images /web .

# Specify the command to run on container start
CMD ["python", "app.py"]
