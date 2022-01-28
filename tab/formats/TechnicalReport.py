# Example:
#
#\begin{table}[ht]
#\centering
#\begin{tabular}{|l|l|l|}

#\hline
#Condition & n & p \\
#\hline
#A & 5 & 0.1 \\
#\hline
#B & 10 & 0.01 \\
#\hline

#\end{tabular}
#\caption{Legend (350 words max). Example legend text.}
#\end{table}

from tab.formats.GenericTable import GenericTable

class TechnicalReport(GenericTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start = [r"\begin{table}[ht]", r"\centering"]
        self.col_str = 'l'
        self.cols_text = r"{\begin{tabular}"
        self.ending = [r"\end{tabular}}", r"\caption{Legend (350 words max). Example legend text.}", r"\label{tab:table_1}", r"\end{table}"]
