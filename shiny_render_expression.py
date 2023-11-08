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
