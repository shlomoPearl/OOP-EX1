# Ex1 - Offline algorithm

### this is an offline alghorithm for elevator's destination dispatch system.  
### the problem- in a given set of calls for 'n' elevators to minimize the waiting time for each passenger.

in this algorithm we get a file in type csv of calls for the elvator's. each call with source, destintion of the call and a time stamp wich represent the time that this current call get in the system.  
In adittion we get a file in type json wich represent the building. this file in fact are a 'dictonary'. The first and second keys are the minimum floor and the maximum floor.  
The third key is a 'list' of 'dictioneris' wich represent elevators of this building.  
Each cell in the list contains details about the current elevator- id, speed, minimum floor, maximum floor,close time open time, start time, stop time.  

#### the cmdElevator goes UP and in the max floor he turn and goes DOWN until the min floor.  




  


