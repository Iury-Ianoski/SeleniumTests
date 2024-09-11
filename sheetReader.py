import pandas as pd
from typing import List, Union

def sheetReader() -> List[Union[int, str]]:

    xlsx = pd.read_excel("challenge.xlsx")
    array = xlsx.to_numpy()

    return array

if __name__ == "__main__":
   array = sheetReader()
   a = 0
   b = 0
   print(array[a][b])