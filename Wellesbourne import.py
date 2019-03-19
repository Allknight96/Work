import os
import pandas as pd

var = r"H:\OPERATIONS\Contracts\2018 Contracts\1UK0001368 Gericke\1UK0001407 Sainsburys Trial MCD155\Sainsbury trial data\TREND Data"
dirs = os.listdir(var)


Names = {
    "AHU1SA"
    "Dehum_Return_Humidity"
    "Dehum_Return_Temperature"
    "Dehum_Supply_Humidity"
    "Dehum_Supply_Temperature"
    "Outside_Air_Temperature"
    "Outside_Humidity"
    "S1CA1_Humidity"
    "S1CA1_Space_Temperature"
    "S1CA2_Humidity"
    "S1CA2_Space_Temperature"
    "S1GM1_Space_Temperature"
    "S1SA1_Humidity"
    "S1SA1_Space_Temperature"
    "S1SA2_Humidity"
    "S1SA2_Space_Temperature"
    "S1SF1_Space_Temperature"
    "S1SF2_Space_Temperature"
        }

#for table in tables:
#    print(table)
    
#for filename in dirs:
#    
i = 0
for table in Names:
    table = pd.read_excel (os.path.join(var, dirs[1]), sheet_name=i)
    i = i+1
