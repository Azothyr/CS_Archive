from utils.format_ops import str_basic_ops


def process_text_to_print(text, **kwargs):
    "rules = jsonmanager"
    order_of_operations = ['start', 'end', 'upper', 'lower', 'capitalize', 'wrap', 'replace']

    # Using the parser:
    parser = KwargsParser(rules)
    parsed_values = parser.parse(start='test', end='end_test', upper=True)
    print(parsed_values)  # Outputs: {'start': '[Start-test]', 'end': '[End-end_test]', 'upper': True}
