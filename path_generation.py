from importlib.resources import path
from itertools import permutations
import copy

class cpg:
    def deliver_sequence(routes):
        l = len(routes[0])
        s_l = int(l/2)
        routes_copy  = copy.deepcopy(routes)
        
        for route in routes_copy:
            d = [] #list storing the index of destination
            for i in range(l):   #store the index of destination
                if route[i] >=s_l:
                    d.append(route[i])
            old_i = d[0]               
            for i in range(1,s_l):    #destination index must sort from low to high
                new_i = d[i]
                if new_i < old_i:
                    try:
                      routes.remove(route)
                    except:
                      pass
                
                old_i = new_i   
        return routes

    def take_before_deliver(routes: list):
        total_points = len(routes[0]) # 4
        total_orders = int(total_points / 2)  # the len of the orders: 2 orders
        routes_copy = copy.deepcopy(routes)

        for route in routes_copy:
             #value of head half of len indicate take, other indicate deliver, take value + len/2 is cooresponding deliver order value
            count = 0
            while count <  total_orders: #filter for take before deliver
                destination_id = count + total_orders
                start_point_index = route.index(count)
                end_point_index = route.index(destination_id) 
                if start_point_index > end_point_index:
                    try:
                        routes.remove(route)
                    except:
                        pass

                count += 1
            

        return routes       
            

    def ini_routes(a):
        l = len(a)
        routes = list(permutations(a,l))
        return routes

    def ini_a(num):
        a= []
        for i in range(num):
            a.append(i)
        return a
    def generation_path_group(num):
        path_group = cpg.ini_a(num)
        path_group = cpg.ini_routes(path_group)
        path_group = list(set(path_group))
        path_group = cpg.take_before_deliver(path_group)
        path_group = cpg.deliver_sequence(path_group)
        return path_group


