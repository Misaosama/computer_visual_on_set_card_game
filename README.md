# computer_visual_on_set_card_game
Aim to train the computer to recognize number, shape, shading and color of cards and find all sets.

# Rules
https://en.wikipedia.org/wiki/Set_(card_game)

# Data Structure
The meaning of 4 dimensions of the vector 
<pre>
+--------------------------------------------+ 
|0 => number:   1         2         3        | 
|1 => shape:    diamond   oval      squiggle | 
|2 => color:    red       green     purple   | 
|3 => shading:  solid     striped   open     | 
+--------------------------------------------+ 
</pre>

# TODO
1) Splite a picture of 12 cards into 12 images each containing one card.
2) Convert each card image into a 4-dim vector.
