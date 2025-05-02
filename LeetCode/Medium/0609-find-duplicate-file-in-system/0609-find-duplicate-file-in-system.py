class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = collections.defaultdict(list)

        for path_info in paths:
            parts = path_info.split(' ')
            if not parts:
                continue
            
            directory_path = parts[0]
            file_details = parts[1:]

            for file_detail in file_details:
                try:
                    idx_open = file_detail.index('(')
                    
                    file_name = file_detail[:idx_open]
                    
                    content = file_detail[idx_open + 1:-1] 
                    
                    full_path = directory_path + '/' + file_name
                    
                    content_map[content].append(full_path)
                except ValueError:
                    continue 

        result = list()
        for paths_list in content_map.values():
            if len(paths_list) >= 2:
                result.append(paths_list)

        return result