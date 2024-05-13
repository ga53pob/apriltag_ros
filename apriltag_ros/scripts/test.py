
import json
import os
import sys
import yaml




if __name__ == "__main__":
    """
    Test file to load and interact with blackboard.json and tags.yaml
    """
    tag_list = []
    file_path_bb = os.path.abspath(os.path.join(os.getcwd(),"config","blackboard","bb_pcb_testing.json"))
    file_path_tags_yaml = os.path.abspath(os.path.join(os.getcwd(),"endeffectors", "zivid-ros","apriltag_ros","apriltag_ros","config","tags.yaml" ))
    print("Hi")
    print(file_path_bb)
    with open(file_path_bb) as json_file:
        json_data = json.load(json_file)
        print(json_data)
    print(json_data['gripper'])

    for gripper in json_data['gripper']: 
        print(gripper)
        print(json_data["gripper"][gripper]["status"])

    with open(file_path_tags_yaml) as stream:
        tags_data = yaml.safe_load(stream)
        print(tags_data)
        for tag in tags_data["standalone_tags"]:
            print(tag)
            name = tag["name"]
            #print(str(name[3::]))
            tag_list.append(str(name[3::]))

    print(tag_list)

    for tag in tag_list:

        pass
        #check if tag in list of tf (ROS)
        #take coordinates and update urdf? / spawn models
        #update Blackboard coordinates