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
       Resources used: https://www.youtube.com/watch?v=R5CpG1eq5uQ , Math Stack Exchange  
   ii) Question 2--> [view code](./medium/q2.py)
       Equations: ASCII table.  
       Challenges faced: none.  
       Approach: To decipher the message, split the input string by spaces to isolate each Morse code sequence and map them to their corresponding  alphanumeric characters using a predefined lookup table.  
       Resources used: none.  
       
   iii) Question 3--> [view code](./medium/q3.c)
       Equations: for postion 1: subract 1, position 2: subtract 2, position 3: subtract 3 and so on.
       Challenges faced: none.  
       Approach: To decode the message, iterate through the string, convert each character to uppercase by subtracting 32 if necessary, and then subtract its position-based shift (i+1) from its alphabetical index while using modulo arithmetic to ensure the value wraps correctly within the 26-letter alphabet.  
   iv) Question 4--> [view code]  
   v) Question 5--> [view code](./medium/q5.py)  
   
