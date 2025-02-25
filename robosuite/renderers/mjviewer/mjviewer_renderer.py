from mujoco import viewer
import mujoco

DEFAULT_FREE_CAM = {
    "lookat": [0, 0, 1],
    "distance": 2,
    "azimuth": 180,
    "elevation": -20,
}




class MjviewerRenderer:
    def __init__(self, env, camera_id=None, cam_config=None, launch_passive = True):
        if cam_config is None:
            cam_config = DEFAULT_FREE_CAM
        self.env = env
        self.camera_id = camera_id
        self.viewer = None
        self.camera_config = cam_config
        self.launch_passive = launch_passive

    def render(self):
        pass

    def set_camera(self, camera_id):
        self.camera_id = camera_id

    def update(self):
        if self.viewer is None:
            if self.launch_passive:
                self.viewer = viewer.launch_passive(
                    self.env.sim.model._model,
                    self.env.sim.data._data,
                    show_left_ui=False,
                    show_right_ui=False,
                )
            else:
                self.viewer = viewer.launch(
                    self.env.sim.model._model,
                    self.env.sim.data._data,
                    show_left_ui=True,
                    show_right_ui=True,
                )

            self.viewer.opt.geomgroup[0] = 0

            if self.camera_config is not None:
                self.viewer.cam.lookat = self.camera_config["lookat"]
                self.viewer.cam.distance = self.camera_config["distance"]
                self.viewer.cam.azimuth = self.camera_config["azimuth"]
                self.viewer.cam.elevation = self.camera_config["elevation"]

            if self.camera_id is not None:
                if self.camera_id >= 0:
                    self.viewer.cam.type = 2
                    self.viewer.cam.fixedcamid = self.camera_id
                else:
                    self.viewer.cam.type = 0

        self.viewer.sync()
        
        # ! this way does not work since the mjv selection function asks for a lot of low level infos
        # d = self.env.sim.data._data
        # m = self.env.sim.model._model
        # # * mouse response --- object inspection
        # selected = mujoco.mjv_select(d, m)
        
        # if selected == -1:
        #     # no object selected, pass
        #     pass
        # else:
        #     # find the object using the geom id = selected
        #     geom_id = selected
        #     geom_name = m.id2name(geom_id, "geom")
        #     # print in green the name of the selected object
        #     print("\033[92m" + geom_name + "\033[0m")
        #     # print the position of the selected object
        #     print("Position: ", d.geom_xpos[geom_id])

    def reset(self):
        pass

    def close(self):

        self.sim = None
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None

    def add_keypress_callback(self, keypress_callback):
        self.keypress_callback = keypress_callback
