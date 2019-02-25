import time

class Column:
    def __init__(self, nb_floors, nb_elevators):
        print('CREATE Column')
        self.nb_Floor = nb_floors
        self.nb_Elevator = nb_elevators
        self.elevators_list = []
        
        print(self.nb_Elevator)
        for i in range(self.nb_Elevator):
            i = Elevator()
            self.elevators_list.append(i)
        

class Elevator:
    def __init__(self):
        self.Status = 'IDLE'
        self.current_floor = 1
        self.Direction = ''
        self.floor_list = []

        
    def open_door(self):
        print('OpenDoor')   
    def close_door(self):
        print('CloseDoor')         
        

class Controller:
    def __init__(self, nb_Floor, nb_Elevator):
        print('CREATE Controller')
        self.column = Column(nb_Floor, nb_Elevator)

        
    # request button !!!outside!!! elevator
    def RequestElevator(self, floor_no, Direction):        
        best_elevator = self.find_best_elevator(floor_no, Direction)
        print(best_elevator)
        best_elevator.floor_list.append(floor_no)
        self.operate_elevator(best_elevator, floor_no)
        return best_elevator

    # Request button !!!inside!!! elevator 
    def RequestFloor(self, elevator, floor_no):
        elevator.floor_list.append(floor_no)
        self.operate_elevator(elevator, floor_no)


    # move Up and down
    def Elevator_move(self, current_Floor, RequestElevator, Elevator, Column):
        for Elevator in Column.elevators_list:                
            while current_Floor != RequestElevator:
                if current_Floor > RequestElevator:
                    RequestElevator -=1
                elif current_Floor < RequestElevator:
                    RequestElevator +=1


    #   display floor info 1,2,3,4... and make the elevator moove
    def move_show(self, Elevator):
        if Elevator.floor_list[0] > Elevator.current_floor:
            while Elevator.floor_list[0] != Elevator.current_floor:
                Elevator.current_floor += 1 
                print('current floor', Elevator.current_floor)
                Elevator.Status = "MoveUp"
                print("Elevator State:", Elevator.Status)
                time.sleep(1)
            print("Elevator arrived to floor:", Elevator.current_floor)

        elif Elevator.floor_list[0] < Elevator.current_floor:
            while Elevator.floor_list[0] != Elevator.current_floor:
                Elevator.current_floor -= 1 
                print('current floor', Elevator.current_floor)
                Elevator.Status = "MoveDown"                
                print("Elevator State:", Elevator.Status)
                time.sleep(1)
            print("Elevator arrived to floor:", Elevator.current_floor)
        else:
            print("Elevator has arrived to floor:", Elevator.current_floor)
            Elevator.Status = "Stop"

    
    # operate the elavater doors and movement with move_show
    def operate_elevator(self, best_elevator, floor_no):
        print('operate_elevator', best_elevator, floor_no) 
        print(best_elevator)

        controller.move_show(best_elevator)
        best_elevator.open_door()
        time.sleep(1)
        best_elevator.close_door()
        time.sleep(1)


    #least busy elevator calcul

    # def Find_least_busy(self, Elevator, Column):
    #     for Elevator in self.column.elevators_list:
    #         length_list = len(Elevator.floor_list)
    #         for index in self.column.elevators_list:
    #             if len(index.floor_list) < length_list:
    #                 length_list = len(index.floor_list)
    #                 Column[index]

    #     return Column[index]


    # #nearest elevator calcul !!!!!
    def nearest_elevator(self, floor_no):
        reference_gap = 1000
        nearestElevator = None
        for Elevator in self.column.elevators_list:
            calculate_gap = abs(floor_no - Elevator.current_floor)
            if calculate_gap <= reference_gap:
                reference_gap = calculate_gap
                nearestElevator = Elevator
        return nearestElevator



    # find best elevator 
    def find_best_elevator(self, floor_no, Direction):
        print('find_best_elevator', floor_no, Direction)
        print(self.column.elevators_list)
        reference_elevator = self.column.elevators_list[0]
        goodElevator = None
        for elevator_item in self.column.elevators_list:
            elevator_item = reference_elevator

            if floor_no == elevator_item.current_floor and elevator_item.Direction == elevator_item.Direction and elevator_item.Status == "Stopped":                
                elevator_item = reference_elevator
                goodElevator = elevator_item

            elif floor_no == elevator_item.current_floor and elevator_item.Status == "IDLE":                
                elevator_item = reference_elevator
                goodElevator = elevator_item

            elif floor_no > elevator_item.current_floor and elevator_item.Status == "Up" or "Down" or "Stopped" and elevator_item.Direction == "Up":
                goodElevator = self.nearest_elevator(floor_no)
                
            elif floor_no < elevator_item.current_floor and elevator_item.Status == "Up" or "Down" or "Stopped" and elevator_item.Direction == "Down":
                goodElevator = self.nearest_elevator(floor_no)
               
            elif floor_no != elevator_item.current_floor and elevator_item.Status == "IDLE":
                elevator_item = reference_elevator
                goodElevator = elevator_item

        return goodElevator   
            

        # Find_least_busy = self.Find_least_busy
        # return Find_least_busy
                
        




# Scenario 1:
# elevator 1 floor 2
# elevator 2 floor 6
# first user on floor 3 request for 7
print('scenario1')
controller = Controller(10, 2)
controller.column.elevators_list[0].current_floor = 2
controller.column.elevators_list[1].current_floor = 6
elevator = controller.RequestElevator(3, "UP")
controller.RequestFloor(elevator, 7)
print(controller)


# Scenario 2:

print('scenario2')
controller = Controller(10, 2)
controller.column.elevators_list[0].current_floor = 10
controller.column.elevators_list[1].current_floor = 3
elevator = controller.RequestElevator(1, "UP")
elevator = controller.RequestElevator(3, "UP")
controller.RequestFloor(elevator, 6)
controller.RequestFloor(elevator, 5)
print(controller)


# Scenario 3:

print('scenario3')
controller = Controller(10, 2)
controller.column.elevators_list[0].current_floor = 10
controller.column.elevators_list[1].current_floor = 3
elevator = controller.RequestElevator(10, "UP")
elevator = controller.RequestElevator(3, "UP")
controller.RequestFloor(elevator, 3)
controller.RequestFloor(elevator, 2)
print(controller)


