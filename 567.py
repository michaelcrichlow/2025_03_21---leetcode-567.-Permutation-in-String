def checkInclusion_00(s1: str, s2: str) -> bool:
    permutations = get_permutations(s1)
    for val in permutations:
        if val in s2:
            return True
    return False


def checkInclusion_01(s1: str, s2: str) -> bool:
    # instead of getting all the permutations, you can use a dictionary
    # to map the values to how many times the value appears
    local_dict = {val: s1.count(val) for val in s1}
    print(local_dict)

    left = 0
    right = len(s1)

    while right <= len(s2):
        __val = s2[left:right]
        test_dict = {val: s2[left:right].count(val) for val in s2[left:right]}
        if test_dict == local_dict:
            return True
        left += 1
        right += 1
    
    return False


# 1.) Testcases passed!
# 2.) Solution accepted!
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1)>len(s2):
        return False

    s1count = [0]*26
    s2count = [0]*26
    
    left = 0
    right = 0

    while(right<len(s1)):
        s1count[ord(s1[right]) - ord('a')] +=1
        s2count[ord(s2[right]) - ord('a')] +=1
        right +=1
    right -=1

    while(right<len(s2)):
        if s1count==s2count:
            return True

        right +=1
        if(right!=len(s2)):
            s2count[ord(s2[right]) - ord('a')] +=1
        s2count[ord(s2[left]) - ord('a')] -=1
        left +=1
    
    return False

def main() -> None:
    # print(checkInclusion(s1 = "ab", s2 = "eidbaooo")) # true original
    # print(checkInclusion(s1 = "ab", s2 = "ooba")) # true
    # print(checkInclusion(s1 = "ab", s2 = "eidboaoo")) # false
    print(checkInclusion(s1 = "adc", s2 = "dcda")) # true



if __name__ == '__main__':
    main()
