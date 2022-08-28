This piece of garbage is perhaps my least useful program to date.
While the standard program executes its commands in a relatively linear
path aside from loops and subroutines, this meta program will execute 
other code in a nonlinear path. The path is laid out in a .csv file, with
a cursor that starts in the top left position in the .csv file, treating 
each location as a command that will be executed when the cursor moves 
over it. Standard Python code can be placed in the .csv, although escape 
characters might pose problems. The characters L, R, and U will change the 
cursor's direction relative to its position (kind of like driving a car)
and S will tell it to skip over the next command. Hopefully you can find
some use for it. If you can, let me know, because I sure can't.