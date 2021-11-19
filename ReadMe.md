# Ex1 - Offline algorithm

## Algorithm description- this is an algorithm which deals with embedding calling elevators.  
### lagnguage - python.  

In this algorithm all the calls are accepted as input (the alghorithm is defined offline). And therefore when set of calls is recived we would like to ammbed it to the elevator so the stand by time from the time stamp of the calling until reaching the destination will be minimal.  

**_Input-_**  
- json file that represnts building.  
- csv file that represnts callings set.  
- file name that represnts the name of output file.  

**_Output-_**  
- csv file that contains the data calls and to which elevator each call is directed.  

*The idea of the algorithm-* is to calculate the percentege of calls to each elevator acorrding to the speed.   

*Algorithm classes-*  
     1.class *Elevator* which represent the technical data of each elevator and queue of calls for this elevator.   
     2.class *Building* which represent the quantity of elevators in the building and maximal/minimal floor in the building.  
     3.class *ElevatorCalls* which represent the set of calls that are recived in the building.  

*Algorithm operation-*   
    1. first of all we build the building and elvator call clases from csv/json file in the input.
    2. calculate the percentege of calls to each elevator acorrding to the speed.  
    3. will direct calls to each elevaor according the calculate.and will spread the calls acording the percenteg of calls it getts (i.e if the percntege of the elevator 'i' is 25 it means that each forth call will be directed to elevator 'i').  
    4. at the end will make sure that each call is directed and will make a new file.

