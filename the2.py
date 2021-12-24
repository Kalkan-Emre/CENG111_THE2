#
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() here. Check before submitting

import math
import random
from evaluator import *   # get_data() will come from this import

universal_state = get_data()[6]

def new_move():
    global universal_state
    
    M,N = get_data()[0],get_data()[1]
    distance_limit ,K = get_data()[2],get_data()[3]
    mask_constant,direction_prob = get_data()[4],get_data()[5]
    
    def new_table(person):     # Defines new directions according to last move
        
        last_move = person[1]
        coordinates = person[0]
        coordinates_list = list(coordinates)
        x = coordinates_list[0]
        y = coordinates_list[1]
        
        
        if last_move == 0:
            forward = (x,y+1)
            forward_left = (x+1,y+1)
            forward_right = (x-1,y+1)
            left = (x+1,y)
            right = (x-1,y)
            backward_left = (x+1,y-1)
            backward_right = (x-1,y-1)
            backward = (x,y-1)
            
        if last_move == 1:
            forward = (x-1,y+1)
            forward_left = (x,y+1)
            forward_right = (x-1,y)
            left = (x+1,y+1)
            right = (x-1,y-1)
            backward_left = (x+1,y)
            backward_right = (x,y-1)
            backward = (x+1,y-1)
            
                        
        if last_move == 2:
            forward = (x-1,y)
            forward_left = (x-1,y+1)
            forward_right = (x-1,y-1)
            left = (x,y+1)
            right = (x,y-1)
            backward_left = (x+1,y+1)
            backward_right = (x+1,y-1)
            backward = (x+1,y)
            
        
        if last_move == 3:
            forward = (x-1,y-1)
            forward_left = (x-1,y)
            forward_right = (x,y-1)
            left = (x-1,y+1)
            right = (x+1,y-1)
            backward_left = (x,y+1)
            backward_right = (x+1,y)
            backward = (x+1,y+1)
            
            
        if last_move == 4:
            forward = (x,y-1)
            forward_left = (x-1,y-1)
            forward_right = (x+1,y-1)
            left = (x-1,y)
            right = (x+1,y)
            backward_left = (x-1,y+1)
            backward_right = (x+1,y+1)
            backward = (x,y+1)
            
            
        if last_move == 5:
            forward = (x+1,y-1)
            forward_left = (x,y-1)
            forward_right = (x+1,y)
            left = (x-1,y-1)
            right = (x+1,y+1)
            backward_left = (x-1,y)
            backward_right = (x,y+1)
            backward = (x-1,y+1)
            
            
        if last_move == 6:
            forward = (x+1,y)
            forward_left = (x+1,y-1)
            forward_right = (x+1,y+1)
            left = (x,y-1)
            right = (x,y+1)
            backward_left = (x-1,y-1)
            backward_right = (x-1,y+1)
            backward = (x-1,y)
            
            
        if last_move == 7:
            forward = (x+1,y+1)
            forward_left = (x+1,y)
            forward_right = (x,y+1)
            left = (x+1,y-1)
            right = (x-1,y+1)
            backward_left = (x,y-1)
            backward_right = (x-1,y)
            backward = (x-1,y-1)
            
        
        table = [forward, forward_left, forward_right, left, right, backward_left, backward_right, backward]
        
        return table
    
      
    def probability_of_move(person):      # Finds new location of a person 
        
        global universal_state
        
        index_of_person = universal_state.index(person)
        
        people = universal_state[:index_of_person] + universal_state[index_of_person+1:]
        
        old_coordinate = person[0]
        
        nonlocal direction_prob
        
        green = direction_prob/2
        yellow = direction_prob/8
        blue = (1-direction_prob-(direction_prob)**2)/2
        purple = ((direction_prob)**2)*(2/5)
        gray = ((direction_prob)**2)*(1/5)
        
        direction_table = ["forward","forward_right","right","backward_right","backward","backward_left","left","forward_left"]
        
        weight_list = [green,yellow,blue,purple,gray,purple,blue,yellow]
        
        direction = random.choices(direction_table, weights = weight_list) 

        change = False

        if direction==["forward"]:
            new_coordinate = new_table(person)[0]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
                
        if direction==["forward_left"]:
            new_coordinate = new_table(person)[1]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
            
        if direction==["forward_right"]:
            new_coordinate = new_table(person)[2]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
                
        if direction==["left"]:
            new_coordinate = new_table(person)[3]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
        
        if direction==["right"]:
            new_coordinate = new_table(person)[4]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
            
        if direction==["backward_left"]:
            new_coordinate = new_table(person)[5]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
            
        if direction==["backward_right"]:
            new_coordinate = new_table(person)[6]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
        
        if direction==["backward"]:
            new_coordinate = new_table(person)[7]
            if is_empty(people,new_coordinate):
                person[0] = new_coordinate
                change = True
                
                
                

        x_difference = new_coordinate[0] - old_coordinate[0]
        y_difference = new_coordinate[1] - old_coordinate[1]
        
        c_d = (x_difference,y_difference) #Coordinate difference

        if change:   # Change last move, if person moves
            if c_d==(0,1):
                person[1] = 0
            
            if c_d==(-1,1):
                person[1] = 1
            
            if c_d==(-1,0):
                person[1] = 2
            
            if c_d==(-1,-1):
                person[1] = 3
            
            if c_d==(0,-1):
                person[1] = 4
            
            if c_d==(1,-1):
                person[1] = 5
            
            if c_d==(1,0):
                person[1] = 6
            
            if c_d==(1,1):
                person[1] = 7
        
        return person
        
    
    def is_empty(people,new_coordinate):       # Checks whether a location is available to go
        
        nonlocal M
        nonlocal N

        coordinates_list = []
        
        for person in people:
            coordinates_list.append(person[0])
        
        for a_coordinate in coordinates_list:
            if a_coordinate == new_coordinate:
                return False
            
        if new_coordinate[0] >= N or new_coordinate[1] >= M or new_coordinate[0] < 0 or new_coordinate[1] < 0 :
            return False
        
        return True
    
   
    def is_infected(person,other_people):     # Determines individual's new infection status
        nonlocal distance_limit
        nonlocal mask_constant
        nonlocal K
        
        coordinate_of_person = person[0]
        x = coordinate_of_person[0]
        y = coordinate_of_person[1]

        other_coordinates = []

        for a_person in other_people:
            other_coordinates.append(a_person[0])

        
        change = False    
        for ele in other_coordinates:    # Porbability calculations
            euclidian_distance = (((x-ele[0])**2) + ((y-ele[1])**2))**(1/2)
            if euclidian_distance <= distance_limit:
                infection_prob = min(1,(K/(euclidian_distance**2)))
            else:
                infection_prob = 0
                
                
            compare_person_index = other_coordinates.index(ele) 
            compare_person_info = other_people[compare_person_index]   # Gives information of person who is being compared
            
                
            if person[2] == "masked" and compare_person_info[2] == "masked":
                infection_prob = infection_prob / (mask_constant**2)
            if person[2] == "masked" :
                infection_prob = infection_prob / mask_constant            
            if compare_person_info[2] == "masked":
                infection_prob = infection_prob / mask_constant


            if compare_person_info[3]=="infected" and person[3]=="notinfected":
                if infection_prob!=0:
                    infection_status = random.choices(["infected","notinfected"],weights= [infection_prob,(1-infection_prob)])
                    change = True
                    if infection_status == ["infected"]:
                        person[3] = "infected"
            elif change:  # Continues to infection calculations as a person is not infected in that time frame
                if compare_person_info[3]=="infected":
                    if infection_prob!=0:
                        infection_status = random.choices(["infected","notinfected"],weights= [infection_prob,(1-infection_prob)])
        
        return person
           
    
    for i in range(len(universal_state)):    # Find new moves for every person
        universal_state[i] = probability_of_move(universal_state[i])
       
    state_at_this_moment = []
    other_people_list = []

    for k in range(len(universal_state)):  # Keeps the current state
        each_person = universal_state[k].copy()
        state_at_this_moment += [each_person]

    for i in range(len(state_at_this_moment)):  # Creates lists which excludes one individual 
        new_other_people = state_at_this_moment[:i] + state_at_this_moment[i+1:]
        other_people_list += [new_other_people]

    for i in range(len(universal_state)):   
        universal_state[i] = is_infected(universal_state[i],other_people_list[i])

    return universal_state