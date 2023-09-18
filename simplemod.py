#!/usr/bin/env python3
# Name : Pushkar Madan
# email : pushkarmadan@yahoo.com
# Purpose: ObjectClass library for simple-mod-manager.

import configparser
import shutil
import yaml
import os
import patoolib
from yaml.loader import SafeLoader
from shutil import copy2
import zipfile
### Need to fetch steam installation path.
from pathlib import Path

class simplemod:
    def __init__(self):
        self.steam_path = self.steam_inst_dir()
        print("Meow Meow !!")

    def steam_inst_dir(self,path="none"):
        if path == "none":
            path = str(Path.home())
            return path
        else:
            return path

    def load_gconf(self):
        with open("db/gconf.yml") as f:
            data = yaml.load(f, Loader=SafeLoader)
        f.close()
        return data

    def list_mods_files(self,game):
        self.get_src(game)
        mdir = self.get_src(game)
        mlist = os.listdir(mdir)
        print("\nPlease find below list of mods.")
        c=1
        for f in mlist:
            print(str(c)+".  "+str(f))
            c = c + 1
        return mlist

    def list_mods_files_root(self,game):
        self.get_src(game)
        mdir = self.get_src(game)
        mlist = os.listdir(mdir)
        return mlist

    def get_src(self,game):
        mdata = self.load_gconf()
        return mdata[game]["mod_src"]

    def get_mod_dest(self,game):
        mdata = self.load_gconf()
        mod_root=mdata[game]["mod_root"]
        mod_dir=mdata[game]["mod_dir"]
        moddir={ "root":mod_root, "moddir":mod_dir }
        return moddir

    def list_games(self):
        x = self.load_gconf()
        c = 1
        for i in x:
            print(str(c)+". "+str(i)+"\t"+str(x[i]['display name']))
            c = c + 1

    ### Need to determine if downloaded mods'a data to be displayed based on data from nexsus mods or based on downloaded files.
    ### As of now going with data from local files.

    def check_moddir(self,game):
        dirdata = self.get_mod_dest(game)
        final_mod_dir=str(dirdata['root'].replace("~",self.steam_path))+str(dirdata['moddir'])
        try:
            os.listdir(dirdata["root"].replace("~",self.steam_path))
            try:
                os.listdir(final_mod_dir)
            except:
                print("ERROR2: unable to find game mod directory.")
                print("ERROR2: Probably we can created a new mod directory : "+str(final_mod_dir))
                self.create_moddir(final_mod_dir)
            else:
                print("listing was sucessful")

        except:
            print("ERROR: unable to find the game directory.")
            print("ERROR: path :- "+str(dirdata["root"]))
            return 2
        else:
            print("Root dir listing was sucessful.")

    def create_moddir(self,path):
        print("creating new directory : "+str(path))
        os.mkdir(path)

    def deploy_mod(self,mod,game):
        mfiles=[]
        ### Fetching path to deploy mods.
        mdir_data = self.get_mod_dest(game)
        ### steam installation directory can be different for different users.
        ### TODO object class variable steam_path can be named better like "steam_install_dir" "steam_parent_path" etc.
        final_mod_dest = str(mdir_data["root"].replace("~",self.steam_path))+str(mdir_data["moddir"])

        self.check_moddir(game)
        ### unzip the modarchives into temp and copy the files to moddir.
        ### later need to identify logic on how to manage multiple mod files and how to copy replace them also how to identify them.
        ### identify if given mod is zip file or not ( this is for later development)
        ### Going ahead with the assumption that the downloaded mod is a zip archive.
        mod_path = self.get_src(game)
        mod_with_path = str(mod_path)+str(mod)
        #print(mod_with_path)
        z = zipfile.ZipFile(mod_with_path)
        print("Extrating mods into \"m_temp\"")
        z.extractall("m_temp")
        for root, dirs, files in os.walk("m_temp"):
            for file in files:
                m_path = str(os.path.join(root,file))
                mfiles.append(m_path)
        #print(mfiles)
        for f in mfiles:
            print( "copyting " +str(f)+ " to " + final_mod_dest )
            shutil.copy2(f, final_mod_dest)
        shutil.rmtree("m_temp")

    def clean_mods_dir(self,game):
        mdir_data = self.get_mod_dest(game)
        final_mod_dest = str(mdir_data["root"].replace("~",self.steam_path))+str(mdir_data["moddir"])
        #print(final_mod_dest)
        shutil.rmtree(final_mod_dest)
        os.mkdir(final_mod_dest)

