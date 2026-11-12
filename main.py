'''
Service Health Checker

- CSV file with domain names
- requests to retrieve an HTTP response code
- loop that checks each domain and sees if they are responding
- output is pushed to a CSV file with the following columns
    - Date
    - Time
    - Domain
    - Status
    - Response code
    - Error message

'''