# Example CLI Session Output

The following is a real CLI session captured while running the task manager.
It demonstrates task creation, status updates, filtering, sorting, and metrics.


TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  1
Title:  Evening walk
Description:  One hour walk to reset and reflect
Task created successfully.

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  1
Title:  Organize notes
Description:  Clean and structure study notes and resume points
Task created successfully.

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  1
Title:  Prepare interview answers
Description:  Go through HR questions and project explanations
Task created successfully.

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  2
Filter by status? (leave empty for all):  

Listing 3 tasks:
ID        : f0c2c5ba-52f0-4779-90d7-f931d1a85af3
Title     : Prepare interview answers
Description: Go through HR questions and project explanations
Status    : todo
Created At: 2026-02-01 15:43:29
Updated At: 2026-02-01 15:43:29


ID        : fc303af9-2482-4267-942b-f2b810d6e7c7
Title     : Organize notes
Description: Clean and structure study notes and resume points
Status    : todo
Created At: 2026-02-01 15:42:54
Updated At: 2026-02-01 15:42:54


ID        : b3945082-57c3-4294-9f9c-194c2a02a5bb
Title     : Evening walk
Description: One hour walk to reset and reflect
Status    : todo
Created At: 2026-02-01 15:41:50
Updated At: 2026-02-01 15:41:50



TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  3
Task ID:  b3945082-57c3-4294-9f9c-194c2a02a5bb
Options: todo / in_progress / done
New Status:  done
Status updated!

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  3
Task ID:  f0c2c5ba-52f0-4779-90d7-f931d1a85af3
Options: todo / in_progress / done
New Status:  in_progress
Status updated!

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  2
Filter by status? (leave empty for all):  done

Listing 1 tasks:
ID        : b3945082-57c3-4294-9f9c-194c2a02a5bb
Title     : Evening walk
Description: One hour walk to reset and reflect
Status    : done
Created At: 2026-02-01 15:41:50
Updated At: 2026-02-01 15:44:15



TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  2
Filter by status? (leave empty for all):  in_progress

Listing 1 tasks:
ID        : f0c2c5ba-52f0-4779-90d7-f931d1a85af3
Title     : Prepare interview answers
Description: Go through HR questions and project explanations
Status    : in_progress
Created At: 2026-02-01 15:43:29
Updated At: 2026-02-01 15:44:35



TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  2
Filter by status? (leave empty for all):  

Listing 3 tasks:
ID        : f0c2c5ba-52f0-4779-90d7-f931d1a85af3
Title     : Prepare interview answers
Description: Go through HR questions and project explanations
Status    : in_progress
Created At: 2026-02-01 15:43:29
Updated At: 2026-02-01 15:44:35


ID        : fc303af9-2482-4267-942b-f2b810d6e7c7
Title     : Organize notes
Description: Clean and structure study notes and resume points
Status    : todo
Created At: 2026-02-01 15:42:54
Updated At: 2026-02-01 15:42:54


ID        : b3945082-57c3-4294-9f9c-194c2a02a5bb
Title     : Evening walk
Description: One hour walk to reset and reflect
Status    : done
Created At: 2026-02-01 15:41:50
Updated At: 2026-02-01 15:44:15



TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  4

 METRICS
Total Tasks: 3
Counts     : {'todo': 1, 'done': 1, 'in_progress': 1}
Avg Time   : 144.81 seconds

TASK MANAGER
1. Add Task
2. List Tasks
3. Update Status
4. Show Metrics
5. Exit
Choose an option:  5
Exiting. Bye!
