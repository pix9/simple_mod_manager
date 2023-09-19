#!/usr/bin/env python
# Name : Pushkar Madan
# Email : pushkarmadan@yahoo.com
# Date : 19th September 2023
# Purpose : To enable the commandline functionality for simple mod manager.
# Notes :
#

import sys
import getopt
import simplemod

argv = sys.argv[1:]

def usage():
    print("usage: manager.py [-h] [-g] [-m] [-G] [-M] [-d] [-C]")
    print("\noptions:")
    print("  -h  --help\t\tDisplay this help message and exit.")
    print("  -g  --game\t\tName of game or Steam ID of respective game.(Note: steam ID not yet supported.)")
    print("  -m  --mod\t\tMod for respective game(ideally *.zip file name for given mod).")
    print("  -G  --list-games\tList available games in simple mod manager config.")
    print("  -M  --list-mods\tList availables mods for the given game")
    print("  -d  --deploy\t\tDeployes the given mode for respective game.")
    print("  -C  --clean-mods\tRemoved all the deployed mod for respective game.")


def main():

    try:
        opts, args = getopt.getopt(argv, "g:m:GMCdh", ["game=", "mod=", "list-games", "list-mods", "clean-mods", "deploy", "help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    game_v = False
    mod_v = False
    list_games = False
    list_mods = False
    clean_mods = False
    deploy= False
    help_menu = False
    my_game="None"
    my_mod="None"

    for o, a in opts:
        if o in ("-g", "--game"):
            game_v = True
            my_game = a
            print("This is the game you want to  display \""+str(my_game)+"\"")
        if o in ("-m", "--mod"):
            mod_v = True
            my_mod = a
            print("This is the mod you want to  display \""+str(my_game)+"\"")
        elif o in ("-G", "--list-games"):
            list_games = True
            print("You want to list games.")
        elif o in ("-M", "--list-mods"):
            list_mods = True
            print("You want to list mods.")
        elif o in ("-C", "--clean-mods"):
            clean_mods = True
            print("You want to clean mods.")
        elif o in ("-d", "--deploy"):
            deploy = True
            print("You want to deploy.")
        elif o in ("-h", "--help"):
            help_menu = True
    ### Initiating simplemod
    sm = simplemod.simplemod()

    if help_menu:
        usage()
    ### List games. ( True values : list_games )
    elif not game_v and not mod_v and list_games and not list_mods and not deploy and not clean_mods:
        sm.list_games()
    ### List mods for given game. ( True values : game_v, list_mods )
    elif game_v and not mod_v and not list_games and list_mods and not deploy and not clean_mods:
        sm.list_mods_files(my_game) 
    ### Deploy mods. (True values : game_v, mod_v, deploy )
    elif game_v and mod_v and not list_games and not list_mods and deploy and not clean_mods:
        sm.deploy_mod(my_mod,my_game)
    ### Clean up games. ( True values : game_v, clean_mods )
    elif game_v and not mod_v and not list_games and not list_mods and not deploy and clean_mods:
        print("You've chosen to clean mods for : "+str(my_game))
        sm.clean_mods_dir(my_game)
    else:
        print("Insufficient parameters.")
        usage()

if __name__ == "__main__":
    main()
