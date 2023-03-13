#######################################
# THIS FILE IS USED TO CONTROL GLOBAL #
# VARIABLES, USED AS SETTINGS FOR THE #
# SOFTWARE. DON'T REASSIGN OUTSIDE T- #
# -HIS SCOPE. ALL UNITS ARE IN SI MKS #
#######################################

from ursina import Vec4, Vec3, Vec2, color

# Viewer Globals #
WIRE_COLOR = color.black

# Scintillator Globals #
SCINTILLATOR_SIZE_X = 0.5
SCINTILLATOR_SIZE_Y = 0.5
SCINTILLATOR_SIZE_Z = 0.0254  # 1 inch
SCINTILLATOR_COLOR = color.pink

# Ground Globals #
GROUND_COLOR = color.brown

# Muons Globals #
CREATION_HEIGHT = 10  # meters above scintillator
MUON_COLOR = color.green

# 0 Vec #
VEC0_2D = Vec2(0, 0)
VEC0_3D = Vec3(0, 0, 0)
VEC0_4D = Vec4(0, 0, 0, 0)

# Energy Scales #
KeV = 10 ** 3
MeV = 10 ** 6
GeV = 10 ** 9

# Deltas for physics #
dt = 0.001  # sec
dx = 0.01  # meter

# Spatial Scales #
m = 1
km = 10**3
cm = 10**-1
mm = 10**-2
