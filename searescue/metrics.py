def summarize(found,total,steps,energy):
    return {"victims_found":found,"victims_total":total,"discovery_rate":found/total if total else 0.0,"steps":steps,"mean_energy_remaining":sum(energy)/len(energy) if energy else 0.0}
