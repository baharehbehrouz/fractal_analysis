import pandas as pd
import math
def readF():

    try:
        # Try to read from existing file
        workbook = pd.read_csv('Fractal.csv')
    except FileNotFoundError:
        # If the file doesn't exist, create an empty dataframe
        workbook = pd.DataFrame({'Ampitude': []})
        return True,workbook

    # Check if the 'Ampitude' column is in the file
    if 'Ampitude' not in workbook.columns:
        print("The 'Ampitude' column does not exist in the file.")
        return False,workbook

    # Check if there are any other columns than 'Ampitude'
    other_cols = workbook.columns[workbook.columns != 'Ampitude']
    if len(other_cols) > 0:
        print(f"Other columns ({', '.join(other_cols)}) exist in the file, and will be ignored.")
        workbook = workbook[['Ampitude']]

    return True,workbook
# def saveF(workbook):
#     workbook.to_csv('Fractal.csv', index=False)

def GCOA(df):
    frequency_dict = {}

    # Get the column of amplitudes
    amplitude_col = df['Ampitude']
    amplitude_col = pd.to_numeric(amplitude_col, errors='coerce')

    # Count the frequency of each amplitude and store it in a dictionary
    for amplitude in amplitude_col.values:
        if not math.isnan(amplitude) and isinstance(amplitude, (int, float)):
            if amplitude > 0:
                if amplitude in frequency_dict:
                    frequency_dict[amplitude] += 1
                else:
                    frequency_dict[amplitude] = 1


    # Sort the frequency dictionary by amplitude and abundance
    sorted_dict = sorted(frequency_dict.items(), key=lambda x: (-x[0], -x[1]))

    # Create a new dataframe and copy the sorted frequency data into it
    sorted_df = pd.DataFrame(sorted_dict, columns=['Sorted Amplitude', 'Sorted Abundance'])
    sorted_df['Cumulative Total Frequency'] = sorted_df['Sorted Abundance'].cumsum()
    sorted_df['log10(Sorted Amplitude)'] = sorted_df['Sorted Amplitude'].apply(lambda x: math.log10(x))
    sorted_df['log10(Cumulative Total Frequency)'] = sorted_df['Cumulative Total Frequency'].apply(lambda x: math.log10(x))

    return sorted_df


# def main():
#     df = readF()
#     sorted_df = GCOA(df)
#     show(sorted_df)
#     saveF(sorted_df)

def saveF(workbook):
    # workbook=d+workbook
    workbook.to_csv('Fractal.csv', index=False)

def show(sorted_df):
 # Create scatter plot
    print(sorted_df)
def main():
    f,df = readF()
    # d=df
    if f is not False:
        sorted_df = GCOA(df)
        saveF(sorted_df)
        df=sorted_df

    show(df)

if __name__ == "__main__":
    main()
