#Find out your current working directory
import os
print(os.getcwd())
# Out: /Users/shane/Documents/blog
# Display all of the files found in your current working directory
print(os.listdir(os.getcwd()))
# Out: ['test_delimted.ssv', 'CSV Blog.ipynb', 'test_data.csv']