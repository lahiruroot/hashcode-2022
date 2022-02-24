#!/usr/bin/env python3

from pprint import pprint
from textwrap import indent
from cv2 import split
import numpy as np

contributors = {}
avail = {}
skills = {}
projects = {}
skillsTotal = set()
final_proj = {}

def process_data(file_path):
    fh = open(file_path)
    l1 = fh.readline().strip().split()
    c, p = l1[0], l1[1]
    
    # ! Contributors
    for i in range(int(c)):
        l2 = fh.readline().strip().split()
        name, numSkill = l2[0], l2[1]

        avail[name] = 0
        # contributors[name] = {
        #     "C++":9,
        #     "Python":8
        # }

        tempDict = dict()

        for j in range(int(numSkill)):
            l3 = fh.readline().strip().split()
            nameSkill, level = l3[0], l3[1]
            skillsTotal.add(nameSkill)
            tempDict[nameSkill] = int(level)

        contributors[name] = tempDict

    # ! Skills
    for name in contributors:
        name_obj = contributors[name]

        for skill in skillsTotal:
            if skill in name_obj:
                if skill in skills:
                    skills[skill][name] = name_obj[skill]
                else:
                    skills[skill] = {name: name_obj[skill]}
            else:
                if skill in skills:
                    skills[skill][name] = 0
                else:
                    skills[skill] = {name: 0}

    # ! Projects
    for i in range(int(p)):
        l1 = fh.readline().strip().split()
        name = l1[0]
        days = l1[1]
        score = l1[2]
        bb = l1[3]
        nR = l1[4]

        projects[name] = {
            "days": int(days),
            "score": int(score),
            "bb": int(bb),
            "roles": [],
            "RL": []
        }

        for j in range(int(nR)):
            l2 = fh.readline().strip().split()
            skill, level = l2[0], l2[1]
            # projects[name]["roles"][skill] = int(level)
            projects[name]["roles"].append(skill)
            projects[name]["RL"].append(int(level))

    # pprint(contributors, indent=4)
    # print(skillsTotal, indent = 4)
    # pprint(skills, indent=4)
    # print(projects)
    # pprint(projects, indent=4)
    # print(c, p)

    fh.close()

def basic_algo():
    proj_done = False

    for project_name in projects:
        project = projects[project_name]
        roles = project["roles"]
        levels = project["RL"]

        # TODO: Shortlist based on

        all_avail = True
        contri_allot = {}
# projects
        itr = 0
        for role in roles:
            levelReq = levels[itr]
            itr += 1
            skill_avail = False

            for contri_name in skills[role]:
                skill_level = skills[role][contri_name]
                
                if avail[contri_name] == 0 and skill_level >= levelReq:
                    contri_allot[contri_name] = [role, (skill_level == levelReq)]
                    skill_avail = True
                    avail[contri_name] = 1
                    break

            if skill_avail == False:
                all_avail = False
                break
        
        if(all_avail == False):
            for contri in contri_allot:
                avail[contri] = 0    
            continue

        # numProj = numProj + 1
        proj_done = True
        final_proj[project_name] = contri_allot

        # pprint(contri_allot)
        for contri in contri_allot:
            # avail[contri] = 1
            if contri_allot[contri][1]:
                skills[contri_allot[contri][0]][contri] += 1
                contributors[contri][contri_allot[contri][0]] += 1


    return proj_done

def iter_basic():
    infi = False
    while infi == False:
        check = basic_algo()
        if check == False:
            infi = True
            break


def submission(file_path="out.txt"):
    oh = open(file_path, 'w')

    pprint(final_proj)
    oh.writelines(str(len(final_proj)))
    oh.writelines("\n")

    for proj_name in final_proj:
        oh.writelines(proj_name)
        oh.writelines("\n")
        oh.writelines(" ".join(final_proj[proj_name]))
        oh.writelines("\n")

    oh.close()

def wrapper(file_path):
    resetter()
    process_data(file_path)
    iter_basic()
    obj = file_path.split("_")[0]
    submission(f"{obj}.txt")

def resetter():
    global contributors
    global avail
    global skills
    global projects
    global skillsTotal
    global final_proj

    contributors = {}
    avail = {}
    skills = {}
    projects = {}
    skillsTotal = set()
    final_proj = {}

if __name__ == '__main__':
    # wrapper("a_an_example.in.txt")
    wrapper("b_better_start_small.in.txt")
    # process_data("b_better_start_small.in.txt")
    # pprint(projects)
    # wrapper("c_collaboration.in.txt")
    # wrapper("d_dense_schedule.in.txt")
    # wrapper("e_exceptional_skills.in.txt")
    # wrapper("f_find_great_mentors.in.txt")
