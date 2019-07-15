def longestCommonPrefix(list1):
    longest_pre = ""
    if not list1: return longest_pre
    shortest_str = min(list1, key=len)
    for i in range(len(shortest_str)):
        if all([x.startswith(shortest_str[:i+1]) for x in list1]):
            longest_pre = shortest_str[:i+1]
        else:
            break
    return longest_pre

if __name__ == '__main__':
    var = int(input())
    list1 = []
    for i in range(var):
        var = input()
        list1.append(var)
    print(longestCommonPrefix(list1))
