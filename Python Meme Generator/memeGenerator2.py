#!/usr/bin/env python

import random

class MemeGenerator(object):
    def __init__(self):
        global nouns, verbs, adjs, structs
        nouns   = []
        verbs   = []
        adjs    = []
        structs = []

        with open("structs.txt") as struct:
            for line in struct:
                structs.append(line.replace("\n",""))

        with open("nouns.txt") as files:
            for line in files:
                nouns.append(line.replace("\n",""))

        with open("verbs.txt") as files:
            for line in files:
                verbs.append(line.replace("\n",""))

        with open("adjs.txt") as files:
            for line in files:
                adjs.append(line.replace("\n",""))

    def genMeme(self):
        struct = random.choice(structs)
        var = struct.count("{")
        for i in range(0,var+1):
            
            e = random.choice(nouns)
            f = random.choice(nouns)
            g = random.choice(nouns)
            
            h = random.choice(verbs)
            i = random.choice(verbs)
            j = random.choice(verbs)

            k = random.choice(adjs)
            l = random.choice(adjs)
            m = random.choice(adjs)
            
        print(struct.format(noun=e,noun2=f,noun3=g,verb=h,verb2=i,verb3=j,adj=k,adj2=l,adj3=m))

memegen = MemeGenerator()
memegen.genMeme()

