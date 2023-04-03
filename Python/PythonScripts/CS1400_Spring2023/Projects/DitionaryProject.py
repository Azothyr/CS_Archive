import sys


def get_summary(lines):
    """
        Extracts information from each line in the input file and generates a summary dictionary

        Returns:
        A dictionary where each key is a code and each value is a nested dictionary with the following keys:
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
            summary[code] = {"longest": {"text": text, "line_number": line_number, "length": len(text)},
                             "shortest": {"text": text, "line_number": line_number, "length": len(text)},
                             "total_length": len(text), "num_lines": 1}
        else:
            current_length = len(text.strip())
            if current_length > summary[code]["longest"]["length"]:
                summary[code]["longest"] = {"text": text, "line_number": line_number, "length": current_length}
            elif current_length == summary[code]["longest"]["length"] and line_number > summary[code]["longest"]["line_number"]:
                summary[code]["longest"] = {"text": text, "line_number": line_number, "length": current_length}
            if current_length < summary[code]["shortest"]["length"]:
                summary[code]["shortest"] = {"text": text, "line_number": line_number, "length": current_length}
            elif current_length == summary[code]["shortest"]["length"] and line_number < summary[code]["shortest"]["line_number"]:
                summary[code]["shortest"] = {"text": text, "line_number": line_number, "length": current_length}
            summary[code]["total_length"] += current_length
            summary[code]["num_lines"] += 1
    for code, values in summary.items():
        values["avg_length"] = round(values["total_length"] / values["num_lines"])
    return summary



def write_summary(summary, filename):
    """
        Writes the summary dictionary to a file.
    """
    with open(filename, "w") as f:
        for code, data in sorted(summary.items()):
            f.write("{}".format(code))
            f.write("Longest line ({line_number}): {text}...{ellipsis}\n".format(
                line_number=data['longest']['line_number'],
                text=data['longest']['text'],
                ellipsis='...' if len(data['longest']['text']) > 50 else ''
            ))
            f.write("Shortest line ({line_number}): {text}\n".format(
                line_number=data['shortest']['line_number'],
                text=data['shortest']['text']
            ))
            f.write("Average length: {}\n\n".format(data['avg_length']))



def write_text(text_dict, filename):
    """
    Writes all the text of the input file, organized by code and separated by '-----', to a file.
    """
    with open(filename, "w") as f:
        for code, lines in text_dict.items():
            f.write(f"{code}\n")
            for line in lines:
                f.write(f"{line.strip()}\n")
            f.write("-----\n")


def main():
    """
    Main function of the program. Takes no arguments

    Reads the contents of a file specified by the first command line argument
    Extracts text from the file and separates it into a text and a summary dictionary
    Return: Written summary information to "novel_summary.txt" and novel text to "novel_text.txt"
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        raise ValueError("Error: Please provide a filename as an argument.")

    with open(filename, 'r') as f:
        lines = f.readlines()

    summary_dict, text_dict = {}, {}
    for line in lines:
        text, line_number, code = line.split("|")
        line_number = int(line_number)
        if code not in text_dict:
            text_dict[code] = [text]
        else:
            text_dict[code].append(text)

    summary_dict = get_summary(lines)
    write_summary(summary_dict, 'novel_summary.txt')
    write_text(text_dict, 'novel_text.txt')


if __name__ == '__main__':
    main()
