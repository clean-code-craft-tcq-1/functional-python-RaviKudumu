Battery_range = [[0, 45], [20, 80], [-1, 0.8]]
batter_parameter = {"temperature": [0,45,"Temperature"],
                    "soc": [20,80,"Soc"],
                    "charge_rate": [0, 0.8,"Charge Rate"]}
def battery_status(battery_parameter_name):
    parameter_range = batter_parameter[battery_parameter_name["battery_parameter"]]
    low = parameter_range[0]
    high = parameter_range[1]
    value = battery_parameter_name["value"]
    if value <= low or value >= high:
        print('{} is out of range!'.format(parameter_range[2]))
        return False
    return True
if __name__ == '__main__':
  assert(battery_status({"battery_parameter": "temperature", "value": 25}) is True)
  assert (battery_status({"battery_parameter": "soc", "value": 70}) is True)
  assert (battery_status({"battery_parameter": "charge_rate", "value": 0.7}) is True)
  assert(battery_status({"battery_parameter": "temperature", "value": 50}) is False)
  assert (battery_status({"battery_parameter": "soc", "value": 85}) is False)
  assert (battery_status({"battery_parameter": "charge_rate", "value": 0}) is False)
