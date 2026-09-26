from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # map of groupings of letters where key = string of letters,
        # value is the array of words
        groupings = {}

        # we will loop through the list of strings
        # if the collection of letters in the string (sorted)
        # doesn't match any of the keys in groupings
        # then we will make a new key value pair
        # otherwise we will add it to the corresponding key

        for s in strs:
            so = "".join(sorted(s))
            if so in groupings:
                groupings[so].append(s)
            else:
                groupings[so] = [s]
        
        return list(groupings.values())
