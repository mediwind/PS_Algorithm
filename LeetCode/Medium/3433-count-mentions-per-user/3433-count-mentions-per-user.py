class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        evs = []
        for typ, ts, arg in events:
            t = int(ts)
            pri = 0 if typ == "OFFLINE" else 1
            evs.append((t, pri, typ, arg))
        evs.sort()
        
        offline_until = [0] * numberOfUsers
        for t, _, typ, arg in evs:
            if typ == "OFFLINE":
                uid = int(arg)
                offline_until[uid] = t + 60
            else:  # MESSAGE
                if arg == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif arg == "HERE":
                    for i in range(numberOfUsers):
                        if t >= offline_until[i]:
                            mentions[i] += 1
                else:
                    for tok in arg.split():
                        if tok.startswith("id"):
                            uid = int(tok[2:])
                            mentions[uid] += 1
                            
        return mentions