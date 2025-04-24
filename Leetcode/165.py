class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versionList1 = version1.split(".")
        versionList2 = version2.split(".")
        total_level_revisions = max([len(versionList1), len(versionList2)])
        ptr = 0
        while ptr < total_level_revisions:
            cur_revision1 = int(versionList1[ptr]) if ptr < len(versionList1) else 0
            cur_revision2 = int(versionList2[ptr]) if ptr < len(versionList2) else 0
            if cur_revision1 > cur_revision2:
                return 1
            elif cur_revision1 < cur_revision2:
                return -1
            else:
                ptr+=1
        return 0

if __name__ == "__main__":
    s = Solution()
    version1 = "0.1"
    version2 = "1.1"
    assert s.compareVersion(version1, version2) == -1

    version1 = "1.0.1"
    version2 = "1"
    assert s.compareVersion(version1, version2) == 1

    version1 = "7.5.2.4"
    version2 = "7.5.3"
    assert s.compareVersion(version1, version2) == -1