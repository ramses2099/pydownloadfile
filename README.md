# pydownloadfile
Python Program for download big file

# create env
╰─ python -m venv venv 
# create env in ubuntu
python3 -m venv venv  

# active the environment in powershell
╰─ .\venv\Scripts\Activate.ps1  

# active the environment in ubuntu
source venv/bin/activate

╰─ pip list

╰─ python.exe -m pip install --upgrade pip

# deativate the environment ubuntu
deactivate

# install python packages
pip install python-dotenv
pip install newsapi
pip install newsapi-python
pip install kafka-python
pip install six
pip install kafka-python-ng

# create requierment file
pip freeze > requirements.txt

# install requirements package
pip install -r requirements.txt
sudo pip3 install -r requirements.txt


# create topic in kafka
kafka-topics.sh --create topicnews localhost:9092

