import pandas as pd
import pytest
from project import readF, GCOA
@pytest.fixture
def sample_dataframe():
    df = pd.DataFrame({'Ampitude': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    return df
def test_readF():
    # Test if the function returns a tuple
    assert isinstance(readF(), tuple)

    # Test if the function returns a tuple with two elements
    assert len(readF()) == 2

    # Test if the first element of the tuple is a boolean
    assert isinstance(readF()[0], bool)

    # Test if the second element of the tuple is a dataframe
    assert isinstance(readF()[1], pd.DataFrame)

def test_GCOA(sample_dataframe):

    # Test if the function returns a dataframe
    assert isinstance(GCOA(sample_dataframe), pd.DataFrame)

    # Test if the function returns a dataframe with 5 columns
    assert len(GCOA(sample_dataframe).columns) == 5

    # Test if the function returns a dataframe with the correct column names
    assert list(GCOA(sample_dataframe).columns) == ['Sorted Amplitude', 'Sorted Abundance', 'Cumulative Total Frequency', 'log10(Sorted Amplitude)', 'log10(Cumulative Total Frequency)']

