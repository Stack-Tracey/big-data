
T_START_FRAME = 0
T_DURATION_FRAME = 1
X_BI_DEFLECTION_RS = 2 #reshaped' X (norm_avrg_reshaped, i.e. after reshaping to 0.8 ==> 1)
Y_BI_DEFLECTION_RS = 3 #reshaped' X (norm_avrg_reshaped, i.e. after reshaping to 0.8 ==> 1)
X_POS_BALL = 4
Y_POS_BALL = 5
X_SPEED_BALL = 6
Y_Speed_BALL = 7
OBSTACLE_HIT = 8 #yes/no (1/0) - per frame
TARGET_HIT = 9 # yes/no (1/0)
TARGET_HIT_ID = 10 # (1,2,3,4)
OBSTACLE_HIT_COL = 11 #yes/no (1/0) - collection events ONLY
TARGET_HIT_COL = 12 #yes/no (1/0) - collection events ONLY
TARGET_HIT_ID = 13 #ID (1,2,3,4) - collection events ONLY
X_BI_DEFLECTION_RAW = 14 #(mean of AI_x_Samples)
Y_BI_DEFLECTION_RAW = 15 #(mean of AI_y_Samples)
X_BI_DEFLECTION_MED = 16 #(norm_avrg, i.e. after calibration)
Y_BI_DEFLECTION_MED = 17 #(norm_avrg, i.e. after calibration)
X_FORCE_BALL = 18#(Fx, considering influence of one or both players, depending on trial type)
Y_FORCE_BALL = 19 # (Fy, considering influence of one or both players, depending on trial type)
MARKER_GOOD_PLAY = 20
PROXI_OBS_T_START_FRAME = 21 #yes/no (1/0) in proximity to obstacle number 1 to 9,
PROXI_OBS_T_DURATION_FRAME = 22 #2
PROXI_OBS_X_BI_DEFLECTION_RS = 23 #3
PROXI_OBS_Y_BI_DEFLECTION_RS = 24 #4
PROXI_OBS_X_POS_BALL = 25 #5
PROXI_OBS_Y_POS_BALL = 26 #6
PROXI_OBS_T_DURATION_FRAME = 27 #7
PROXI_OBS_X_SPEED_BALL = 28 #8
PROXI_OBS_Y_SPEED_BALL = 29 #9
PROXI_ANY_OBSTACLE = 30
WHO_SEES_PROXI_OBSTACLE = 31

START_PAIR = 21
END_PAIR = 30




