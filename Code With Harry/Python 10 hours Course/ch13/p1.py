# Open terminal and run the following commands:

# virtualenv env1

# virtualenv env2

# .\env1\Scripts\activate.ps1
#There were some issues with the activation of the virtual environment. I had to run the following commands to fix the issue:
# Set-ExecutionPolicy Unrestricted -Scope Process

# .\env1\Scripts\activate.ps1

# pip install pandas

# pip install pyjokes

# pip freeze > requirements.txt

# deactivate

# .\env2\Scripts\activate.ps1

# pip install -r .\requirements.txt
