 clear all; close all; clc;
n = 10000;
stat_arr =[];
for i = 1:n
X = gamrnd(3,1,30,1); Y = gamrnd(3,1,47,1);
[~,~,~,stats] = ttest2(X,Y);
stat_arr = [stat_arr stats.tstat];
end
ecdf(stat_arr)
hold on; grid on
norm = [-3:0.1:3];
norm_cdf = normcdf(norm, 0 ,1);
plot(norm,norm_cdf,'--')
legend('ecdf','normcdf')


stat_arr =[]; 
for i = 1:n
X = gamrnd(3,1,30,1);
Y = gamrnd(5,1,47,1);
[~,~,~,stats] = ttest2(X,Y);
stat_arr = [stat_arr stats.tstat];
end
stat_mean = mean(stat_arr);
figure
ecdf(stat_arr)
hold on; grid on
norm = [-7.5:0.1:-1];
norm_cdf = normcdf(norm, stat_mean ,1);
plot(norm,norm_cdf,'--')
legend('ecdf','normcdf')