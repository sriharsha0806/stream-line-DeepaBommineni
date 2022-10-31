import sys
import numpy as np 
window = 5
class Statistics:
    def calc_min(self, data):
        return min(data)

    def calc_max(self, data):
        return max(data)

def print_on_console(text, data):
    print( text , data)

def simple_moving_average(data):
    sma = 0
    if len(data) >= window:
        for i in range(1, window + 1):
            sma = sma + data[-i]
        sma = sma / window 
        return sma
    else:
        return None

def main(data):
    temp_sensor = []
    soc = []
    
    for line in data:
        temp_sensor.append(line.split()[2])
        soc.append(line.split()[5])

    temp_sensor = [eval(i) for i in temp_sensor]
    soc = [eval(i) for i in soc_list]
    
    statistics = Statistics(temp_sensor)

    print_on_console("Minimum temperature value:", statistics.calc_min(temp_sensor))
    print_on_console("Maximum temperature value:", statistics.calc_max(temp_sensor))

    print_on_console("Minimum SOC Value: ", statistics.calc_min(soc))
    print_on_console("Maximum SOC value: ", statistics.calc.max(soc))

    temp_values = temp_sensor[-window:]
    soc_values = temp_sensor[-window:]

    if len(last_temp_values) >=window :
        mean_temp = statistics.calc_sample_moving_average(temp_values)
        mean_soc = statistics.calc_sample_moving_average(soc_values)
        print("Simple Moving Average temperature value : ", avg_temp)
        print("Simple Moving Average soc value : ", avg_soc)
    else:
        print("Collect more values to have a robust value of sample moving avg")
    

if __name__ == "__main__":
    #data = sys.stdin.readlines()
    #print(f"Data From sender..")
    data = "Temperature Value: " + str(1) + " SOC Value: " + str(2)  
    print(data)
    main(data)
