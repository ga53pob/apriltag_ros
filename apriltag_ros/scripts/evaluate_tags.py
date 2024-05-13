#! /usr/bin/env python3

import rospy
import os, sys
import time
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
import json

from std_srvs.srv import Trigger
from robot_controller.srv import NewActionPlan

def update_blackboard(path):
    """
    blackboard_file = open(path)
    blackboard_json = json.load(blackboard_file)"""
    pass

def spawn_objects():
    pass

if __name__ == '__main__':
    #checks the detectet tags and updates the blackboard
    #then the objects are spawned
    try:
        rospy.init_node(os.path.basename(sys.argv[0]).replace('.py', '_node'))
        rospy.loginfo("NODE CALL ACTION PLAN: Executing!")

        #initialize
        action_plan = rospy.get_param("/task")

        action_plan_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../../','config','tasks',f'{action_plan}.json'))
        rospy.loginfo("Action plan path: "+str(action_plan_path))
            
        action_plan_file = open(action_plan_path)
        action_plan_json = json.load(action_plan_file)

        # call service to send action plan
        try:
            rospy.wait_for_service("/robot_controller_node/new_action_plan", timeout=2)
            new_action_plan = rospy.ServiceProxy("/robot_controller_node/new_action_plan", NewActionPlan)
            rospy.loginfo("NODE CALL ACTION PLAN: Send action plan to robot controller.")

            resp = new_action_plan(json.dumps(action_plan_json))

            # show result, if robot accepted or declined action plan
            if resp.success == 1:
                rospy.loginfo("NODE CALL ACTION PLAN: Robot idle and accepted action plan.")
            else:
                rospy.loginfo("NODE CALL ACTION PLAN: Robot busy and declined action plan.")
                rospy.loginfo("Task Execution Failed", "Failed to execute the task, as the robot is currently busy and therefore declined the action plan.")

        except:
            rospy.loginfo("NODE CALL ACTION PLAN: service call '/robot_controller_node/new_action_plan' failed.")
            rospy.loginfo("Task Execution Failed", "Failed to execute the task, as the service call '/robot_controller_node/new_action_plan' failed.")

        rospy.spin()
    except rospy.ROSInterruptException:
        pass