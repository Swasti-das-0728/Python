class Solution:
    def areIsomorphic(self, s1, s2):
        # If lengths are not equal, they cannot be isomorphic
        if len(s1) != len(s2):
            return False
        
        map_s1_to_s2 = {}
        map_s2_to_s1 = {}
        
        for ch1, ch2 in zip(s1, s2):
            # Check mapping from s1 -> s2
            if ch1 in map_s1_to_s2 and map_s1_to_s2[ch1] != ch2:
                return False
            
            # Check mapping from s2 -> s1
            if ch2 in map_s2_to_s1 and map_s2_to_s1[ch2] != ch1:
                return False
            
            map_s1_to_s2[ch1] = ch2
            map_s2_to_s1[ch2] = ch1
            
        return True