# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import textwrap
import mujoco
import mujoco.viewer

# %%
MUJOCO_MODEL_XML = textwrap.dedent('''\
    <mujoco>
        <option integrator="RK4"/>
        <option timestep="0.0002"/>
        <asset>
            <mesh file="funnel_piece_0.stl" scale="0.01 0.01 0.01"/>
        </asset>
        <asset>
            <mesh file="funnel_piece_120.stl" scale="0.01 0.01 0.01"/>
        </asset>
        <asset>
            <mesh file="funnel_piece_240.stl" scale="0.01 0.01 0.01"/>
        </asset>
        <asset>
            <mesh file="ball.stl" scale="0.01 0.01 0.01"/>
        </asset>
        <worldbody>
            <light name="top" pos=".1 0 1"/>
            <body name="ball">
                <geom type="mesh" mesh="ball" name="ball" rgba="0 1 0 1" friction="0.75 0.00375 0.000075"/>
                <freejoint name="object"/>
            </body>
            <body name="funnel">
                <geom type="mesh" mesh="funnel_piece_0" rgba="1 0 0 1" friction="0.75 0.00375 0.000075"/>
                <geom type="mesh" mesh="funnel_piece_120" rgba="1 0 0 1" friction="0.75 0.00375 0.000075"/>
                <geom type="mesh" mesh="funnel_piece_240" rgba="1 0 0 1" friction="0.75 0.00375 0.000075"/>
            </body>
        </worldbody>
    </mujoco>''')

# %%
model = mujoco.MjModel.from_xml_string(MUJOCO_MODEL_XML)
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

# %%
mujoco.viewer.launch(model)

# %%
