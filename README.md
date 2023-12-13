# Shojin Point

## What is this?
This app gets an AtCoder user's submissions and calculate "Shojin Point".

## Installation
1. Install Python (Python3.10 is recommended).
2. Install following libraries:
    - flet
    - schedule
    - requests
    - lark
3. Copy shojinpoint directory to somewhere.
4. Done!

## How to use
1. Run "shojinpoint.py" (ex. type "python3 ./shojinpoint.py" in shojinpoint directory).
2. Click "Settings" menu (gear icon).
3. Input following values:
    - User name: Your username.
    - Begin/End date: Beginning and ending of the aggregation period. Make sure to input in "YYYY-MM-DD hh:mm:ss" format.
    - Formula: The formula of calculating "Shojin Point". These variables are available:
        - \[tee\]: Total TEE in period.
        - \[x\] \[y\] \[z\]: Constants.
    - x/y/z: Constants values. Please input 0 into unused values.
4. Press "OK" button.
5. Click "Main" menu (chart icon) and you'll see points!
