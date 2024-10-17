import mujoco
import mujoco.viewer as viewer

xml_path = "assets/low_cost_robot_6dof/pick_place_cube.xml"
model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)

viewer.launch(model, data)