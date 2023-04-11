# Fractal Analysis
#### Video Demo: <https://youtu.be/G_DhLdtVgW0>
#### Description:
TODO
My project  focused on applying the GCOA (Generalized Cantor Set-Based Oscillation Algorithm) to a set of data in a CSV file, and then visualizing the output using a scatter plot. In this response, I will provide a more detailed description of my project, its features, and how it is implemented.

Features of my Software
The main feature of my software is its ability to apply the GCOA algorithm to data in a CSV file. The GCOA algorithm is a mathematical method used to create oscillations based on a generalized Cantor set. This algorithm is implemented in your software using the Pandas library and the math library in Python. Specifically, the main program imports the Pandas library as pd and the math library.

The readF() function is defined to read data from an existing CSV file called "Fractal.csv". This function reads from the file using a try-except block, and if the file doesn't exist, it creates an empty Pandas DataFrame with a column named 'Ampitude'. The function returns a tuple with two elements, the first element is a boolean indicating if the file was successfully read or not, and the second element is a Pandas DataFrame. If the 'Ampitude' column is not in the file or if there are other columns in the file, the function prints a message indicating that the column(s) will be ignored.

The GCOA() function is defined to perform the GCOA algorithm on the Pandas DataFrame. This function takes a Pandas DataFrame as input and returns a Pandas DataFrame with the sorted amplitude values, the abundance of each amplitude value, the cumulative total frequency of each amplitude value, and the logarithm (base 10) of the sorted amplitude and cumulative total frequency values. The function uses a dictionary to count the frequency of each amplitude value in the input DataFrame, sorts the dictionary by amplitude and abundance, and copies the sorted data to a new Pandas DataFrame.

The main() function is defined to call the readF() and GCOA() functions and save the output DataFrame to the "Fractal.csv" file. If the readF() function successfully reads data from the file, the GCOA() function is called and the output DataFrame is saved to the file. The output DataFrame is then passed to the show() function to display a scatter plot.

How to implemented my Software ?
My software is implemented using the Python programming language and several libraries including Pandas and math. The main program imports the Pandas and math libraries, defines the readF(), GCOA(), and main() functions, and then calls the main() function to run the program.

The readF() function uses Pandas to read data from a CSV file. If the file doesn't exist, the function creates an empty Pandas DataFrame with a column named 'Ampitude'. If the 'Ampitude' column is not in the file or if there are other columns in the file, the function prints a message indicating that the column(s) will be ignored.

The GCOA() function takes a Pandas DataFrame as input and applies the GCOA algorithm to the data. Specifically, the function uses a dictionary to count the frequency of each amplitude value in the input DataFrame, sorts the dictionary by amplitude and abundance, and copies the sorted data to a new Pandas DataFrame. The function then returns this new DataFrame.

The main() function calls the readF() function to read data from the CSV file, and if successful, calls the GCOA() function to apply the GCOA algorithm to the data. The output DataFrame is then saved to the "Fractal.csv" file, and passed to the show() function to print the result in the output
