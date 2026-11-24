def sweep_target(agent,step,width,height):
    offset=0 if agent.kind=="drone" else width//3
    return ((step+offset)%width,(step//width+(0 if agent.kind=="drone" else height//2))%height)
