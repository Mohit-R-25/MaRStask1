# Mars Club Recruitment Submission

## Name: mohit raghavendra

## Overview:
This repository contains my answers, learning experience, (equations, theorems or sketches used to solve the problems), challenges faced, approach for each answer and resources used for Mars Club recruitment.

---
1) Light dose questions' screenshots are in -> [view images](./light)
   
2) Medium dose questions:  
   i) Question 1--> [view code](./medium/q1.py)  
       Equations--> [view image](./Equations/rotationmatrices.png)  
       Challenges faced: I was finding it hard to understand the question at first because I thought the camera and rover had different frames of reference  
       Approach: Converted all the coordinates of object with respect to camera into coordinates of the object with respect to world by using rotation matrices  
       Resources used: https://www.youtube.com/watch?v=R5CpG1eq5uQ , Math Stack Exchange.  
     
   ii) Question 2--> [view code](./medium/q2.py)  
       Equations: ASCII table.  
       Challenges faced: none.  
       Approach: I was finding it hard to decipher the message, split the input string by spaces to isolate each Morse code sequence and map them to their corresponding  alphanumeric characters using a predefined lookup table.   
       Resources used: none.  
       
   iii) Question 3--> [view code](./medium/q3.c)  
       Equations: for postion 1: subract 1, position 2: subtract 2, position 3: subtract 3 and so on.  
       Challenges faced: none.  
       Approach: I was finding it hard to decode the message, iterate through the string, convert each character to uppercase by subtracting 32 if necessary, and then subtract its position-based shift (i+1) from its alphabetical index while using modulo arithmetic to ensure the value wraps correctly within the 26-letter alphabet.  
       Resources: none.  
   iv) Question 4--> [view code](./medium/q4.c)  
       Equations: median and mean.  
       Challenges faced: none.  
       Approach: I was finding it hard to stabilize the sensor data, the rover applied a median filter to a sliding window of the log.txt readings, effectively discarding chaotic outliers caused by microgravity while preserving the true signal necessary for a safe deployment.  
       Resouces: Chatgpt.  
   v) Question 5--> [view code](./medium/q5.py)  
       Equations: none.  
       Challenges faced: The primary challenge lied in implementing a dynamic programming solution that balances segment extension limits and stability constraints while minimizing cumulative transition costs across a multidimensional state space.  
       Approach: Use a dynamic programming approach to track the minimum cumulative wear cost for all valid (Inner,Outer) configurations at each target step, transitioning from the optimal states of the previous target.  

3) Hard dose questions:
   i) Question 1--> 
   
