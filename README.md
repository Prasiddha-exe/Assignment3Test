# Assignment3Test

# **Overview of the Project - Ferry Requisition Booking System**

The program functions as a basic Python platform which handles and compiles ferry reservation management.
Through this system users can input their information while selecting requested services after which the program determines the total cost of services for their booking. 
The system establishes three booking statuses through which it approves or reserves or disapproves bookings depending on their cost.
The program prints out the summary results after processing multiple booking data.

# **Simplicity of the code – KISS ( Keep it Simple , Stupid. )**

The program designers maintained a straightforward and understandable code structure.
Each section within the program uses simple direct language while completely avoiding processes that lead to confusion.
Inside a single class the program contains various functions which manages separate operational segments of the task.
Advanced logic remains absent and excessive abstraction does not exist. 
By applying KISS principles the code becomes easy to maintain because it simplifies the change and fix possibilities in the future.

# **DRY**

The programming code prevents the unnecessary duplicate display of identical lines that is throughout the codebase. 
The program implements reusable functions that eliminate unnecessary repetition of print statements and calculations.
Three significant business functions maintain separate individual methods within the system including customer information handling and services evaluation along with price calculation.
The system maintains the DRY principles throughout its development.



# **Adding the Features in the codes – Open/Closed Rule** 

The system design allows programmers to add new rules or enhance existing ones without altering the entire program structures.
A single method serves as the editing point for implementing discounts codes and special approval rules in the approval logic.


# **Composition**

The booking system runs from one single class thus this maintaining proper organizational unity.
The distribution of code across multiple small classes becomes unnecessary when we are using this method for managing a project of this size.

# **Focused Functions – Single Responsibility**

Every function within a class operates independently to perform one duty at a time.
The class contains separate functions that deal with user information as well as approval procedures before showing the booking results. 
The structure of the code allows viewers to grasp each segment individually.

# *Things That Could Improve*

The code would benefit from divided structure at specific points. 
The approval check method combines both input processing and logical evaluation into a single element.
Additional protection mechanisms to prevent empty input do not exist currently.
Bookings are still processed even when users provide no name in the booking form.
Better input checks will be implemented throughout future updates.

# **Conclusion**

The ferry requisition system presents an uncomplicated example of Python-based data collection as well as decision-making and result output functionality.
The implementation demonstrates real-world application of programming guidelines such as including KISS, DRY and Single Responsibility. 
The system functions imperitably though it exemplifies how functions and classes enable production of clean working code through straightforward solutions. 
The code will become more reliable in the upcoming updates following improvements in validation techniques and separation logic implementation.

# -------------- *Thank you* -------------







