# Author: Andre Doumad

# PaymentWorks Coding Problem

This program allows the user to see/request a list of all subway lines in Boston.


# HTTP Data Retrieval and Decoding 
We will be using the API at https://www.mbta.com/developers/v3-api. 

1. The two API endpoints we expect you to use are:  
○ https://api-v3.mbta.com/routes - lists all the subway lines, commuter-rail lines, bus-lines and ferry-routes  
○ https://api-v3.mbta.com/stops - lists all the stops for those routes   
○ You are free to use other endpoints at your discretion. 

2. Your program should allow the user to see/request a list of all subway lines in Boston.  
The output should provide the user with both the name and “ID” of each line.  
For example, the output should provide information that includes:  
○ ID: Red, NAME: Red Line  
○ ID: Green-B NAME: Green Line B   
○ ID: Orange NAME: Orange Line  
○ Note these three bullets are a sample, they are not complete output nor do they imply your output must be text-based   

3. Your program should also allow the user to see the list of all stops on a particular subway-line, where the user 
specifies the subway-line by providing or selecting that line’s “ID”. For example, if the user provides / selects the 
ID “Red”, then the resulting output should show all stops on the Red Line.


# DOCKER USAGE 
0. Ensure that you have docker installed
1. cd to .../PaymentWorksCodingProblem/docker
2. run docker-compose up --build
3. navigate to http://0.0.0.0:8000/mtba/routes/
4. navigate to http://0.0.0.0:8000/mtba/stops/
5. user input with url params like so: http://0.0.0.0:8000/mtba/stops/Red
6. Note: The source data is pulled from mtba db and serialized into our db which takes some time to process. 

# TESTING USAGE

0. Ensure you're in a virtual environment, its activated and that you've installed the requirements.txt
1. cd to .../PaymentWorksCodingProblem/src
2. run pytest
3. the tests should pass in about 15 seconds.

# Given more time...

I'd like to add more to this to improve performance.  
Some work might include a postgres database link.  
Perhaps some kind of caching system.  
Some additional endpoints or parameters that do not take the extra time to pull from the mtba website.  
Instead of using url params, include usage for request body as well.  
Some templating to provide some limited dashboard UI functionality.  
More nested serialization / logic improvements to reduce the impact on the database.  
I'd like to see some more error handling.  
I would add more fixtures to support my assertions and separate each test into a single assertion and parameterize them.  

# Closing thoughts...

I love Django, this is a fantastic framework for handling data and building api.  
This was what I would consider a "fun" assessment, and I enjoyed spending some time on it.
