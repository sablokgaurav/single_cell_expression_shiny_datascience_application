# single_cell_expression_shiny_expression_datascience_visual

a combined expression and datascience approach based on shiny to look at the expression plots plus the sequence intervals using shiny. I havent added much of the templating but the information you can plot from the same. You can use this for the expression datasets coming from the rna-seq, metagenome expression, bacterial expression and others You can plot also your expression with any other variables such as bins and method variables. This package is still in development. This code is in development and it will make a single cell or expression summation from the single cell or any expression datasets. Just you have to put the expression file in the same folder. 

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# a shiny python app for the expression or the counts coming from the 
# expression datasets or the single cell genomics. 
from pathlib import Path
import pandas as pd
from shiny import App, render, ui
app_ui = ui.page_fixed(
    ui.h2("single cell expression or any expression summary counts"),
        ui.markdown("an example view to how to apply the dashboard using the \
                     shiny python for the single cell analysis. You can add as many functions \
                     you want"),
        ui.output_table("table"), 
        ui.output_plot("plot")   
)
def server(input, output, session):
    @output
    @render.table
    def table():
        infile = Path(__file__).parent / "expression.csv"
        df = pd.read_csv(infile, sep = "\t")
        return df.head(n=10) 
    @output     
    @render.plot
    def plot():
        infile = Path(__file__).parent / "expression.csv"
        df = pd.read_csv(infile, sep = "\t")
        control = pd.DataFrame(df.iloc[::,[2,3,4]].apply(sum, axis=1), columns = ["control"])
        first = pd.DataFrame(df.iloc[::,[2,3,4]].apply(sum, axis=1), columns = ["first"])
        combined = pd.concat([control, first], axis = 1)
        return control.head().plot.bar(), first.head().plot.bar()
app = App(app_ui, server)
```

Gaurav Sablok \
ORCID: https://orcid.org/0000-0002-4157-9405 \
WOS: https://www.webofscience.com/wos/author/record/C-5940-2014 \
RubyGems Published: https://rubygems.org/profiles/sablokgaurav \
Python Packages Published : https://pypi.org/user/sablokgaurav/ \
