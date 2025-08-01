DATA_COLLECTION_PROMPT = """

## Tools available

- filesystem: create/write/read files in the local filesystem
- github: access all content in github. 

## Instructions

This is an example of searching for code with a specific extension with a keyword: 
'aspen extension:bkp'. 

Now, please find all those files on the specified page number and tell me what are they about. 
You don't need to give me the files in your response, you will create files instead. 

## Notes

- specify the page number in your search query, currently it is {page_number}
- specify per_page, which is the number of files to return per page, currently it is {per_page}

## Files you will create
 
The output directory is /projects/data/

- full_file_list_{page_number}.txt: a list of all the files you found, with their github url, separated by new lines. 
- file_description_{page_number}.md: a more detailed document, with the file name, the github url, and a description of what the file is about. 

The full_file_list_{page_number}.txt will be used to download the files from github, so make sure it 
contains and only contains the github urls, one per line.

"""
