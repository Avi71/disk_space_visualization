# disk_space_visualization
A visualization of the distribution of disk space within a directory.

Use Jupyter Notebook to run the given week2_project.ipynb file as I used the same.

Software used while making the project was Jupyter Notebook itself.

Some details about my project are as follows:

1. First a directory is taken as an input.

2. Then a check() function is executed to know whether the given directory exists in the system if no, then input of a new directory is asked.

3. Next a Data Frame is created using pandas to get a tabular visualization of the files in the given directory and their respective occupied size. To get the size "st_size" is used, its function is to return: Size in bytes of a plain file; amount of data waiting on some special files.

 4. A scatter, bar and line plot of the Data Frame is given as output. This is achieved using plotly and to use it in offline mode cufflinks package is used.

 5. Then an input is taken from the user to ask if he/she wants to go to:
      a. Child Directory
          Then the user is asked to specify the child folder in which he/she want to go.
      b. Parent directory
      c. Exit

6. The current directory is then changed using os.chdir(file_path) and the steps 3,4 and 5 are repeated unless the user wants to Exit.
