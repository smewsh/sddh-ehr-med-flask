# Flask Server

This project is a Flask server built using Python 3.9. The following instructions will guide you on how to set up and run the server using a virtual environment (venv).

## Prerequisites

- Python 3.9
- pip

## Setup

1. Create a virtual environment using Python 3.9:
   ```
   python3.9 -m venv venv
   ```
2. Activate the virtual environment:

    - For Windows:
    ```
    venv\Scripts\activate
    ```

    - For macOS and Linux:
    ```
    source venv/bin/activate
    ```

3. Install the required packages from the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```


## Running the Server

1. Ensure the virtual environment is active (repeat step 3 in the Setup section if needed).

2. Start the Flask server by running:

```
python run.py
```

The server will start, and you should see output similar to the following:
```
----------------------------------------------------------------------
Web Server Started!
Please open your browser to: http://127.0.0.1:8001/
----------------------------------------------------------------------
```

3. Open your web browser and navigate to the URL displayed in the console (e.g., `http://127.0.0.1:5000/`) to access the Flask application.

## Stopping the Server

To stop the Flask server, press `CTRL+C` in the terminal or command prompt where the server is running.

## Deactivating the Virtual Environment

After you have finished working with the Flask server, deactivate the virtual environment:

```
deactivate
```


This command will return you to your system's global Python environment.

# My Health Record

## How to use

The current iteration of this app is intented to fulfll the workflow of a Doctor logging in, and viewing their patients. From here, the doctor can add notes, but also register new patients to the system. The web app also has a privileges system, such that access control can be implemented for certain pages.

To test the prototype, you can use the supplied account, (username:`admin`, password:`admin`).

### Privileges

With this admin account, the priviliges system can be used, by navigating to the `<site>/manageusers/` page. 
The current privileges system works as a simple whitelist system, and only applies to certain pages (at this stage, only `/manageusers/`).


### Doctor Workflow

1. Log in to account (use test account username:`admin` password:`admin`)
2. Click on Patients tab
3. Choose a patient to view information by clicking on a name
4. Click `Add Note`
5. Click back
6. Scroll to the bottom, and click `Add Patient`
7. Enter details
8. Submit
9. Log out by clicking the `logout` link in the top right.
