clear all; close all; clc;
n = 10000;
nx = 30; ny = 47;
m = nx*(nx+ny+1)/2; s = sqrt(nx*ny*(nx+ny+1)/12);
stat_arr =[];
for i = 1:n
X = gamrnd(3,1,nx,1); Y = gamrnd(3,1,ny,1);
[~,~,stats] = ranksum(X,Y);
wstat = (stats.ranksum - m)/s;
stat_arr = [stat_arr wstat];
end
ecdf(stat_arr)
hold on; grid on
norm = [-3:0.1:3];
norm_cdf = normcdf(norm, 0 ,1);
plot(norm,norm_cdf,'--')
legend('ecdf','normcdf')


stat_arr =[];
for i = 1:n
X = gamrnd(3,1,nx,1); Y = gamrnd(5,1,ny,1);
[~,~,stats] = ranksum(X,Y);
wstat = (stats.ranksum - m)/s;
stat_arr = [stat_arr wstat];
end
figure
ecdf(stat_arr)
hold on; grid on
norm = [-6:0.1:-1];
m = mean(stat_arr); s = std(stat_arr);
norm_cdf = normcdf(norm, m ,s);
plot(norm,norm_cdf,'--')
legend('ecdf','normcdf')