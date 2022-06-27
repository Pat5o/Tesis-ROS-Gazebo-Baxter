#!/usr/bin/env python

"""
Tool to tuck/untuck Baxter's arms to/from the shipping pose
"""
import subprocess

import baxter_interface

subprocess.call(["rosrun","baxter_sim_examples","tuck_arms.py", "-u"])

