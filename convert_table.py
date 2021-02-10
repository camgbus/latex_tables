
from tab.formats.MIDL2021 import MIDL2021

csv_path = 'test'

csv_name = 'dummy_table.csv'
table = MIDL2021()
table.add_rows_from_csv(csv_path=csv_path, csv_name=csv_name)
table.save_file(save_path=csv_path, save_name='dummy_table.txt')

csv_name = 'dummy_table_mean_std.csv'
table = MIDL2021()
table.add_rows_from_csv_as_df(csv_path=csv_path, csv_name=csv_name, cols=['Column A'], mean_std_cols = ['Column B'])
table.save_file(save_path=csv_path, save_name='dummy_table_mean_std.txt')
