A script that takes an html page and replaces its header and footer with 
those provided in two respective config files.

Usage:
python template_generator.py <html file path> <header file path> <footer file path>

Where:
<html file path> = the path to the html page
<header file path> = the path to a file containing the html code for the header (including the header tags)
<footer file path> = the path to a file containing the html code for the footer (including the footer tags)

The config files can be of any type, can include any tags and comments, and their output is automatically 
formatted.