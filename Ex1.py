import csv
import json
import sys

from Building import Building
from Elevator import Elevator
from ElevatorCall import ElevatorCall


def create_building_from_file(file_name):
    with open(file_name) as file:
        json_building = json.load(file)
        file.close()
    elevators = create_elevator_list_from_json(json_building["_elevators"])
    new_building = Building(min_floor=json_building["_minFloor"],
                            max_floor=json_building["_maxFloor"],
                            elevators=elevators)
    return new_building


def create_elevator_list_from_json(elevators):
    list_of_elevators = []
    for elevator in elevators:
        new_elevator = Elevator(
            elevator_id=elevator["_id"],
            speed=elevator["_speed"],
            min_floor=elevator["_minFloor"],
            max_floor=elevator["_maxFloor"],
            close_time=elevator["_closeTime"],
            open_time=elevator["_openTime"],
            start_time=elevator["_startTime"],
            stop_time=elevator["_stopTime"]
        )
        list_of_elevators.append(new_elevator)
    return list_of_elevators


def create_list_of_call_from_csv(file_name):
    call_list = []
    csv_call_list = []
    with open(file_name) as file:
        call_list_as_csv_reader = csv.reader(file)
        for call in call_list_as_csv_reader:
            csv_call_list.append(call)

    call_parameters = {"time": 1, "source": 2, "destination": 3, "allocated_to_elevator": 5}

    for call in csv_call_list:
        new_call = ElevatorCall(
            time_of_call=float(call[call_parameters["time"]]),
            source=int(call[call_parameters["source"]]),
            destination=int(call[call_parameters["destination"]]),
            allocated_to_elevator=int(call[call_parameters["allocated_to_elevator"]])
        )
        call_list.append(new_call)
    return call_list


def write_to_csv(list_of_calls, file_name):
    e = "Elevator call"
    csv_list_of_calls = []
    for call in list_of_calls:
        string_list = [
            e,
            str(call.time_of_call),
            str(call.source),
            str(call.destination),
            '0',
            str(call.allocated_to_elevator)]
        csv_list_of_calls.append(string_list)
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_list_of_calls)


def offline_algorithm(json_building_file_name, csv_input_file_name, csv_output_file_name):
    building = create_building_from_file(json_building_file_name)
    list_of_calls = create_list_of_call_from_csv(csv_input_file_name)

    weights = [0] * building.number_of_elevators()

    total_speeds = 0
    index = 0
    fastest_elevator = building.elevators[index]
    for elevator in building.elevators:
        if elevator.speed > fastest_elevator.speed:
            fastest_elevator = elevator
            index = elevator.elevator_id
        total_speeds += elevator.speed
    for elevator in building.elevators:
        weights[elevator.elevator_id] = elevator.speed/total_speeds

    original_length = len(list_of_calls)
    for elevator in building.elevators:
        number_of_calls = int(original_length * weights[elevator.elevator_id])
        step = int(len(list_of_calls)/number_of_calls)
        i = 0
        while i < len(list_of_calls):
            if list_of_calls[i].allocated_to_elevator == -1:
                list_of_calls[i].allocated_to_elevator = elevator.elevator_id
                i += step
            else:
                i += 1
    for i in list_of_calls:
        if i.allocated_to_elevator == -1:
            i.allocated_to_elevator = index

    write_to_csv(list_of_calls, csv_output_file_name)


def main():
    files = {"json_building_file_name": 0, "csv_input_file_name": 1, "csv_output_file_name": 2}
    file_names = sys.argv[1:]
    offline_algorithm(file_names[files["json_building_file_name"]],
                      file_names[files["csv_input_file_name"]],
                      file_names[files["csv_output_file_name"]])
    #offline_algorithm("B5.json", "Calls_d.csv", "outB5D.csv")


if __name__ == '__main__':
    main()