class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        폴더 경로는 항상 "/"로 시작하지만,
        "/a"가 있으면 "/a/..."로 시작하는 모든 경로는 "/a"의 서브폴더로 간주해 결과에서 제외한다.
        즉, "/a"가 부모라면 "/a/b", "/a/b/c" 등은 모두 "/a"의 하위 폴더로 처리되어 남지 않는다.
        "/"로 시작하는 것은 모든 경로가 동일하므로, "/" 뒤의 구조(슬래시로 구분된 폴더명)로 부모-자식 관계를 판단한다.
        '''
        folder.sort()
        res = list()
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res