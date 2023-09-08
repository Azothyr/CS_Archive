"""
Project Name: Project 4: Library of Congress
Author: Zachary Peterson
Due Date: 2023-03-31
Course: CS1400-x01

This code takes in a text file that has lines with text, line number, and a 3-letter code,
separated by an '|'. It then splits the line at each '|',
organizes the data into text based on the code then line number and output
a summary and organized text in separate txt files
"""
import sys


def get_summary(lines):
    """
        Extracts information from each line in the input file and generates a summary dictionary

        Returns:
        A dictionary where each key is a code and
        each value is a nested dictionary with the following keys:
        - 'longest': longest line dictionary with keys 'text', 'line_number', and 'length'
        - 'shortest': shortest line dictionary with keys 'text', 'line_number', and 'length'
        - 'total_length': total length of all lines
        - 'num_lines': number of all lines
        - 'avg_length': average length of all lines with the code (rounded to the nearest integer)
    """
    summary = {}
    for line in lines:
        text, line_number, code = line.split("|")
        line_number = int(line_number)
        text = text.strip()
        if code not in summary:
            summary[code] = {"longest": {"text": text, "line_number": line_number,
                                         "length": len(text)},
                             "shortest": {"text": text, "line_number": line_number,
                                          "length": len(text)},
                             "total_length": len(text), "num_lines": 1}
        else:
            current_length = len(text.strip())
            if current_length > summary[code]["longest"]["length"]:
                summary[code]["longest"] = {"text": text, "line_number": line_number,
                                            "length": current_length}
            elif current_length == summary[code]["longest"]["length"] and line_number > summary[
                code]["longest"]["line_number"]:
                summary[code]["longest"] = {"text": text, "line_number": line_number,
                                            "length": current_length}
            if current_length < summary[code]["shortest"]["length"]:
                summary[code]["shortest"] = {"text": text, "line_number": line_number,
                                             "length": current_length}
            elif current_length == summary[code]["shortest"]["length"] and line_number < summary[
                code]["shortest"]["line_number"]:
                summary[code]["shortest"] = {"text": text, "line_number": line_number,
                                             "length": current_length}
            summary[code]["total_length"] += current_length
            summary[code]["num_lines"] += 1
    for code, values in summary.items():
        values["avg_length"] = round(values["total_length"] / values["num_lines"])
    return summary


def write_summary(summary, filename):
    """
        Writes the summary dictionary to a file.
    """
    with open(filename, "w", encoding='utf-8') as file:
        for code, data in sorted(summary.items()):
            file.write(f"{code}")
            file.write(f"Longest line ({data['longest']['line_number']}): {data['longest']['text']}\n")
            file.write(f"Shortest line ({data['shortest']['line_number']}): "
                       f"{data['shortest']['text']}\n")
            file.write(f"Average length: {data['avg_length']}\n\n")


def write_text(text_dict, filename):
    """
    Writes all the text of the input file,
    organized by the dictionary key 'code' and separated by '-----', to a file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        sorted_items = sorted(text_dict.items())
        for i, (code, text_list) in enumerate(sorted_items):
            file.write(code)
            for text_item in sorted(text_list, key=lambda x: x["line_number"]):
                file.write(text_item['text'] + '\n')
            if i != len(sorted_items) - 1:
                file.write('-----\n')


def main():
    """
    Main cus_funcs of the program. Takes no arguments

    Reads the contents of a file specified by the first command line argument
    Extracts text from the file and separates it into a text and a summary dictionary
    Return: Written summary information to "novel_summary.txt" and novel text to "novel_text.txt"
    """
    try:
        filename = sys.argv[1]
    except IndexError as exc:
        raise ValueError("Error: Please provide a filename as an argument.") from exc

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    summary_dict, text_dict = {}, {}
    for line in lines:
        text, line_number, code = line.split("|")
        line_number = int(line_number)
        text = text.strip()
        if code not in text_dict:
            text_dict[code] = [{"text": text, "line_number": line_number}]
        else:
            text_dict[code].append({"text": text, "line_number": line_number})

    summary_dict = get_summary(lines)
    write_summary(summary_dict, 'novel_summary.txt')
    write_text(text_dict, 'novel_text.txt')


if __name__ == '__main__':
    main()
