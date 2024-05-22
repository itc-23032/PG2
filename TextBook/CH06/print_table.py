def print_table(table_data):
    col_widths = [max(len(item) for item in col) for col in table_data]

    for row in range(len(table_data[0])):
        for col in range(len(table_data)):
            print(table_data[col][row].rjust(col_widths[col]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
