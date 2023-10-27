import sys
import json

def update_test_values(tests, values_dict):

    def update_values(test):
        if test['id'] in values_dict:
            test['value'] = values_dict[test['id']]
        if 'values' in test:
            for subtest in test['values']:
                update_values(subtest)

    for test in tests:
        update_values(test)

def main():
    if len(sys.argv) != 3:
        print("Инструкция: python ваш_скрипт.py tests.json values.json")
        sys.exit(1)

    tests_file = sys.argv[1]
    values_file = sys.argv[2]

    with open(values_file, 'r') as values_json_file:
        values_data = json.load(values_json_file)
        values_dict = {value['id']: value['value'] for value in values_data['values']}

    with open(tests_file, 'r') as tests_json_file:
        tests_data = json.load(tests_json_file)

        update_test_values(tests_data['tests'], values_dict)

        with open('report.json', 'w') as report_json_file:
            json.dump(tests_data, report_json_file, indent=4)

        print("Файл Report.json успешно создан.")


if __name__ == '__main__':
    main()
