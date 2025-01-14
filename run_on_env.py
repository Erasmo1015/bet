import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" # before import torch, keras
os.environ['PYOPENGL_PLATFORM'] = 'egl'

import hydra
import joblib
import numpy as np


@hydra.main(config_path="configs", config_name="env_config")
def main(cfg):
    # Needs _recursive_: False since we have more objects within that we are instantiating
    # without using nested instantiation from hydra
    workspace = hydra.utils.instantiate(cfg.env.workspace, cfg=cfg, _recursive_=False)
    rewards, infos = workspace.run()
    print(rewards)
    print(infos)
    print(f"Average reward: {np.mean(rewards)}")
    print(f"Std: {np.std(rewards)}")


if __name__ == "__main__":
    main()
