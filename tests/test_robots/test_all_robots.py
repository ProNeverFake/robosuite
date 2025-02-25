"""
Tests the basic interface of all robots.

This runs some basic sanity checks on the robots, namely, checking that:
    - Verifies that all single-arm robots have properly defined contact geoms.

Obviously, if an environment crashes during runtime, that is considered a failure as well.
"""
from robosuite.robots import  FixedBaseRobot, LeggedRobot, WheeledRobot
# , ROBOT_CLASS_MAPPING

ROBOT_CLASS_MAPPING = {
    # "Baxter": FixedBaseRobot,
    # "IIWA": FixedBaseRobot,
    # "Jaco": FixedBaseRobot,
    # "Kinova3": FixedBaseRobot,
    # "Panda": FixedBaseRobot,
    # "Sawyer": FixedBaseRobot,
    # "UR5e": FixedBaseRobot,
    # "SpotWithArm": LeggedRobot,
    # "SpotWithArmFloating": LeggedRobot,
    # "PandaOmron": WheeledRobot,
    # "Tiago": WheeledRobot,
    # "GR1": LeggedRobot,
    # "GR1FixedLowerBody": LeggedRobot,
    # "GR1ArmsOnly": LeggedRobot,
    "GR1FloatingBody": LeggedRobot,
    # "PandaDexRH": FixedBaseRobot,
    # "PandaDexLH": FixedBaseRobot,
}

def test_all_robots():
    for name, robot in ROBOT_CLASS_MAPPING.items():
        print(f"Testing {name}")
        if robot not in [FixedBaseRobot, WheeledRobot, LeggedRobot]:
            raise ValueError(f"Invalid robot type: {robot}")
        else:
            _test_contact_geoms(robot(name))
            
    return robot


def _test_contact_geoms(robot):
    robot.load_model()
    contact_geoms = robot.robot_model._contact_geoms
    for geom in contact_geoms:
        assert isinstance(geom, str), f"The geom {geom} is of type {type(geom)}, but should be {type('placeholder')}"


if __name__ == "__main__":
    # test_single_arm_robots()
    robot = test_all_robots()
    import ipdb; ipdb.set_trace() 
    print("Robot tests completed.")
