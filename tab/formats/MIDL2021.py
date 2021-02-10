
# From the MIDL Latex template, see https://2021.midl.io/
# \begin{table}[htbp]
#  % The first argument is the label.
#  % The caption goes in the second argument, and the table contents
#  % go in the third argument.
# \floatconts
#   {tab:example}%
#   {\caption{An Example Table}}%
#   {\begin{tabular}{ll}
#   \bfseries Dataset & \bfseries Result\\
#   Data1 & 0.12345\\
#   Data2 & 0.67890\\
#   Data3 & 0.54321\\
#   Data4 & 0.09876
#   \end{tabular}}
# \end{table}

from tab.formats.GenericTable import GenericTable

class MIDL2021(GenericTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start = [r"\begin{table}[htbp]", r"\floatconts", "{tab:label}%", r"{\caption{An Example Table}}%"]
        self.col_str = 'l'
        self.cols_text = r"{\begin{tabular}"
        self.ending = [r"   \end{tabular}}", r"\end{table}"]
