clc
clear all
close all
%считывание x из первого csv файла
table1=readtable('BTSX_BTC_EUR_200101_210101.csv');
% table1=readtable('MOEX_180101_190101.csv');
x=table1{1:end,5};
%считывание y из второго csv файла
table2=readtable('GDAX_ETH-EUR_200101_210101.csv');
% table2=readtable('broken.csv');
% table2=readtable('GAZP_180101_190101.csv');
y=table2{1:end,5};
n=length(x)
%---------------------------------------------------------------------------------------------
% ѕо методике »рвина найти аномальные данные и заменить их на данные, не выбивающиес€ из общего тренда.
%данные вычислени€ I_pred
n_pred=[2 3 10 20 30 50 100 400];
alpha=0.05;
I_pred=[2.8 2.2 1.5 1.3 1.2 1.1 1 0.9];
% alpha=0.01;
% I_pred=[3.7 2.9 2 1.8 1.7 1.6 1.5 1.3];
%предполагаетс€, что n>=2 и n<=400
I_predel=0;
for i=1:length(n_pred)
    if n==n_pred(i)
        I_predel=I_pred(i);
        break
    end
    if n<n_pred(i)
        k=(I_pred(i)-I_pred(i-1))/(n_pred(i)-n_pred(i-1));
        I_predel=k*n+I_pred(i)-n_pred(i)*k;
%         I_predel=n*(I_pred(i)-I_pred(i-1))/(n_pred(i)-n_pred(i-1))+...
%             (I_pred(i-1)*n_pred(i)-I_pred(i)*n_pred(i-1))/(n_pred(i)-n_pred(i-1));
        break
    end
end
I_predel
x_=sum(x)/n;
y_=sum(y)/n;
S=sqrt(sum((y-y_).^2)/(n-1));
I=abs(y(2:end)-y(1:end-1))/S;
xy_=sum(x.*y)/n;
xx_=sum(x.*x)/n;
b=(xy_-x_*y_)/(xx_-x_*x_) 
a=y_-b*x_
%эксперементальные точки и пр€маю регрессии
y_pr=a+b*x;
plot(x,y,'*',x,y_pr)
hold on
%отмечу аномальные точки
y_bez_anomal=y;
for i=2:n
    if I(i-1)>=I_predel
        plot(x(i),y(i),'*r')
        if i==n
            y_bez_anomal(i)=(y_bez_anomal(i)+y_bez_anomal(i-1))/2;
            break
        end
        y_bez_anomal(i)=(y_bez_anomal(i+1)+y_bez_anomal(i-1))/2;
    end
end
%построю график с исправленными аномальными точками
figure
plot(x,y_bez_anomal,'*',x,y_pr)
%--------------------------------------------------------------------------------
%ѕроверить гипотезу о наличии неслучайных компонент по критерию —тьюдента или по методу серий.
%----------------ћетод серий-----------------
y_sort=sort(y);
y_med=median(y_sort)
%если встроенный метод нельз€ использовать
% if mod(n,2)==0
%     %значит четное n
%     y_med=(y_sort(n/2)+y_sort(n/2+1))/2;
% else
%     y_med=y_sort((n+1)/2);
% end
t=0;
if y(1)>=y_med
        t=1;
    else
        t=0;
end
Nu=1;
tau=0;
k=1;
for i=2:n
    t_last=t;
    if y(i)>=y_med
        t=1;
    else
        t=0;
    end
    if t_last~=t
        Nu=Nu+1;
        if tau<k
            tau=k;
        end
        k=1;        
    else
        k=k+1;
        if tau<k
            tau=k;
        end
    end
end
%проверка гипотезы
%кака€ то хренатень
if tau>floor((n+2-1.96*sqrt(n-1))/2)
    if Nu<floor(1.43*log(n+1))
        %принимаетс€ гипотеза
        disp('случайных компонент нет')
    end
else
    disp('случайные компоненты есть')
end
%-----------------------------------------------------------------------
%на глаз уже можно определить, есть ли зависимость y от x( в примере это эфир от битка)
%коэффициент детерминации R^2
% Q_ost=sum((y-y_pr).^2);
% Q_obsh=sum((y-y_).^2);
% R_2=1-Q_ost/Q_obsh
% e=(y-y_pr);