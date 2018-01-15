% data of original pairs 8, 10, 12, 19, 20 and 23 (now 'locally' pairs 1-6)
% in terms of 'SHARED EXPERIENCE', pairs 8, 10, 20 and 23 are 'good' (correlated ratings of engagement and-or collaboration)
%  while pairs 12 and 19 are 'bad collaborators' (uncorrelated ratings of engagement and collaboration)
% in terms of POERFORMANCE, pairs 8 and 23 are good, pairs 10 and 19 OK, and pairs 12 and 20 bad

% you can also find this (and other) information in the data I am sending:

%% 1. Game Data, 6x3 cell "data_over_trials" in Data_BallGame_6pairs.mat
% row# in Data_BallGame_6pairs = pair#
% columns in Data_BallGame_6pairs: 1 = player 1, 2 = player 2, 3 = information about the pair

% the entries in the first two columns (i.e. the frame-by-frame data of both players in each pair) are 3-dimensional: 

% first dimension = properties
%       1 - time start of frame
%       2 - time duration of frame
%       3 - bimetal deflection 'reshaped' X (norm_avrg_reshaped, i.e. after reshaping to 0.8 ==> 1)
%       4 - bimetal deflection 'reshaped' Y (norm_avrg_reshaped, i.e. after reshaping to 0.8 ==> 1)
%       5 - X coordinate of ball
%       6 - Y coordinate of ball
%       7 - X speed of ball
%       8 - Y speed of ball
%       9 - Obstacle hit, yes/no (1/0) - per frame
%       10 - Target hit, yes/no (1/0) - per frame   %%%%%%%%%%%%% ALWAYS 1 EXCEPT AT END OF THIS TRIAL's FRAMES...
%       11 - Target hit, ID (1,2,3,4) - per frame
%       12 - Obstacle hit, yes/no (1/0) - collection events ONLY
%       13 - Target hit, yes/no (1/0) - collection events ONLY
%       14 - Target hit, ID (1,2,3,4) - collection events ONLY
%       15 - bimetal deflection 'raw' X (mean of AI_x_Samples)
%       16 - bimetal deflection 'raw' Y (mean of AI_y_Samples)
%       17 - bimetal deflection 'medium' X (norm_avrg, i.e. after calibration)
%       18 - bimetal deflection 'medium' Y (norm_avrg, i.e. after calibration)
%       19 - X force on ball (Fx, considering influence of one or both players, depending on trial type)
%       20 - Y force on ball (Fy, considering influence of one or both players, depending on trial type)
%       21 - marker of especially good play
%		22-30 - yes/no (1/0) in proximity to obstacle number 1 to 9, 
%		31 - yes/no (1/0) in proximity to any obstacle
%		32 - who sees the obstacle in proximity? (0 = nobody, 1 = Player 1, 2 = Player 2, 3 = both players)

% second dimension = frames (32 seconds with approx. 30 Hz = approx. 960 frames)

% third dimension = trials (20 individual + 100 joint + 20 individual = 140 trials)
%   if you want to know the difference between collaborative play with SAME or DIFFerent 
%   obstacle-visibility for both players, check in the pair-information in column 3 of Data_BallGame_4pairs.
%   there is an entry called 'trialtype': 1-5 = individual play, 11-15 = joint DIFFerent, 21-25 = joint SAME


%% 2. additional information (questionnaires, demographics), 6x2 cell "meta_info" in meta_info_6pairs.mat

% row# = pair#, column# = player#

% QA_NEO = [Neuroticism Extraversion Openness Vertraeglichkeit Gewissenhaftigkeit]
% QA_general = [hours_sleep drowsiness1_7 enough_food0_1 music_experience0_1 musicActive0_3 PCgaming_experience0_1 PCgaming_active0_3]
% nine_hole_peg = time to complete task with [left right] hand in seconds (faster = better hand motoric ability)

% max possible values, for empathy = 60, for Autistic trait questionnaire (ATQ) FIRST 3 PAIRS = 33 // LAST 3 PAIRS = 50 
%  for NEO in each category = 48


%% 3. Eye tracking data // UPLOADED SOON!

