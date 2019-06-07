clear;

data = load('data0.mat');
data0 = data.data0;
data = load('data1.mat');
data1 = data.data1;

mp = length(data0);
mq = length(data1);

batchSize = 1000;

for i = 1:150
    rng(i+batchSize);
    
    shuffInd = randperm( mq, batchSize);
    realData0 = data1(shuffInd,1:4);
    
    shuffInd = randperm( mq, batchSize);
    realData1 = data1(shuffInd,1:4);
    
    outfilePaht = strcat('./c/q_q_',int2str(i),'.csv');
    csvwrite(outfilePaht, [realData0;realData1]);
    
end