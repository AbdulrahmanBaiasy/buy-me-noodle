#!/bin/bash

# Create virtual environment (if not already done)
echo "Creating or activating virtual environment..."
python3.12 -m venv venv
source venv/bin/activate

# (Optional) Update pip if necessary
python -m pip install --upgrade pip 

# Install dependencies
echo "Installing project dependencies..."
pip install -r requirements.txt

# Navigate to the core directory

# Make migrations
echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Build process completed!"
