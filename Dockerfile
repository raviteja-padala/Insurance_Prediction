
# Use an official Python runtime as the base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code to the working directory
COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt


# Expose the port that the Streamlit app will listen on
EXPOSE 8501

# Set the default command to run when the container starts
CMD ["streamlit", "run", "--server.enableCORS", "false", "app_streamlit.py"]

