#!/usr/bin/env python3
# -*- coding: utf-8 -*-

well_height = 125
daily_advance = 30
night_retreat = -20
accumulated_distance = daily_advance + night_retreat
totalcms = 0
days=0

snailhasnotescaped = True
while snailhasnotescaped:
    totalcms += daily_advance
    if totalcms >= well_height:
        snailhasnotescaped = False
        break

    days += 1

    totalcms += night_retreat
    if totalcms >= well_height:
        snailhasnotescaped = False
        break

print(days)

#######
well_height = 125
daily_advance = 30
night_retreat = -20
accumulated_distance = daily_advance + night_retreat
totalcms = 0
total = 0
days = 0
snailhasnotescaped = True

while snailhasnotescaped:
    totalcms += accumulated_distance
    days += 1
    if totalcms >= well_height:
        snailhasnotescaped = False
        break
#########
print("Days = ", days, "days")

and 



