Coding Challenge

Author - Vivek Muralidharan
Date - 2021/12/05

1) Problem Statement
	- Combine files in a location and display Source IP and Environment.
2) Assumptions
	- Only csv files are to be read.
	- All the source files will have the same structure
	- The Environment name will be numbers and “.csv” removed from the end of file name.
	- Even though the data is different, it’s ok to process the csv file if it has the expected number of columns.
	- The final csv must not have duplicates based on “Source IP” and “Environment”.

3) How to run combine_csv.py
	- The python script is named combine_csv.py.
	- It expects a source file folder, Target file name with path, and the log file location as parameters in the order as written below.
	  python combine_csv.py <source file path> <target file name with path> <log file path>
	- The log file name combine_csv.log has been coded into the python script.
