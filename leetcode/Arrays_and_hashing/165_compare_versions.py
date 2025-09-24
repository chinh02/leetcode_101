# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.


def compareVersion(version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n = max(len(version1),len(version2))
        if len(version1)<n:
            version1 += ['0']*(n-len(version1))
        if len(version2)<n:
            version2 += ['0']*(n-len(version2))
        for i in range(n):
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) > int(version2[i]):
                return 1
        return 0
