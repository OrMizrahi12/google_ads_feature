import streamlit as st
import pandas as pd

class CSVColumnAverager:
    def __init__(self):
        self.uploaded_file = None
        self.df:pd.DataFrame = None

    def welcome_msg(self):
        st.title("Hey Tal 🤗, Let's make fun!")

    def upload_file(self):
        self.uploaded_file = st.file_uploader("First, Upload your CSV file", type=["csv"])

    def process_file(self):
        if self.uploaded_file is not None:
            # Read the uploaded CSV file
            self.df = pd.read_csv(self.uploaded_file)
            
            # Display the dataframe
            st.write("Here's your data:",self.df)
            
            # Allow user to select columns for averaging
            columns = st.multiselect("Select columns to calculate the average", self.df.columns)

            self.calculate_average(columns)
            self.calculate_non_weigted_avg(columns)

    def calculate_average(self, columns:list):
        
        self.df.dropna(inplace=True)
        
        if len(columns) == 2:
            mult:pd.DataFrame = self.df[columns[0]] * self.df[columns[1]]
            avg = mult.sum() / sum(self.df[columns[0]])
            st.write("The Real Avg: ", avg)
       
        elif len(columns) == 3: 
            mid_range:pd.DataFrame  =  (self.df[columns[1]] + self.df[columns[2]]) / 2 
            mult:pd.DataFrame = self.df[columns[0]] * mid_range
            avg = mult.sum() / sum(self.df[columns[0]])
            st.write("The Real Avg: ", avg)

    
    def calculate_non_weigted_avg(self, columns):
        self.df.dropna(inplace=True)
        if len(columns) == 3: 
            for c in columns[1:]:
                st.write(f"Teoretical Avg of {c}: ", self.df[c].mean())






        return


    def run(self):
        self.welcome_msg()
        self.upload_file()
        self.process_file()

if __name__ == "__main__":
    app = CSVColumnAverager()
    app.run()
