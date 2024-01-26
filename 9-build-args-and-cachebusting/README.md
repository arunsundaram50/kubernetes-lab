To optimize build time, whereever possible
1) do the expensive (ex: large file copy) operations in the beginning
2) perform the often modified file copy later
this way docker CACHING can be taken full advantage

