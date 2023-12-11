# Mobile Test Automation Project

This project is a mobile test automation framework designed for iOS and Android platforms. It utilizes Python, Appium, Pytest, Pipenv, Pyenv, and Git for building a robust and scalable mobile testing solution.

### Prerequisites
Before running the tests, ensure you have the following installed:

- Python 3.9.6
- pipenv and pyenv
- Git
- Appium Server
- java
- Android Studio + SDK
- Xcode and tools
- libimobiledevice
- ideviceinstaller



### Installation
1. Clone the repository to your local machine:
    git clone https://github.com/mottipazlazar/mh_assignment.git 
    
2. Navigate to the project directory:
  cd <project_directory>

3. Install project dependencies using Pipenv:
    pipenv install --dev


### Configuration
Update the `pytest.ini` file to set the desired mobile operating system type:

mobile_os_type = ios
; Uncomment the line below for Android testing
; mobile_os_type = android


## Running Tests
Execute the following command to run the test suite:
pipenv run python invoker.py



## Some assumptions and limitations taken to simplify current delivery:
1.	Valid users already signed up before
2.	Flow begins on “Discover” landing page, and nowhere else.
3.	Permissions popups have already been approved/rejected before.
4.	No captcha handling needed.
5.	Logout always succeeds.No handling for failed logout.
6.	No other popups handling during flows, for example:
 ![image](https://github.com/mottipazlazar/mh_assignment/assets/32642069/f2ca8327-98ad-4bf3-a0af-46f6119d0f06)

Or this:
 ![image](https://github.com/mottipazlazar/mh_assignment/assets/32642069/665a1e18-11b6-4ac1-8377-7edb17dec213)

7.	No OS versions compatibility support yet
8.	No popup handling except for logout popup, and no missing popup handling

