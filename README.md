# PuDatabase
A useless database, for fun, it will be updated continuously.



In this program, "/" is the path separator, and "." is the root path.

In this program, each path can store a piece of information. The information is enclosed in triple single quotes, such as: '''example'''



Currently supported command statements:

①[path] read

This can read the information stored in a path.

②[path] set [info]

This can store information in a path.

③[path] mkdir [directory name]

This can create a directory in an existing path.

④[path] ls [method]

This can list the sub-paths under a path

	0-List the next-level path name
	
	1-List the next-level full path name
	
	2-List all sub-path path names
	
	3-List all sub-path full path names
	
⑤[path] del

This can delete a path and its subpaths