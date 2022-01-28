
from tab.formats.TechnicalReport import TechnicalReport

csv_path = 'test'

csv_name = 'dummy_table.csv'
table = TechnicalReport()
table.add_rows_from_csv(csv_path=csv_path, csv_name=csv_name)
table.save_file(save_path=csv_path, save_name='dummy_table.txt')

csv_name = 'dummy_table_mean_std.csv'
table = TechnicalReport()
table.add_rows_from_csv_as_df(csv_path=csv_path, csv_name=csv_name, mean_std_cols = ['Column B'])
table.save_file(save_path=csv_path, save_name='dummy_table_mean_std.txt')
