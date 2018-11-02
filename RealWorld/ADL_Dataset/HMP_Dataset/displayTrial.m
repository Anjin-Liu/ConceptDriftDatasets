function displayTrial(trial)
% function displayTrial(trial)
%
% displayTrial plots the acceleration recorded in the given accelerometer
% trial. Acceleration data are decoded and filtered with median filtering.
%
% Input:
%   trial --> name of the accelerometer trial to be displayed
%
% Output:
%   ---
%
% Example:
%   trial = 'Climb_stairs\Accelerometer-2011-03-24-10-24-39-climb_stairs-f1.txt';
%   displayTrial(trial);

% READ THE ACCELEROMETER DATA FILE
dataFile = fopen(trial,'r');
data = fscanf(dataFile,'%d\t%d\t%d\n',[3,inf]);

% CONVERT THE ACCELEROMETER DATA INTO REAL ACCELERATION VALUES
% mapping from [0..63] to [-14.709..+14.709]
noisy_x = -14.709 + (data(1,:)/63)*(2*14.709);
noisy_y = -14.709 + (data(2,:)/63)*(2*14.709);
noisy_z = -14.709 + (data(3,:)/63)*(2*14.709);

% REDUCE THE NOISE ON THE SIGNALS BY MEDIAN FILTERING
n = 3;      % order of the median filter
x = medfilt1(noisy_x,n);
y = medfilt1(noisy_y,n);
z = medfilt1(noisy_z,n);
numSamples = length(x);

% DISPLAY THE RESULTS
time = 1:1:numSamples;
% noisy signal
figure,
    subplot(3,1,1);
    plot(time,noisy_x,'-');
    axis([0 numSamples -14.709 +14.709]);
    title('Noisy accelerations along the x axis');
    subplot(3,1,2);
    plot(time,noisy_y,'-');
    axis([0 numSamples -14.709 +14.709]);
    ylabel('acceleration [m/s^2]');
    title('Noisy accelerations along the y axis');
    subplot(3,1,3);
    plot(time,noisy_z,'-');
    axis([0 numSamples -14.709 +14.709]);
    xlabel('time [samples]');
    title('Noisy accelerations along the z axis');
% clean signal
figure,
    subplot(3,1,1);
    plot(time,x,'-');
    axis([0 numSamples -14.709 +14.709]);
    title('Filtered accelerations along the x axis');
    subplot(3,1,2);
    plot(time,y,'-');
    axis([0 numSamples -14.709 +14.709]);
    ylabel('acceleration [m/s^2]');
    title('Filtered accelerations along the y axis');
    subplot(3,1,3);
    plot(time,z,'-');
    axis([0 numSamples -14.709 +14.709]);
    xlabel('time [samples]');
    title('Filtered accelerations along the z axis');