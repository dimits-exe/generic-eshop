import re
import sys
import bs4

"""
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
"""


def main(html_file_path: str, header_file_path: str, footer_file_path: str):
    try:
        with open(html_file_path, "r") as html_file:
            html_contents = html_file.read()
    except IOError as ioe:
        print(f"Cannot read HTML input file {html_file_path}: {ioe}")
        sys.exit(-1)

    html_soup = bs4.BeautifulSoup(html_contents, "html.parser")

    # delete old template code
    delete_section(html_soup, "header")
    delete_section(html_soup, "footer")
    new_html_contents = str(html_soup.prettify())

    # read new template code
    try:
        header = read_section(header_file_path)
    except IOError as ioe:
        print(f"Cannot read header config file {header_file_path}: {ioe}")
        sys.exit(-1)

    try:
        footer = read_section(footer_file_path)
    except IOError as ioe:
        print(f"Cannot read header config file {footer_file_path}: {ioe}")
        sys.exit(-1)

    # add template html code
    new_html_contents = add_header(new_html_contents, header)
    new_html_contents = add_footer(new_html_contents, footer)

    # format html
    new_html_soup = bs4.BeautifulSoup(new_html_contents, "html.parser")

    try:
        with open(html_file_path, "w") as html_file:
            html_file.write(str(new_html_soup.prettify()))
    except IOError as ioe:
        print(f"Cannot write back to HTML file {html_file_path}: {ioe}")
        sys.exit(-1)


def delete_section(soup: bs4.BeautifulSoup, tag: str):
    for elm in soup.find_all(tag):
        elm.decompose()


def read_section(section_file_path: str) -> str:
    with open(section_file_path, "r") as section_file:
        return section_file.read()


def add_header(html_content: str, header: str) -> str:
    tag = "<main>"
    index = html_content.find(tag)
    return html_content[:index] + header + html_content[index:len(html_content)]


def add_footer(html_content: str, footer: str) -> str:
    tag = "</main>"
    index = html_content.find(tag) + len(tag) # add after main end-tag
    return html_content[:index] + footer + html_content[index:]


def write_new_line(line, current_indent, desired_indent):
    new_line = ""
    spaces_to_add = (current_indent * desired_indent) - current_indent
    if spaces_to_add > 0:
        for i in range(spaces_to_add):
            new_line += " "
    new_line += str(line) + "\n"
    return new_line


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
