class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26            # for a - z

            for c in s:
                # checks 
                count[ord(c) - ord("a")] += 1       # calculate frequency of each character
            
            # print(count)

            results[tuple(count)].append(s)

        return list(results.values())
        
        
        
        
        
        
        
        
        
        
        # counter_list = []
        # for s in strs:
        #     counter_list.append(Counter(s))
            
        
        # # print(counter_list)
        
        # unique_counters = set(tuple(counter_list))

        # # for counter in counter_list:
        # #     if counter not in unique_counters:
        # #         unique_counters.append(counter)

        # # print(unique_counters)
        
        # results = []
        # for counter in unique_counters:
        #     counter_results = []

        #     for s in strs:
        #         if Counter(s) == counter:
        #             counter_results.append(s)

        #     # for i in range(len(strs)):
        #     #     if counter == counter_list[i]:
        #     #         counter_results.append(strs[i])

        #     results.append(counter_results)

        # # print(results)

        # return results
        
        
        
        
        
        
        
        
        
        
        
        # # Creating the counter for each string in the list
        # counter_list = []
        
        # for string in strs:
        #     counter_list.append(Counter(string))

        # print(counter_list)

        # output_list = []

        # seen_words = set()

        # for i in range(len(counter_list)):
        #     temp_list = []
        #     # temp_list.append(strs[i])
        #     # print(temp_list)
        #     print(f"Current i: {strs[i]}")
        #     for j in range(i, len(counter_list)):
        #         print("Current j:", strs[j])
        #         if counter_list[i] == counter_list[j]:
        #             print(i, j, (strs[i], strs[j]))
        #             if strs[j] not in seen_words:
        #                 print("this is running")
        #                 temp_list.append(strs[j])
        #                 print(temp_list)
        #                 # seen_words.add(strs[j])
        #             # if strs[j] == "":
        #             #     temp_list.append(strs[j])

        #     if temp_list:
        #         output_list.append(temp_list)
        #     print(output_list)

        # return output_list
