#!/usr/bin/env python3
# Name : Pushkar Madan
# email : pushkarmadan@yahoo.com
# Purpose: basic deployement test of mod using simplemod as core library.

import simplemod

### Initiating class.
my_mod = simplemod.simplemod()

print ("listing supported games")
my_mod.list_games()

print("Selecting \"nier-testing2\" as game to work with.")
my_game = "nier-testing2"

print("Listing mods available for game \""+str(my_game)+"\"")
mods = my_mod.list_mods_files(my_game)
c = 1
for x in mods:
    print(str(c)+" "+str(x))
    c = c + 1

print("Please ensure you've created a testing directory \"~/neir_automata-testing/data/\" for this, if you know what your are doing you can update \"gconf\"." )
mod = "2btoa2.zip"

print("Deploying mod \"2btoa2.zip\"")
my_mod.deploy_mod(mod,my_game)

print("Testing the removal of mods deployed")
my_mod.clean_mods_dir(my_game)
