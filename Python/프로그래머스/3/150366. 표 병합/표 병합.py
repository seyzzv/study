def solution(commands):
    parent = [i for i in range(2500)]
    values = [""] * 2500

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    def get_index(r, c):
        return (int(r) - 1) * 50 + (int(c) - 1)

    result = []

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == "UPDATE":
            if len(parts) == 4:
                r, c, val = parts[1], parts[2], parts[3]
                idx = get_index(r, c)
                root = find(idx)
                values[root] = val
            else:
                val1, val2 = parts[1], parts[2]
                for i in range(2500):
                    if find(i) == i and values[i] == val1:
                        values[i] = val2

        elif cmd == "MERGE":
            r1, c1, r2, c2 = parts[1], parts[2], parts[3], parts[4]
            idx1 = get_index(r1, c1)
            idx2 = get_index(r2, c2)
            
            root1 = find(idx1)
            root2 = find(idx2)

            if root1 != root2:
                val1 = values[root1]
                val2 = values[root2]

                union(root1, root2)
                
                if val1:
                    values[root1] = val1
                elif val2:
                    values[root1] = val2
                else:
                    values[root1] = ""
                    
                values[root2] = ""

        elif cmd == "UNMERGE":
            r, c = parts[1], parts[2]
            idx = get_index(r, c)
            root = find(idx)
            original_val = values[root]

            merged_cells = [i for i in range(2500) if find(i) == root]

            for cell in merged_cells:
                parent[cell] = cell
                values[cell] = ""

            values[idx] = original_val

        elif cmd == "PRINT":
            r, c = parts[1], parts[2]
            idx = get_index(r, c)
            root = find(idx)
            val = values[root]

            result.append(val if val else "EMPTY")

    return result