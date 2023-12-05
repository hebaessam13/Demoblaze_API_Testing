# DEMOBLAZE API Automation Framework with Python
#

## SETUP
### Environment Setup
- Python version 3.10.5

### Create Virtual environment
- create a virtual environment named env
```commandline
 python -m venv virtualenv
```
- activate environment
```commandline
.\virtualenv\Scripts\activate
```
### Install required packages
```commandline
pip install -r requirements.txt
```
### Runing Tests
- specify tests you want to run by marker (signup, login)
```commandline
python -m pytest -m marker
```
- to run all tests
```commandline
python -m pytest 
```
### Using Docker
- to build image after changes
```commandline
docker build . -t imageName:version
ex: docker build  . -t demoblaze:latest 
```
- to run all tests
```commandline
docker run demoblaze:latest
```
- to run tests with markers
```commandline
docker run -e MARKER=login demoblaze:latest
```

- to extract reports and logs from container
```commandline
docker cp containerID:usr/src/reports ./desiredlocation
docker cp containerID:usr/src/logs ./desiredlocation
```

#
#
## Project Structure

- **modules**:
  * users: include all apis that interacts with the user entity so it can be used in any other api testing that requires user related setup
- **test_data**
  * users_test_data: include any data that will be used in creating data driven tests
  * It can also include static json files that could be used to validate responses with static data
- **utils**:
  * api: include helper methods to make it more readable when using making api requests and getting urls and also contains all endpoints which can be exported in another file if necessary
  * data_generator: include helper methods to generate random string which can be used when creating users
- **tests**:
  * user_tests: include files for each endpoint testing, this separation helps with modularity and with keeping test files small and maintainable
  * conftest: include any required fixtures or setup necessary 
- **Reports and Logs**: include generated logs files and summary reports
- **.env**: include any environment related variable should be part of .gitignore file but will be included in the repo as part of the test solution
#
## Problems with APIs under test
- usually when testing login/signup functionalities whether through api or ui, cleanup should follow the test which is not applicable at the moment as this is a dummy website for testing purposes.
- So for testing the signup, I'd have two tests one for the positive scenarios which will be followed by a cleanup call to delete the newly created user and another test for the negative signup cases.
- And for the login, I'd use the same data to create a user as a setup(before test fixture) and after testing the login api, this user will also be deleted.
- To Test the login functionality for now, I assumed keirahahe account an existing user/superuser and added the test cases based on that.
- the current implementation of the api is full of bugs so most of the apis are failing in the assertion.
