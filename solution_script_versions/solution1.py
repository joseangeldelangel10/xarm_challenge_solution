#!/usr/bin/env python
"""
---------------- ROS NODE THAT INSTRUCTS XARM6 COLAB ROBOT ----------------
---------------- IN ORDER TO ACHIVE A PICK AND PLACE TASK  ----------------  
Developed by:
      - Leonardo Javier Nava Castellanos        ITESM CEM       A01750595
      - Jose Angel Del Angel Dominguez          ITESM CEM       A01749386

The following program uses python 3, along with ROS framework.

Several plugins of ROS framework are used simulate the xarm colab robot
in a testing environment. Such testing environment consists in the xarm robot
positioned over a table, such table also has 3 solid boxes and 3 containers to deposit such boxes.

The following code will allow the robot to pick each box and place it in the container that matches the color of the box.

The ROS plugins used to achive this simulation are:
  - Gazebo
  - Rviz
  - Moveit (Rviz plugin)

The code consists in 2 main classes Planer() and myNode(); Planner() allows us to plan and excecute trajectories given a pose, consider the exixsing obstacles in the robot environment and simulate the gripper closing and opening, while myNode() consumes the service RequestGoal provided by other nodes to know the order in wich the boxes should be picked and placed and at the same calls the functions of planner as required so that the robot picks and places all the boxes  
"""
import rospy
import sys
import tf_conversions
import tf2_ros
import moveit_commander
import moveit_msgs.msg
from numpy import pi
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import PoseStamped, Pose
from path_planner.srv import *
from tf.transformations import *
from moveit_msgs.msg import Grasp
import copy

class Planner():

  def __init__(self):
    moveit_commander.roscpp_initialize(sys.argv)
    self.robot = moveit_commander.RobotCommander()
    self.scene = moveit_commander.PlanningSceneInterface(synchronous=True)
    self.arm_group = moveit_commander.MoveGroupCommander("xarm6")
    self.gripper_group = moveit_commander.MoveGroupCommander("xarm_gripper")
    self.arm_eff_link = self.arm_group.get_end_effector_link()    
  
  def wait_for_state_update(self,box_name, box_is_known=False, box_is_attached=False, timeout=4):
    rospy.sleep(0.1)
    return True
    
  def addObstacles(self):
    print("===== ADDING OBSTACLES =====")
    #Cargo names
    targets = ["RedBox",
               "BlueBox",
               "GreenBox"]
    #goal names
    deposits = ["DepositBoxGreen",
               "DepositBoxRed",
               "DepositBoxBlue"]
    for i in targets:
      print("ADDING OBSTACLES: " + i)
      box_pose = PoseStamped()
      box_pose.header.frame_id = i
      box_pose.pose.position.x = 0
      box_pose.pose.position.y = 0
      box_pose.pose.position.z = 0
      box_pose.pose.orientation.w = 1.0
      box_name = i
      self.scene.add_box(box_name, box_pose, size=(0.06, 0.06, 0.06))
    for j in deposits:
      print("ADDING OBSTACLES: " + j)
      deposit_pose = PoseStamped()
      deposit_pose.header.frame_id = j
      deposit_pose.pose.position.x = 0
      deposit_pose.pose.position.y = 0
      deposit_pose.pose.position.z = 0
      deposit_pose.pose.orientation.w = 1.0
      deposit_name = j
      self.scene.add_box(deposit_name, deposit_pose, size=(0.39524, 0.171428, 0.109964))
    return True
    
  def goToPose(self,pose_goal):
    print("======= TRAVELING TO THE GIVEN POSE ======")
    self.arm_group.set_pose_target(pose_goal)
    plan = self.arm_group.go(wait=True)
    self.arm_group.stop()    
    self.arm_group.clear_pose_targets()
    
  def detachBox(self,box_name):
    joint_goal = [0,0,0,0,0,0]
    self.gripper_group.set_joint_value_target(joint_goal)
    self.gripper_group.go(wait=True)
    self.gripper_group.stop()
    self.scene.remove_attached_object(self.arm_eff_link, name=box_name)
    try:
      attach = rospy.ServiceProxy('AttachObject', AttachObject)
      resp = attach(False, box_name)
    except rospy.ServiceException as e:
      print("Service AttachObject call failed: %s"%e)
    return True

  def attachBox(self,box_name):
    joint_goal = [0.2094,0.2094,0.2094,0.2094,0.2094,0.2094]
    self.gripper_group.set_joint_value_target(joint_goal)
    self.gripper_group.go(wait=True)
    self.gripper_group.stop()
    
    grasping_group = "xarm_gripper"
    touch_links = self.robot.get_link_names(group=grasping_group)
    print("=========== TOUCK LINK INFO: ========")
    print( "type: " + str(type(touch_links)))
    print( "len: " + str(len(touch_links)))
    print("=========== TOUCK LINK INFO ENDS ========")
    self.scene.attach_box(self.arm_eff_link, box_name, touch_links=touch_links)
    try:
      attach = rospy.ServiceProxy('AttachObject', AttachObject)
      resp = attach(True, box_name)
    except rospy.ServiceException as e:
      print("Service AttachObject call failed: %s"%e)
    return True


class myNode():
  def __init__(self):
    rospy.init_node("solution_template")
    
    # wait until the required services are online before continuing with the aplication
    rospy.wait_for_service('RequestGoal')
    rospy.wait_for_service('AttachObject')

    RedBoxPose = Pose()
    RedBoxPose.position.x = 0.20078 + 0.01
    RedBoxPose.position.y = 0.51023
    RedBoxPose.position.z = -0.0003553 + 0.01
    RedBoxPose.orientation.x = 1.0
    RedBoxPose.orientation.w = 0.0

    BlueBoxPose = Pose()
    BlueBoxPose.position.x = 0.074797 + 0.005
    BlueBoxPose.position.y = 0.55853
    BlueBoxPose.position.z = -0.013793 + 0.01
    BlueBoxPose.orientation.x = 1.0
    BlueBoxPose.orientation.w = 0.0

    GreenBoxPose = Pose()
    GreenBoxPose.position.x = 0.2062 - 0-01
    GreenBoxPose.position.y = 0.19451
    GreenBoxPose.position.z = -0.0062706 + 0.01
    GreenBoxPose.orientation.x = 1.0
    GreenBoxPose.orientation.w = 0.0

    RedDepositPose = Pose()
    RedDepositPose.position.x = 0.049178
    RedDepositPose.position.y = -0.45759
    RedDepositPose.position.z = 0.17092
    RedDepositPose.orientation.x = 1.0
    RedDepositPose.orientation.w = 0.0

    BlueDepositPose = Pose()
    BlueDepositPose.position.x = -0.1738
    BlueDepositPose.position.y = -0.47428
    BlueDepositPose.position.z = 0.17092
    BlueDepositPose.orientation.x = 1.0
    BlueDepositPose.orientation.w = 0.0

    GreenDepositPose = Pose()
    GreenDepositPose.position.x = 0.2593
    GreenDepositPose.position.y = -0.45035
    GreenDepositPose.position.z = 0.17092
    GreenDepositPose.orientation.x = 1.0
    GreenDepositPose.orientation.w = 0.0

    HomePose = Pose()
    HomePose.position.x = 0.37796
    HomePose.position.y = 0.000244214
    HomePose.position.z = 0.246642
    HomePose.orientation.x = 1.0
    HomePose.orientation.w = 0.0

    self.targets = {"RedBox" : RedBoxPose ,"BlueBox" : BlueBoxPose,"GreenBox" : GreenBoxPose, "DepositBoxGreen" : GreenDepositPose , "DepositBoxRed" : RedDepositPose, "DepositBoxBlue" : BlueDepositPose, "End": HomePose}

  def getGoal(self,action):
    try:
      goal = rospy.ServiceProxy('RequestGoal', RequestGoal)
      resp = goal(action)
      print("===== GOAL IS : =====")
      print(resp.goal)
      return resp.goal
    except rospy.ServiceException as e:
      print("Service call failed: %s"%e)
      return None

  def tf_goal(self, goal):
    
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    transformStamped = tfBuffer.lookup_transform("link_base", goal, rospy.Time(), rospy.Duration(1.0))
    print("===== Here is datatype =====")
    print(str(type(transformStamped)))
    print(goal, transformStamped)
    pose = Pose()
    pose.position.x = transformStamped.transform.translation.x
    pose.position.y = transformStamped.transform.translation.y
    pose.position.z = transformStamped.transform.translation.z
    pose.orientation.x = 1.0
    pose.orientation.w = 0.0
    return pose

  def main(self):
    #TODO: Main code that contains the aplication
    self.planner = Planner()
    self.planner.addObstacles()
    
    for i in range(3):
      pick = self.getGoal("pick")
      
      self.planner.goToPose(self.tf_goal(pick))
      self.planner.attachBox(pick)
      place = self.getGoal("place")
      self.planner.goToPose(self.targets[place])
      self.planner.detachBox(pick)

    self.planner.goToPose(self.targets["End"])
    
    rospy.signal_shutdown("Task Completed")



if __name__ == '__main__':
  try:
    node = myNode()
    node.main()

  except rospy.ROSInterruptException:
    pass
