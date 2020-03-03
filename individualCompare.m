clear;
clc;
close all;

%% import all data
% have to manually change the author each time
A_tab = readtable('WinstonChurchillAFC—V3.csv');
B_tab = readtable('WinstonChurchillRC—V0.csv');
C_tab = readtable('WinstonChurchillOS.csv');
D_tab = readtable('WinstonChurchillMAJ.csv');
E_tab = readtable('WinstonChurchillLR.csv');
F_tab = readtable('WinstonChurchillC—V0.csv');
G_tab = readtable('WinstonChurchillAFOF.csv');
com = readtable('WinstonChurchillComposite.csv');

%% convert to matrix
WC1 = table1array(A_tab);
WC2 = table1array(B_tab);
WC3 = table1array(C_tab);
WC4 = table1array(D_tab);
WC5 = table1array(E_tab);
WC6 = table1array(F_tab);
WC7 = table1array(G_tab);
WCC = table1array(com);

%% calculate one norm for each composite matrix
ntc = 1;

NWCC = norm(WCC,ntc);
NACDC = norm(ACDC,ntc);
NACHC = norm(ACHC,ntc);
NEGC = norm(EGC,ntc);
NEHC = norm(EHC,ntc);
NGBNC = norm(GBMC,ntc);
NGPC = norm(GPC,ntc);
NHMGC = norm(HMGC,ntc);
NIBC = norm(IBC,ntc);
NJFC = norm(JFC,ntc);

%% create a vector that stores the 1 norm of all composite matrices
NC = 100 .* [NWCC, NACDC, NACHC, NEGC, NEHC, NGBNC, NGPC, NHMGC, NIBC, NJFC];

NC = sort(NC);

%% create the matrix norm for each novel

nt = 2; % norm type

NWC = [norm(WC1,nt), norm(WC2,nt), norm(WC3,nt), norm(WC4,nt), norm(WC5,nt), norm(WC6,nt), norm(WC7,nt)];
NACD = [norm(ACD1,nt), norm(ACD2,nt), norm(ACD3,nt), norm(ACD4,nt), norm(ACD5,nt), norm(ACD6,nt), norm(ACD7,nt)];
NACH = [norm(ACH1,nt), norm(ACH2,nt), norm(ACH3,nt), norm(ACH4,nt), norm(ACH5,nt), norm(ACH6,nt), norm(ACH7,nt)];
NEG = [norm(EG1,nt), norm(EG2,nt), norm(EG3,nt), norm(EG4,nt), norm(EG5,nt), norm(EG6,nt), norm(EG7,nt)];
NEH = [norm(EH1,nt), norm(EH2,nt), norm(EH3,nt), norm(EH4,nt), norm(EH5,nt), norm(EH6,nt), norm(EH7,nt)];
NGBM = [norm(GBM1,nt), norm(GBM2,nt), norm(GBM3,nt), norm(GBM4,nt), norm(GBM5,nt), norm(GBM6,nt), norm(GBM7,nt)];
NGP = [norm(GP1,nt), norm(GP2,nt), norm(GP3,nt), norm(GP4,nt), norm(GP5,nt), norm(GP6,nt), norm(GP7,nt)];
NHMG = [norm(HMG1,nt), norm(HMG2,nt), norm(HMG3,nt), norm(HMG4,nt), norm(HMG5,nt), norm(HMG6,nt), norm(HMG7,nt)];
NIB = [norm(IB1,nt), norm(IB2,nt), norm(IB3,nt), norm(IB4,nt), norm(IB5,nt), norm(IB6,nt), norm(IB7,nt)];
NJF = [norm(JF1,nt), norm(JF2,nt), norm(JF3,nt), norm(JF4,nt), norm(JF5,nt), norm(JF6,nt), norm(JF7,nt)];

NWC = sort(NWC);
NACD = sort(NACD);
NACH = sort(NACH);
NEG = sort(NEG);
NEH = sort(NEH);
NGBM = sort(NGBM);
NGP = sort(NGP);
NHMG = sort(NHMG);
NIB = sort(NIB);
NJF = sort(NJF);

%% try data fitting

length = [1,2,3,4,5,6,7];
pricise = 2;

pNWC = polyfit(length, NWC, pricise);
pNACD = polyfit(length, NACD, pricise);
pNACH = polyfit(length, NACH, pricise);
pNEG = polyfit(length, NEG, pricise);
pNEH = polyfit(length, NEH, pricise);
pNGBM = polyfit(length, NGBM, pricise);
pNGP = polyfit(length, NGP, pricise);
pNHMG = polyfit(length, NHMG, pricise);
pNIB = polyfit(length, NIB, pricise);
pNJF = polyfit(length, NJF, pricise);

pAll = [pNWC;pNACD;pNACH;pNEG;pNEH;pNGBM;pNGP;pNHMG;pNIB;pNJF];
pAll = 10000 .* pAll;
pAll(:,1)

% plot(length, NWC)
% hold on
% plot(length, NJF)
% plot(length, NACD)
% plot(length, NACH)
% plot(length, NEG)
% plot(length, NEH)
% plot(length, NGBM)
% plot(length, NGP)
% plot(length, NHMG)
% plot(length, NIB)



%% polyfit
x = linspace(0,7);


y1 = polyval(pNWC,x);
y2 = polyval(pNACD,x);
y3 = polyval(pNACH,x);
y4 = polyval(pNEG,x);
y5 = polyval(pNEH,x);
y6 = polyval(pNGBM,x);
y7 = polyval(pNGP,x);
y8 = polyval(pNHMG,x);
y9 = polyval(pNIB,x);
y10 = polyval(pNJF,x);

plot(x,y1)
hold on
plot(x,y2)
plot(x,y3)
plot(x,y4)
plot(x,y5)
plot(x,y6)
plot(x,y7)
plot(x,y8)
plot(x,y9)
plot(x,y10)
hold off


%% distance between point and line
