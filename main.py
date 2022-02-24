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
numProj = 0
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
            "roles": {}
        }

        for j in range(int(nR)):
            l2 = fh.readline().strip().split()
            skill, level = l2[0], l2[1]
            projects[name]["roles"][skill] = int(level)

    # pprint(contributors, indent=4)
    # print(skillsTotal, indent = 4)
    # pprint(skills, indent=4)
    # print(projects)
    # pprint(projects, indent=4)
    # print(c, p)

    fh.close()

def basic_algo():
    for project_name in projects:
        project = projects[project_name]
        roles = project["roles"]

        # TODO: Shortlist based on

        all_avail = True
        contri_allot = []

        for role in roles:
            levelReq = roles[role]
            skill_avail = False

            print(role, levelReq)

            for contri_name in skills[role]:
                skill_level = skills[role][contri_name]
                
                print(contri_name, role, skill_level)
                
                if avail[contri_name] == 0 and skill_level >= levelReq:
                    contri_allot.append(contri_name)
                    skill_avail = True

            if skill_avail == False:
                print(skill_avail)
                all_avail == False
                break
        
        if(all_avail == False):
            print(project_name)
            continue

        # numProj = numProj + 1
        final_proj[project_name] = contri_allot

        for contri in contri_allot:
            avail[contri] = 1


def submission(file_path="out.txt"):
    oh = open(file_path, 'w')

    pprint(final_proj)
    # oh.writelines(len(final_proj))

    # for proj_name in final_proj:
    #     oh.writelines(proj_name)
    #     oh.writelines(" ".join(final_proj[proj_name]))

    oh.close()

if __name__ == '__main__':
    process_data("a_an_example.in.txt")
    basic_algo()
    submission("a.txt")
    # pprint(avail)
    # process_data("b_better_start_small.in.txt")
    # process_data("c_collaboration.in.txt")
    # process_data("d_dense_schedule.in.txt")
    # process_data("e_exceptional_skills.in.txt")
    # process_data("f_find_great_mentors.in.txt")
