Atomic operation: 
  - An operation acting on shared memory is atomic if it completes in a single step relative to other threads.
  - Uninterruptable, prevents processor from writing or reading memory until operation is complete
  - 

Semaphore:
 - A Variable or abstract data type that is used to control access to a common resource by multiple processes in a concurrent system
 - Bouncer: a certain number of people allowed at once. Full: No one enters, otherwise people can enter.
 - Flag. Used for signaling. 
 - An integer greater than or equal to 0
  - A way of allowing multiple users simultaneous access to the same resource, or not allowing.

Mutex:
  - A binary flag, locks or releases, always in that order
  - Used to protect a shared resource by ensuring mutual exclusion 
  - One key, one bathroom analogy

Critical Section:
  - A piece of code that should not be concurrently executed
  - Use Mutex to protect

