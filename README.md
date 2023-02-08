# MyNetDiary-test
## Automated tests for MyNetDiary Web Application
### Register on the project website
1. go to https://www.mynetdiary.com/
2. sign up to the application

### Copy the project
3. open cmd 
4. git clone https://github.com/akurylenka/MyNetDiary-test.git
5. cd .\MyNetDiary-test.git\
6. create virtual environment: python -m venv venv

### Add your credentials to the project
7. create creds.py file, add in file: <br>
email = 'your_email'<br>
password = 'your_password'<br>

### Requirements and run
8. pip install requirements.txt
9. pytest -v --reruns 2 -n 2 --alluredir=reports
10. allure serve reports
