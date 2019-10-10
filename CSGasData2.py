
import BlockData

global name, ip, comp, awt, nspec, natom, itab, ntab, indx, iprint, gsinit, print0 #/gasp/
global ipr, nch, nel, ntot, nat, zat, neut, idel, indsp, indzat, iat, natsp, iatsp #/gasp2/

ip = BlockData.ip
comp = BlockData.comp
awt = BlockData.awt
name = BlockData.name
ipr = BlockData.ipr
nch = BlockData.nch
nel = BlockData.nel
nat = BlockData.nat
zat = BlockData.zat

logk = [ [0.0e0 for i in range(150)] for j in range(5) ]
logwt = [0.0e0 for i in range(150)]

name[0] = "H";      ipr[0] = 1; nch[0] =  0; nel[0] = 1; nat[0][0] = 1;  zat[0][0] = 1;  awt[0] =  1.008; comp[0] = 9.32e-01
name[1] = "H+";     ipr[1] = 1; nch[1] = +1; ip[1] = 13.598;  logwt[1] = 0.000
name[2] = "H-";     ipr[2] = 1; nch[2] = -1; ip[2] =  0.754;  logwt[2] = 0.600
name[3] = "He";     ipr[3] = 2; nch[3] =  0; nel[3] = 1; nat[0][3] = 1;  zat[0][3] = 2;  awt[3] =  4.003; comp[1] = 6.53e-02
name[4] = "He+";    ipr[4] = 2; nch[4] = +1; ip[4] = 24.587;  logwt[4] = 0.600
name[5] = "C";      ipr[5] = 1; nch[5] =  0; nel[5] = 1; nat[0][5] = 1;  zat[0][5] = 6;  awt[5] = 12.011; comp[2] = 4.94e-04
name[6] = "C+";     ipr[6] = 1; nch[6] = +1; ip[6] = 11.260;  logwt[6] = 0.100
name[7] = "N";      ipr[7] = 1; nch[7] =  0; nel[7] = 1; nat[0][7] = 1;  zat[0][7] = 7;  awt[7] = 14.007; comp[3] = 8.95e-04
name[8] = "N+";     ipr[8] = 1; nch[8] = +1; ip[8] = 14.534;  logwt[8] = 0.650
name[9] = "O";      ipr[9] = 1; nch[9] =  0; nel[9] = 1; nat[0][9] = 1;  zat[0][9] = 8;  awt[9] = 16.000; comp[4] = 8.48e-04
name[10] = "O+";    ipr[10] = 1; nch[10] = +1; ip[10] = 13.618; logwt[10] = -0.050
name[11] = "Ne";    ipr[11] = 2; nch[11] =  0; nel[11] = 1; nat[0][11] = 1;  zat[0][11] = 10; awt[11] = 20.179; comp[5] = 7.74e-05
name[12] = "Ne+";   ipr[12] = 2; nch[12] = +1; ip[12] = 21.564;  logwt[12] = 1.080
name[13] = "Na";    ipr[13] = 2; nch[13] =  0; nel[13] = 1; nat[0][13] = 1;  zat[0][13] = 11; awt[13] = 22.990; comp[6] = 1.68e-06
name[14] = "Na+";   ipr[14] = 2; nch[14] = +1; ip[14] =  5.139;  logwt[14] = 0.000
name[15] = "Mg";    ipr[15] = 2; nch[15] =  0; nel[15] = 1; nat[0][15] = 1;  zat[0][15] = 12; awt[15] = 24.305; comp[7] = 2.42e-05
name[16] = "Mg+";   ipr[16] = 2; nch[16] = +1; ip[16] =  7.644;  logwt[16] = 0.600
name[17] = "Mg++";  ipr[17] = 2; nch[17] = +2; ip[17] = 15.031;  logwt[17] = 0.000
name[18] = "Al";    ipr[18] = 2; nch[18] =  0; nel[18] = 1; nat[0][18] = 1;  zat[0][18] = 13; awt[18] = 26.982; comp[8] = 2.24e-06
name[19] = "Al+";   ipr[19] = 2; nch[19] = +1; ip[19] =  5.984; logwt[19] = -0.480
name[20] = "Si";    ipr[20] = 1; nch[20] =  0; nel[20] = 1; nat[0][20] = 1;  zat[0][20] = 14; awt[20] = 28.086; comp[9] = 3.08e-05
name[21] = "Si+";   ipr[21] = 1; nch[21] = +1; ip[21] =  8.149;  logwt[21] = 0.120
name[22] = "S";     ipr[22] = 1; nch[22] =  0; nel[22] = 1; nat[0][22] = 1;  zat[0][22] = 16; awt[22] = 32.060; comp[10] = 1.49e-05
name[23] = "S+";    ipr[23] = 1; nch[23] = +1; ip[23] = 10.360; logwt[23] = -0.050
name[24] = "Cl";    ipr[24] = 3; nch[24] =  0; nel[24] = 1; nat[0][24] = 1;  zat[0][24] = 17; awt[24] = 35.453; comp[11] = 3.73e-07
name[25] = "Cl-";   ipr[25] = 3; nch[25] = -1; ip[25] =  3.613;  logwt[25] = 1.080
name[26] = "K";     ipr[26] = 2; nch[26] =  0; nel[26] = 1; nat[0][26] = 1;  zat[0][26] = 19; awt[26] = 39.102; comp[12] = 8.30e-08
name[27] = "K+";    ipr[27] = 2; nch[27] = +1; ip[27] =  4.339;  logwt[27] = 0.000
name[28] = "Ca";    ipr[28] = 2; nch[28] =  0; nel[28] = 1; nat[0][28] = 1;  zat[0][28] = 20; awt[28] = 40.080; comp[13] = 1.86e-06
name[29] = "Ca+";   ipr[29] = 2; nch[29] = +1; ip[29] =  6.111;  logwt[29] = 0.600
name[30] = "Ca++";  ipr[30] = 2; nch[30] = +2; ip[30] = 11.868;  logwt[30] = 0.000
name[31] = "Sc";    ipr[31] = 3; nch[31] =  0; nel[31] = 1; nat[0][31] = 1;  zat[0][31] = 21; awt[31] = 44.956; comp[14] = 1.49e-09
name[32] = "Sc+";   ipr[32] = 3; nch[32] = +1; ip[32] =  6.540;  logwt[32] = 0.480
name[33] = "Ti";    ipr[33] = 3; nch[33] =  0; nel[33] = 1; nat[0][33] = 1;  zat[0][33] = 22; awt[33] = 47.900; comp[15] = 1.21e-07
name[34] = "Ti+";   ipr[34] = 3; nch[34] = +1; ip[34] =  6.820;  logwt[34] = 0.430
name[35] = "V";     ipr[35] = 3; nch[35] =  0; nel[35] = 1; nat[0][35] = 1;  zat[0][35] = 23; awt[35] = 50.941; comp[16] = 2.33e-08
name[36] = "V+";    ipr[36] = 3; nch[36] = +1; ip[36] =  6.740;  logwt[36] = 0.250
name[37] = "Cr";    ipr[37] = 3; nch[37] =  0; nel[37] = 1; nat[0][37] = 1;  zat[0][37] = 24; awt[37] = 51.996; comp[17] = 6.62e-07
name[38] = "Cr+";   ipr[38] = 3; nch[38] = +1; ip[38] =  6.766;  logwt[38] = 0.230
name[39] = "Mn";    ipr[39] = 3; nch[39] =  0; nel[39] = 1; nat[0][39] = 1;  zat[0][39] = 25; awt[39] = 54.938; comp[18] = 2.33e-07
name[40] = "Mn+";   ipr[40] = 3; nch[40] = +1; ip[40] =  7.435;  logwt[40] = 0.370
name[41] = "Fe";    ipr[41] = 2; nch[41] =  0; nel[41] = 1; nat[0][41] = 1;  zat[0][41] = 26; awt[41] = 55.847; comp[19] = 3.73e-05
name[42] = "Fe+";   ipr[42] = 2; nch[42] = +1; ip[42] =  7.870;  logwt[42] = 0.380
name[43] = "Co";    ipr[43] = 3; nch[43] =  0; nel[43] = 1; nat[0][43] = 1;  zat[0][43] = 27; awt[43] = 58.933; comp[20] = 1.12e-07
name[44] = "Co+";   ipr[44] = 3; nch[44] = +1; ip[44] =  7.860;  logwt[44] = 0.180
name[45] = "Ni";    ipr[45] = 2; nch[45] =  0; nel[45] = 1; nat[0][45] = 1;  zat[0][45] = 28; awt[45] = 58.710; comp[21] = 1.86e-06
name[46] = "Ni+";   ipr[46] = 2; nch[46] = +1; ip[46] =  7.635; logwt[46] = -0.020
name[47] = "Sr";    ipr[47] = 3; nch[47] =  0; nel[47] = 1; nat[0][47] = 1;  zat[0][47] = 38; awt[47] = 87.620; comp[22] = 6.62e-10
name[48] = "Sr+";   ipr[48] = 3; nch[48] = +1; ip[48] =  5.695;  logwt[48] = 0.500
name[49] = "Y";     ipr[49] = 3; nch[49] =  0; nel[49] = 1; nat[0][49] = 1;  zat[0][49] = 39; awt[49] = 88.906; comp[23] = 5.87e-11
name[50] = "Y+";    ipr[50] = 3; nch[50] = +1; ip[50] =  6.380;  logwt[50] = 0.500
name[51] = "Zr";    ipr[51] = 3; nch[51] =  0; nel[51] = 1; nat[0][51] = 1;  zat[0][51] = 40; awt[51] = 91.220; comp[24] = 2.98e-10
name[52] = "Zr+";   ipr[52] = 3; nch[52] = +1; ip[52] =  6.840;  logwt[52] = 0.420
name[53] = "H2";    ipr[53] = 1; nch[53] =  0; nel[53] = 1; nat[0][53] = 2;  zat[0][53] = 1;           logk[0][53] = 12.739; logk[1][53] = -5.1172;  logk[2][53] = 0.12572; logk[3][53] = -1.4149e-02; logk[4][53] = 6.3021e-04
name[54] = "H2+";   ipr[54] = 1; nch[54] = +1; ip[54] = 15.422;  logwt[54] = 0.600
name[55] = "C2";    ipr[55] = 1; nch[55] =  0; nel[55] = 1; nat[0][55] = 2;  zat[0][55] = 6;           logk[0][55] = 12.804; logk[1][55] = -6.5178;  logk[2][55] = .097719; logk[3][55] = -1.2739e-02;  logk[4][55] = 6.2603e-04
name[56] = "C3";    ipr[56] = 1; nch[56] =  0; nel[56] = 1; nat[0][56] = 3;  zat[0][56] = 6;           logk[0][56] = 25.230; logk[1][56] = -14.445;  logk[2][56] = 0.12547; logk[3][56] = -1.7390e-02;  logk[4][56] = 8.8594e-04
name[57] = "N2";    ipr[57] = 1; nch[57] =  0; nel[57] = 1; nat[0][57] = 2; zat[0][57] = 7;           logk[0][57] = 13.590; logk[1][57] = -10.585;  logk[2][57] = 0.22067; logk[3][57] = -2.9997e-02;  logk[4][57] = 1.4993e-03
name[58] = "O2";    ipr[58] = 1; nch[58] =  0; nel[58] = 1; nat[0][58] = 2; zat[0][58] = 8;           logk[0][58] = 13.228; logk[1][58] = -5.5181;  logk[2][58] = .069935; logk[3][58] = -8.1511e-03;  logk[4][58] = 3.7970e-04
name[59] = "CH";    ipr[59] = 1; nch[59] =  0; nel[59] = 2; nat[0][59] = 1; zat[0][59] = 6;  nat[1][59] = 1;  zat[1][59] = 1;  nat[2][59] = 0;  zat[2][59] = 0; logk[0][59] = 12.135; logk[1][59] = -4.0760; logk[2][59] =  0.12768; logk[3][59] = -1.5473e-02; logk[4][59] =  7.2661e-04
name[60] = "C2H2";  ipr[60] = 1; nch[60] =  0; nel[60] = 2; nat[0][60] = 2; zat[0][60] = 6;  nat[1][60] = 2;  zat[1][60] = 1;  nat[2][60] = 0;  zat[2][60] = 0; logk[0][60] = 38.184; logk[1][60] = -17.365; logk[2][60] =  .021512; logk[3][60] = -8.8961e-05; logk[4][60] = -2.8720e-05
name[61] = "NH";    ipr[61] = 1; nch[61] =  0; nel[61] = 2; nat[0][61] = 1; zat[0][61] = 7;  nat[1][61] = 1;  zat[1][61] = 1;  nat[2][61] = 0;  zat[2][61] = 0; logk[0][61] = 12.033; logk[1][61] = -3.8435; logk[2][61] =  0.13629; logk[3][61] = -1.6643e-02; logk[4][61] =  7.8691e-04
name[62] = "NH2";   ipr[62] = 1; nch[62] =  0; nel[62] = 2; nat[0][62] = 1; zat[0][62] = 7;  nat[1][62] = 2;  zat[1][62] = 1;  nat[2][62] = 0;  zat[2][62] = 0; logk[0][62] = 24.603; logk[1][62] = -8.6300; logk[2][62] =  0.20048; logk[3][62] = -2.4124e-02; logk[4][62] =  1.1484e-03
name[63] = "NH3";   ipr[63] = 1; nch[63] =  0; nel[63] = 2; nat[0][63] = 1; zat[0][63] = 7;  nat[1][63] = 3;  zat[1][63] = 1;  nat[2][63] = 0;  zat[2][63] = 0; logk[0][63] = 37.554; logk[1][63] = -13.059; logk[2][63] =  0.12910; logk[3][63] = -1.2338e-02; logk[4][63] =  5.3429e-04
name[64] = "OH";    ipr[64] = 1; nch[64] =  0; nel[64] = 2; nat[0][64] = 1; zat[0][64] = 8;  nat[1][64] = 1;  zat[1][64] = 1;  nat[2][64] = 0;  zat[2][64] = 0; logk[0][64] = 12.371; logk[1][64] = -5.0578; logk[2][64] =  0.13822; logk[3][64] = -1.6547e-02; logk[4][64] =  7.7224e-04
name[65] = "MgH";   ipr[65] = 2; nch[65] =  0; nel[65] = 2; nat[0][65] = 1; zat[0][65] = 12; nat[1][65] = 1;  zat[1][65] = 1;  nat[2][65] = 0;  zat[2][65] = 0; logk[0][65] = 11.285; logk[1][65] = -2.7164; logk[2][65] =  0.19658; logk[3][65] = -2.7310e-02; logk[4][65] =  1.3816e-03
name[66] = "AlH";   ipr[66] = 2; nch[66] =  0; nel[66] = 2; nat[0][66] = 1; zat[0][66] = 13; nat[1][66] = 1;  zat[1][66] = 1;  nat[2][66] = 0;  zat[2][66] = 0; logk[0][66] = 12.191; logk[1][66] = -3.7636; logk[2][66] =  0.25557; logk[3][66] = -3.7261e-02; logk[4][66] =  1.9406e-03
name[67] = "SiH";   ipr[67] = 1; nch[67] =  0; nel[67] = 2; nat[0][67] = 1; zat[0][67] = 14; nat[1][67] = 1;  zat[1][67] = 1;  nat[2][67] = 0;  zat[2][67] = 0; logk[0][67] = 11.852; logk[1][67] = -3.7418; logk[2][67] =  0.15999; logk[3][67] = -2.0629e-02; logk[4][67] =  9.9897e-04
name[68] = "HS";    ipr[68] = 1; nch[68] =  0; nel[68] = 2; nat[0][68] = 1; zat[0][68] = 16; nat[1][68] = 1;  zat[1][68] = 1;  nat[2][68] = 0;  zat[2][68] = 0; logk[0][68] = 12.019; logk[1][68] = -4.2922; logk[2][68] =  0.14913; logk[3][68] = -1.8666e-02; logk[4][68] =  8.9438e-04
name[69] = "H2S";   ipr[69] = 1; nch[69] =  0; nel[69] = 2; nat[0][69] = 1; zat[0][69] = 16; nat[1][69] = 2;  zat[1][69] = 1;  nat[2][69] = 0;  zat[2][69] = 0; logk[0][69] = 24.632; logk[1][69] = -8.4616; logk[2][69] =  0.17014; logk[3][69] = -2.0236e-02; logk[4][69] =  9.5782e-04
name[70] = "HCl";   ipr[70] = 3; nch[70] =  0; nel[70] = 2; nat[0][70] = 1; zat[0][70] = 17; nat[1][70] = 1;  zat[1][70] = 1;  nat[2][70] = 0;  zat[2][70] = 0; logk[0][70] = 12.528; logk[1][70] = -5.1827; logk[2][70] =  0.18117; logk[3][70] = -2.4014e-02; logk[4][70] =  1.1994e-03
name[71] = "CaH";   ipr[71] = 3; nch[71] =  0; nel[71] = 2; nat[0][71] = 1; zat[0][71] = 20; nat[1][71] = 1;  zat[1][71] = 1;  nat[2][71] = 0;  zat[2][71] = 0; logk[0][71] = 11.340; logk[1][71] = -3.0144; logk[2][71] =  0.42349; logk[3][71] = -6.1467e-02; logk[4][71] =  3.1639e-03
name[72] = "CN";    ipr[72] = 1; nch[72] =  0; nel[72] = 2; nat[0][72] = 1; zat[0][72] = 7;  nat[1][72] = 1;  zat[1][72] = 6;  nat[2][72] = 0;  zat[2][72] = 0; logk[0][72] = 12.805; logk[1][72] = -8.2793; logk[2][72] =  .064162; logk[3][72] = -7.3627e-03; logk[4][72] =  3.4666e-04
name[73] = "NO";    ipr[73] = 1; nch[73] =  0; nel[73] = 2; nat[0][73] = 1; zat[0][73] = 8;  nat[1][73] = 1;  zat[1][73] = 7;  nat[2][73] = 0;  zat[2][73] = 0; logk[0][73] = 12.831; logk[1][73] = -7.1964; logk[2][73] =  0.17349; logk[3][73] = -2.3065e-02; logk[4][73] =  1.1380e-03
name[74] = "CO";    ipr[74] = 1; nch[74] =  0; nel[74] = 2; nat[0][74] = 1; zat[0][74] = 8;  nat[1][74] = 1;  zat[1][74] = 6;  nat[2][74] = 0;  zat[2][74] = 0; logk[0][74] = 13.820; logk[1][74] = -11.795; logk[2][74] =  0.17217; logk[3][74] = -2.2888e-02; logk[4][74] =  1.1349e-03
name[75] = "CO2";   ipr[75] = 1; nch[75] =  0; nel[75] = 2; nat[0][75] = 2; zat[0][75] = 8;  nat[1][75] = 1;  zat[1][75] = 6;  nat[2][75] = 0;  zat[2][75] = 0; logk[0][75] = 27.478; logk[1][75] = -17.098; logk[2][75] =  .095012; logk[3][75] = -1.2579e-02; logk[4][75] =  6.4058e-04
name[76] = "MgO";   ipr[76] = 3; nch[76] =  0; nel[76] = 2; nat[0][76] = 1; zat[0][76] = 12; nat[1][76] = 1;  zat[1][76] = 8;  nat[2][76] = 0;  zat[2][76] = 0; logk[0][76] = 11.702; logk[1][76] = -5.0326; logk[2][76] =  0.29641; logk[3][76] = -4.2811e-02; logk[4][76] =  2.2023e-03
name[77] = "AlO";   ipr[77] = 2; nch[77] =  0; nel[77] = 2; nat[0][77] = 1; zat[0][77] = 13; nat[1][77] = 1;  zat[1][77] = 8;  nat[2][77] = 0;  zat[2][77] = 0; logk[0][77] = 12.739; logk[1][77] = -5.2534; logk[2][77] =  0.18218; logk[3][77] = -2.5793e-02; logk[4][77] =  1.3185e-03
name[78] = "SiO";   ipr[78] = 1; nch[78] =  0; nel[78] = 2; nat[0][78] = 1; zat[0][78] = 14; nat[1][78] = 1;  zat[1][78] = 8;  nat[2][78] = 0;  zat[2][78] = 0; logk[0][78] = 13.413; logk[1][78] = -8.8710; logk[2][78] =  0.15042; logk[3][78] = -1.9581e-02; logk[4][78] =  9.4828e-04
name[79] = "SO";    ipr[79] = 1; nch[79] =  0; nel[79] = 2; nat[0][79] = 1; zat[0][79] = 16; nat[1][79] = 1;  zat[1][79] = 8;  nat[2][79] = 0;  zat[2][79] = 0; logk[0][79] = 12.929; logk[1][79] = -6.0100; logk[2][79] =  0.16253; logk[3][79] = -2.1665e-02; logk[4][79] =  1.0676e-03
name[80] = "CaO";   ipr[80] = 2; nch[80] =  0; nel[80] = 2; nat[0][80] = 1; zat[0][80] = 20; nat[1][80] = 1;  zat[1][80] = 8;  nat[2][80] = 0;  zat[2][80] = 0; logk[0][80] = 12.260; logk[1][80] = -6.0525; logk[2][80] =  0.58284; logk[3][80] = -8.5805e-02; logk[4][80] =  4.4425e-03
name[81] = "ScO";   ipr[81] = 3; nch[81] =  0; nel[81] = 2; nat[0][81] = 1; zat[0][81] = 21; nat[1][81] = 1;  zat[1][81] = 8;  nat[2][81] = 0;  zat[2][81] = 0; logk[0][81] = 13.747; logk[1][81] = -8.6420; logk[2][81] =  0.48072; logk[3][81] = -6.9670e-02; logk[4][81] =  3.5747e-03
name[82] = "ScO2";  ipr[82] = 3; nch[82] =  0; nel[82] = 2; nat[0][82] = 1; zat[0][82] = 21; nat[1][82] = 2;  zat[1][82] = 8;  nat[2][82] = 0;  zat[2][82] = 0; logk[0][82] = 26.909; logk[1][82] = -15.824; logk[2][82] =  0.39999; logk[3][82] = -5.9363e-02; logk[4][82] =  3.0875e-03
name[83] = "TiO";   ipr[83] = 2; nch[83] =  0; nel[83] = 2; nat[0][83] = 1; zat[0][83] = 22; nat[1][83] = 1;  zat[1][83] = 8;  nat[2][83] = 0;  zat[2][83] = 0; logk[0][83] = 13.398; logk[1][83] = -8.5956; logk[2][83] =  0.40873; logk[3][83] = -5.7937e-02; logk[4][83] =  2.9287e-03
name[84] = "VO";    ipr[84] = 3; nch[84] =  0; nel[84] = 2; nat[0][84] = 1; zat[0][84] = 23; nat[1][84] = 1;  zat[1][84] = 8;  nat[2][84] = 0;  zat[2][84] = 0; logk[0][84] = 13.811; logk[1][84] = -7.7520; logk[2][84] =  0.37056; logk[3][84] = -5.1467e-02; logk[4][84] =  2.5861e-03
name[85] = "VO2";   ipr[85] = 3; nch[85] =  0; nel[85] = 2; nat[0][85] = 1; zat[0][85] = 23; nat[1][85] = 2;  zat[1][85] = 8;  nat[2][85] = 0;  zat[2][85] = 0; logk[0][85] = 27.754; logk[1][85] = -14.040; logk[2][85] =  0.33613; logk[3][85] = -4.8215e-02; logk[4][85] =  2.4780e-03
name[86] = "YO";    ipr[86] = 3; nch[86] =  0; nel[86] = 2; nat[0][86] = 1; zat[0][86] = 39; nat[1][86] = 1;  zat[1][86] = 8;  nat[2][86] = 0;  zat[2][86] = 0; logk[0][86] = 13.514; logk[1][86] = -8.7775; logk[2][86] =  0.40700; logk[3][86] = -5.8053e-02; logk[4][86] =  2.9535e-03
name[87] = "YO2";   ipr[87] = 3; nch[87] =  0; nel[87] = 2; nat[0][87] = 1; zat[0][87] = 39; nat[1][87] = 2;  zat[1][87] = 8;  nat[2][87] = 0;  zat[2][87] = 0; logk[0][87] = 26.764; logk[1][87] = -16.447; logk[2][87] =  0.39991; logk[3][87] = -5.8916e-02; logk[4][87] =  3.0506e-03
name[88] = "ZrO";   ipr[88] = 3; nch[88] =  0; nel[88] = 2; nat[0][88] = 1; zat[0][88] = 40; nat[1][88] = 1;  zat[1][88] = 8;  nat[2][88] = 0;  zat[2][88] = 0; logk[0][88] = 13.296; logk[1][88] = -9.0129; logk[2][88] =  0.19562; logk[3][88] = -2.9892e-02; logk[4][88] =  1.6010e-03
name[89] = "ZrO2";  ipr[89] = 3; nch[89] =  0; nel[89] = 2; nat[0][89] = 1; zat[0][89] = 40; nat[1][89] = 2;  zat[1][89] = 8;  nat[2][89] = 0;  zat[2][89] = 0; logk[0][89] = 26.793; logk[1][89] = -16.151; logk[2][89] =  0.46988; logk[3][89] = -6.4636e-02; logk[4][89] =  3.2277e-03
name[90] = "CS";    ipr[90] = 1; nch[90] =  0; nel[90] = 2; nat[0][90] = 1; zat[0][90] = 16; nat[1][90] = 1;  zat[1][90] = 6;  nat[2][90] = 0;  zat[2][90] = 0; logk[0][90] = 13.436; logk[1][90] = -8.5574; logk[2][90] =  0.18754; logk[3][90] = -2.5507e-02; logk[4][90] =  1.2735e-03
name[91] = "SiS";   ipr[91] = 1; nch[91] =  0; nel[91] = 2; nat[0][91] = 1; zat[0][91] = 14; nat[1][91] = 1;  zat[1][91] = 16; nat[2][91] = 0;  zat[2][91] = 0; logk[0][91] = 13.182; logk[1][91] = -7.1147; logk[2][91] =  0.19300; logk[3][91] = -2.5826e-02; logk[4][91] =  1.2648e-03
name[92] = "TiS";   ipr[92] = 2; nch[92] =  0; nel[92] = 2; nat[0][92] = 1; zat[0][92] = 22; nat[1][92] = 1;  zat[1][92] = 16; nat[2][92] = 0;  zat[2][92] = 0; logk[0][92] = 13.316; logk[1][92] = -6.2216; logk[2][92] =  0.45829; logk[3][92] = -6.4903e-02; logk[4][92] =  3.2788e-03
name[93] = "SiC";   ipr[93] = 1; nch[93] =  0; nel[93] = 2; nat[0][93] = 1; zat[0][93] = 14; nat[1][93] = 1;  zat[1][93] = 6;  nat[2][93] = 0;  zat[2][93] = 0; logk[0][93] = 12.327; logk[1][93] = -5.0419; logk[2][93] =  0.13941; logk[3][93] = -1.9363e-02; logk[4][93] =  9.6202e-04
name[94] = "SiC2";  ipr[94] = 1; nch[94] =  0; nel[94] = 2; nat[0][94] = 1; zat[0][94] = 14; nat[1][94] = 2;  zat[1][94] = 6;  nat[2][94] = 0;  zat[2][94] = 0; logk[0][94] = 25.623; logk[1][94] = -13.085; logk[2][94] = -.055227; logk[3][94] =  9.3363e-03; logk[4][94] = -4.9876e-04
name[95] = "NaCl";  ipr[95] = 2; nch[95] =  0; nel[95] = 2; nat[0][95] = 1; zat[0][95] = 11; nat[1][95] = 1;  zat[1][95] = 17; nat[2][95] = 0;  zat[2][95] = 0; logk[0][95] = 11.768; logk[1][95] = -4.9884; logk[2][95] =  0.23975; logk[3][95] = -3.4837e-02; logk[4][95] =  1.8034e-03
name[96] = "MgCl";  ipr[96] = 2; nch[96] =  0; nel[96] = 2; nat[0][96] = 1; zat[0][96] = 12; nat[1][96] = 1;  zat[1][96] = 17; nat[2][96] = 0;  zat[2][96] = 0; logk[0][96] = 11.318; logk[1][96] = -4.2224; logk[2][96] =  0.21137; logk[3][96] = -3.0174e-02; logk[4][96] =  1.5480e-03
name[97] = "AlCl";  ipr[97] = 2; nch[97] =  0; nel[97] = 2; nat[0][97] = 1; zat[0][97] = 13; nat[1][97] = 1;  zat[1][97] = 17; nat[2][97] = 0;  zat[2][97] = 0; logk[0][97] = 11.976; logk[1][97] = -5.2228; logk[2][97] = -.010263; logk[3][97] =  3.9344e-03; logk[4][97] = -2.6236e-04
name[98] = "CaCl";  ipr[98] = 2; nch[98] =  0; nel[98] = 2; nat[0][98] = 1; zat[0][98] = 20; nat[1][98] = 1;  zat[1][98] = 17; nat[2][98] = 0;  zat[2][98] = 0; logk[0][98] = 12.314; logk[1][98] = -5.1814; logk[2][98] =  0.56532; logk[3][98] = -8.2868e-02; logk[4][98] =  4.2822e-03
name[99] = "HCN";   ipr[99] = 1; nch[99] =  0; nel[99] = 3; nat[0][99] = 1; zat[0][99] = 7;  nat[1][99] = 1;  zat[1][99] = 6;  nat[2][99] = 1;  zat[2][99] = 1; logk[0][99] = 25.635; logk[1][99] = -13.833; logk[2][99] =  0.13827; logk[3][99] = -1.8122e-02; logk[4][99] =  9.1645e-04
name[100] = "HCO";  ipr[100] = 1; nch[100] =  0; nel[100] = 3; nat[0][100] = 1; zat[0][100] = 8;  nat[1][100] = 1;  zat[1][100] = 6;  nat[2][100] = 1;  zat[2][100] = 1; logk[0][100] = 25.363; logk[1][100] = -13.213; logk[2][100] =  0.18451; logk[3][100] = -2.2973e-02; logk[4][100] =  1.1114e-03
name[101] = "MgOH"; ipr[101] = 2; nch[101] =  0; nel[101] = 3; nat[0][101] = 1; zat[0][101] = 12; nat[1][101] = 1;  zat[1][101] = 8;  nat[2][101] = 1;  zat[2][101] = 1; logk[0][101] = 24.551; logk[1][101] = -9.3818; logk[2][101] =  0.19666; logk[3][101] = -2.7178e-02; logk[4][101] =  1.3887e-03
name[102] = "AlOH"; ipr[102] = 2; nch[102] =  0; nel[102] = 3; nat[0][102] = 1; zat[0][102] = 13; nat[1][102] = 1;  zat[1][102] = 8;  nat[2][102] = 1;  zat[2][102] = 1; logk[0][102] = 25.707; logk[1][102] = -10.624; logk[2][102] =  .097901; logk[3][102] = -1.1835e-02; logk[4][102] =  5.8121e-04
name[103] = "CaOH"; ipr[103] = 2; nch[103] =  0; nel[103] = 3; nat[0][103] = 1; zat[0][103] = 20; nat[1][103] = 1;  zat[1][103] = 8;  nat[2][103] = 1;  zat[2][103] = 1; logk[0][103] = 24.611; logk[1][103] = -10.910; logk[2][103] =  0.60803; logk[3][103] = -8.7197e-02; logk[4][103] =  4.4736e-03

