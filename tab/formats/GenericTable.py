import os
import csv
import pandas as pd

def write_file(save_path, save_name, lines):
    f = open(os.path.join(save_path, save_name), "w")
    for line in lines:
        f.write(line+"\n")
    f.close()

def round_decimal_spaces(x):
    try:
        x = float(x)
        return "{:.2f}".format(x)
    except:
        return x

def get_rows_from_csv(csv_path, csv_name):
    rows = []
    with open(os.path.join(csv_path, csv_name), newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            rows.append(row)
    return rows

def bold_str(x):
    return r'\textbf{'+x+r'}'

class GenericTable:
    def __init__(self, nr_cols=5, bold_first_row=True, bold_first_col=True):
        self.nr_cols = nr_cols
        self.rows = []
        self.bold_first_row = bold_first_row
        self.bold_first_col = bold_first_col
        # Particular from different tables
        self.start = []
        self.col_str = 'c'
        self.cols_text = r"\begin{tabular}"
        self.ending = [r"\end{tabular}"]

    def add_row(self, row, decimal_points=2, bold=False):
        assert len(row) == self.nr_cols, "{} cols given for table with {} cols".format(len(row), self.nr_cols)
        row_str = [round_decimal_spaces(x) for x in row]
        if bold:
            row_str = [bold_str(x) for x in row_str]
        if self.bold_first_col:
            row_str[0] = bold_str(row_str[0])
        row_str = " & ".join(row_str)
        self.rows.append(row_str)

    def add_rows(self, *rows):
        for ix, row in enumerate(rows):
            self.add_row(row, bold=(ix == 0 and self.bold_first_row))

    def add_rows_from_csv(self, csv_path, csv_name):
        rows = get_rows_from_csv(csv_path, csv_name)
        self.nr_cols = len(rows[0])
        self.add_rows(*rows)

    def add_rows_from_csv_as_df(self, csv_path, csv_name, cols, mean_std_cols=None, filtering=None):
        df = pd.read_csv(os.path.join(csv_path, csv_name))
        orig_cols = list(df.columns)
        if filtering is not None:
            for key, value in filtering.items():
                df = df[df[key]==value]
        for mean_std_col in mean_std_cols:
            df[mean_std_col+'_MEAN'] = df[mean_std_col+'_MEAN'].apply(lambda x: round_decimal_spaces(x))
            df[mean_std_col+'_STD'] = df[mean_std_col+'_STD'].apply(lambda x: round_decimal_spaces(x))
            df[mean_std_col] = df[mean_std_col+'_MEAN'] + r" (\textpm " + df[mean_std_col+'_STD'] + ")"
        drop_cols = [col for col in orig_cols if col not in cols]
        df = df.drop(drop_cols, axis=1)
        rows = [list(df.columns)] + df.values.tolist()
        self.nr_cols = len(rows[0])
        self.add_rows(*rows)

    def save_file(self, save_path, save_name):
        # Add begin
        table = self.start
        table.append(self.cols_text+"{"+self.col_str*self.nr_cols+"}")
        # Add '\\' characters at the end of all table rows except the last
        for row_ix in range(len(self.rows)-1):
            table.append(self.rows[row_ix] + r"\\")
        table.append(self.rows[len(self.rows)-1])
        table += self.ending
        write_file(save_path, save_name, table)
