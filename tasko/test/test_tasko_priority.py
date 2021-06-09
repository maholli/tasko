#Test File for Priority Level Implementation
#Desired Output: All tasks execute in order of priorities, in all runs.

import tasko

async def priority_one_task():
    print("Priority one task is being done....")

async def priority_two_task():
    print("Priority two task is being done....")

async def priority_three_task():
    print("Priority three task is being done....")

async def priority_four_task():
    print("Priority four task is being done....")

async def priority_five_task():
    print("Priority five task is being done....")


#Schedule tasks with desired priority
tasko.schedule(1, priority_five_task, 5)
tasko.schedule(1, priority_one_task, 1)
tasko.schedule(1, priority_three_task, 3)
tasko.schedule(1, priority_two_task, 2)
tasko.schedule(1, priority_four_task, 4)

tasko.run()
