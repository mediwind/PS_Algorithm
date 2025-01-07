class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = list()
        for op in operations:
            if op.isdigit() or op[0] == '-':
                record.append(int(op))
            else:
                if op == '+':
                    tmp = record[-1] + record[-2]
                    record.append(tmp)
                elif op == 'D':
                    tmp = record[-1] * 2
                    record.append(tmp)
                else:
                    record.pop()
        
        if not record:
            return 0

        return sum(record)
