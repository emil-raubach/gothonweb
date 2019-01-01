# Gothon Web

My attempt at extending the _**gothonweb**_ game from the book 'Learn Python The Hard Way' by Zed A. Shaw.

As of 12-Feb-2018 I have done the following:
* Fixed several bugs
* Replaced the **load_room** and **name_room** functions that used the **globals()** dict
* Made the HTML / CSS look a little bit better (still need to figure out the \<pre\> tags)
* Improved the automated tests to some degree
* Added all of the paths from the original game - albeit in a completely linear fashion

My main holdup has been trying to figure out how to add the ability to insert control flow logic into the game so I can add features like having the code to the lockbox randomly generated, or just some other fun stuff that you can do with **if-else**, etc.  

I am trying to implement this by adding the **enter** method to the **Room()** class with the intent to subclass it and override the **enter** method in the subclasses.  (e.g., **CentralCorridor(Room)**)
