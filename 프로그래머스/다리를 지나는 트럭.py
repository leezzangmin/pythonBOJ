# 다리를 건너는데 필요한 시간이 bridge_length

def solution(bridge_length, weight, truck_weights):
    





    return time

#print(solution(2,10,[7,4,5,6]))
#print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))


def solution2(bridge_length, weight, truck_weights):
    truck_on_bridge=[[truck_weights[0],0]]
    weight_sum=truck_weights[0]
    i=1
    time=1
    lt=len(truck_weights)
    while truck_on_bridge or i<lt:
        if i<lt and weight>weight_sum+truck_weights[i] and len(truck_on_bridge)<bridge_length:
            truck_on_bridge.append([truck_weights[i],0])
            i+=1
        
        for idx,(truck, duration) in enumerate(truck_on_bridge):
            truck_on_bridge[idx][1]+=1
            if truck_on_bridge[idx][1]==bridge_length:
                truck_on_bridge.pop(idx)
                weight_sum-=truck
        time+=1  
        #print(truck_on_bridge,time)
    #print(truck_on_bridge)
    return time