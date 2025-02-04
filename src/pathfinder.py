import sys
from collections import deque

sys.setrecursionlimit(10**6)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def destination(graph, src, dest, dsc, way):
    dsc[src] = True
    way.append(src)

    if src == dest:
        return True

    for i in graph[src]:
        if not dsc.get(i):
            if destination(graph, i, dest, dsc, way):
                return True
    way.pop()
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    with open(sys.argv[0]) as ipt_file:
        slns = ipt_file.readlines()
    ipt_lst = []
    i = -1
    for sln in slns:
        sln = sln.strip()
        if i == -1:
            i += 1;
        else:
            ipt_sln = sln.split()
            ipt_lst.append(ipt_sln)

    graph = {}
    dsc = {}
    for i in range(len(ipt_lst)):
        for j in range(len(ipt_lst[i])):
            adj_lst = []
            flag = ipt_lst[i][j].split('-')[0]
            if (ipt_lst[i][j].split('-')[-1] == 'S'):
                for k in range(i + 1, len(ipt_lst)):
                    if ipt_lst[k][j].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(j))
            elif (ipt_lst[i][j].split('-')[-1] == 'N'):
                for k in range(i, -1, -1):
                    if ipt_lst[k][j].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(j))
            elif (ipt_lst[i][j].split('-')[-1] == 'E'):
                for k in range(j + 1, len(ipt_lst[i])):
                    if ipt_lst[i][k].split('-')[0] != flag:
                        adj_lst.append(str(i) + '-' + str(k))
            elif (ipt_lst[i][j].split('-')[-1] == 'W'):
                for k in range(j, -1, -1):
                    if ipt_lst[i][k].split('-')[0] != flag:
                        adj_lst.append(str(i) + '-' + str(k))
            elif (ipt_lst[i][j].split('-')[-1] == 'SE'):
                for k, l in zip(range(i, len(ipt_lst)), range(j, len(ipt_lst[i]))):
                    if ipt_lst[k][l].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(l))
            elif (ipt_lst[i][j].split('-')[-1] == 'NE'):
                for k, l in zip(range(i, -1, -1), range(j, len(ipt_lst[i]))):
                    if ipt_lst[k][l].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(l))
            elif (ipt_lst[i][j].split('-')[-1] == 'SW'):
                for k, l in zip(range(i, len(ipt_lst)), range(j, -1, -1)):
                    if ipt_lst[k][l].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(l))
            elif (ipt_lst[i][j].split('-')[-1] == 'NW'):
                for k, l in zip(range(i, -1, -1), range(j, -1, -1)):
                    if ipt_lst[k][l].split('-')[0] != flag:
                        adj_lst.append(str(k) + '-' + str(l))
            graph[str(i) + '-' + str(j)] = adj_lst
            dsc[str(i) + '-' + str(j)] = False
            dest = str(i) + '-' + str(j)
    src = '0-0'

    # List to store the complete path between source and destination
    way = deque()

    if destination(graph, src, dest, dsc, way):
        print(f'Path exists from vertex {src} to vertex {dest}')
        trv = list(way)
    else:
        print(f'No path exists between vertices {src} and {dest}')
    print(trv)
    output_way = ''

    for a in range(len(trv)):
        if a == len(trv)-1:
            break
        else:
            i = int(trv[a].split('_')[-1].split('-')[0])
            j = int(trv[a].split('_')[-1].split('-')[1])
            if (ipt_lst[i][j].split('-')[-1] == 'S'):
                output_way += str(int(trv[a + 1].split('_')[-1].split('-')[0]) - i) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'N'):
                output_way += str(i - int(trv[a + 1].split('_')[-1].split('-')[0])) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'E'):
                output_way += str(int(trv[a + 1].split('_')[-1].split('-')[1]) - j) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'W'):
                output_way += str(j - int(trv[a + 1].split('_')[-1].split('-')[1])) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'SE'):
                output_way += str(int(trv[a + 1].split('_')[-1].split('-')[0]) - i) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'NE'):
                output_way += str(i - int(trv[a + 1].split('_')[-1].split('-')[0])) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'SW'):
                output_way += str(int(trv[a + 1].split('_')[-1].split('-')[0]) - i) + ipt_lst[i][j].split('-')[-1] + ' '
            elif (ipt_lst[i][j].split('-')[-1] == 'NW'):
                output_way += str(i - int(trv[a + 1].split('_')[-1].split('-')[0])) + ipt_lst[i][j].split('-')[-1] + ' '

    print(output_way)
    with open(sys.argv[2], "a") as file_object:
        file_object.write(output_way.strip())
