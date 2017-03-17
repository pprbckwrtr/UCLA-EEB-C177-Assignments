# 1 files combined:
# 	/home/eeb177-student/Desktop/eeb-177/lab-work/exercise-9/pyrate_mcmc_logs/canid_occ_1_marginal_rates.log

# 95% HPDs calculated using code from Biopy (https://www.cs.auckland.ac.nz/~yhel002/biopy/)

pdf(file='/home/eeb177-student/Desktop/eeb-177/lab-work/exercise-9/pyrate_mcmc_logs/canid_occ_1_marginal_rates_RTT.pdf',width=0.6*9, height=16.8)
par(mfrow=c(4,1))
library(scales)
L_hpd_m95=c(0.129987812188, 0.129987812188,0.129987812188,0.129987812188,0.132453026137,0.0469418731676,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0326035016041,0.0420078071325,0.0365212546188,0.0506448800792,0.0638207768359,0.0746773990751,0.0859276297425,0.101664364489,0.104810666235,0.106102808611,0.104810666235,0.104810666235,0.101664364489,0.106102808611,0.101664364489,0.0910030574073,0.104810666235,0.118753592579,0.113854672157,0.118753592579,0.135719564353,0.135719564353,0.135719564353,0.121210322799,0.11972751481,0.11972751481,0.118753592579,0.118753592579,0.118753592579,0.118753592579,0.104810666235,0.11972751481,0.11972751481,0.11972751481,0.118753592579,0.0928716556293,0.0928716556293,0.0928716556293,0.0928716556293,0.0928716556293,0.0928716556293)
L_hpd_M95=c(0.330982111406, 0.330982111406,0.330982111406,0.330982111406,0.336761768125,0.324471334515,0.225223765181,0.147690773089,0.14643577551,0.14643577551,0.14643577551,0.14643577551,0.144482659925,0.144482659925,0.144482659925,0.155449474331,0.158735432421,0.190594050811,0.200308705014,0.206567276675,0.208417438627,0.206567276675,0.208417438627,0.209345150133,0.209345150133,0.209345150133,0.209345150133,0.223396647033,0.223396647033,0.243360878885,0.30384631624,0.334164062015,0.335820126874,0.343763294324,0.375227384633,0.375227384633,0.375227384633,0.369456778833,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.400674709441,0.400674709441,0.400674709441,0.400674709441,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.375227384633,0.375227384633)
M_hpd_m95=c(0.87046300301, 0.87046300301,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0893907001167,0.0781115305218,0.0505647545634,0.0465593840345,0.0465593840345,0.0417464678795,0.0417464678795,0.0417464678795,0.0417464678795,0.0417464678795,0.0373441128581,0.0373441128581,0.0352969698834,0.0352969698834,0.0331494480278,0.0331494480278,0.0331494480278,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972,0.0314330607972)
M_hpd_M95=c(1.45900062212, 1.45900062212,0.200143041943,0.200143041943,0.200143041943,0.200143041943,0.174379639925,0.160906371384,0.141575975606,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.136878532375,0.143225963704,0.13576589728,0.132604728149,0.130374690086,0.122797471904,0.1154157512,0.1154157512,0.1154157512,0.1154157512,0.110562967387,0.110562967387,0.107357530436,0.107357530436,0.108058628868,0.108058628868,0.108058628868,0.107357530436,0.108058628868,0.119244961807,0.119643769488,0.124029687326,0.157746526886,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599,0.162431305599)
R_hpd_m95=c(-1.21151503862, -1.21151503862,0.0124363353426,0.0124363353426,0.0124363353426,-0.0703953325389,-0.126489055978,-0.114295484229,-0.0885354564338,-0.084715153398,-0.084715153398,-0.084715153398,-0.084548766096,-0.084548766096,-0.084548766096,-0.084715153398,-0.084715153398,-0.0707850398027,-0.0513044383808,-0.0346239034964,-0.0346239034964,-0.00843971436512,-0.0130123539828,-0.00792665161224,-0.00634421327418,0.00587883010111,0.0143679295989,0.0110311969573,0.0143679295989,0.0076041275498,0.0283551278736,0.0345080310383,0.0318746023679,0.048700697385,0.0538642923094,0.048700697385,0.048700697385,0.048700697385,0.0444638864494,0.0444638864494,0.0363129440346,0.0291300520388,0.0363129440346,0.0181743793014,0.0181743793014,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518,-0.00390829588518)
R_hpd_M95=c(-0.608708384872, -0.608708384872,0.225559412163,0.225559412163,0.231097427809,0.222464882493,0.135371824135,0.0466398235286,0.0466398235286,0.0386030863182,0.0386030863182,0.0386030863182,0.0386030863182,0.0386030863182,0.0386030863182,0.0407420773335,0.0478449459024,0.0781250713978,0.0988808281849,0.107460403377,0.0988808281849,0.108618700179,0.0989144665501,0.113844511877,0.119953655262,0.141311484078,0.141311484078,0.141311484078,0.154113048332,0.173620915089,0.232361808406,0.258956549511,0.264664417246,0.282048750042,0.301920909168,0.301920909168,0.301920909168,0.301920909168,0.322583564019,0.322583564019,0.322583564019,0.342077936606,0.355406111598,0.355406111598,0.355406111598,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291,0.349713563291)
L_mean=c(0.255502519696, 0.255502519696,0.255502519696,0.255502519696,0.254549729672,0.218742798796,0.0869445469486,0.0777088950713,0.077613104717,0.0776039123871,0.0776039123871,0.0776039123871,0.0768007258336,0.0768007258336,0.0768007258336,0.0777088936005,0.0864449705576,0.121002760258,0.145886714267,0.152063769291,0.155270072391,0.159215789075,0.160261862258,0.161077230788,0.161252363064,0.161216039254,0.161155990054,0.162431519773,0.163139923449,0.169292088702,0.188184628044,0.208718762356,0.215554984533,0.228725701961,0.235873207623,0.237028860475,0.23749190205,0.239117762151,0.243552233535,0.243902885806,0.243695045238,0.242589756143,0.242224187585,0.24261707263,0.244133502044,0.245244434202,0.244515615082,0.243985881347,0.243379929006,0.243256816359,0.243156528108,0.243156528108,0.243156528108,0.243156528108,0.243156528108)
M_mean=c(1.12945431499, 1.12945431499,0.125750473142,0.125750473142,0.125589717139,0.124919105179,0.12119325912,0.11789648589,0.115188565798,0.113942408818,0.113942408818,0.113942408818,0.113942408818,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113945814708,0.113712274677,0.110820735984,0.102307513817,0.0940313922159,0.0892460937639,0.08722989522,0.0805601500532,0.0785037347291,0.076596827521,0.0757125234419,0.0737786724873,0.0734726434133,0.0726094366853,0.0713983517137,0.0712427011488,0.0712427011488,0.0712427011488,0.0715754421182,0.0721147010754,0.0744051396171,0.0750928290548,0.0761660891638,0.0772667069245,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163,0.0776752263163)
R_mean=c(-0.873951795291, -0.873951795291,0.129752046554,0.129752046554,0.128960012534,0.0938236936168,-0.0342487121719,-0.0401875908184,-0.0375754610812,-0.0363384964313,-0.0363384964313,-0.0363384964313,-0.0371416829848,-0.0371450888746,-0.0371450888746,-0.0362369211078,-0.0275008441507,0.00705694554962,0.0319408995591,0.0381179545829,0.0413242576829,0.0452699743671,0.0465495875814,0.0502564948045,0.0589448492476,0.0671846470379,0.0719098962898,0.0752016245529,0.0825797733961,0.0907883539733,0.111587800523,0.133006238914,0.141776312045,0.155253058548,0.163263770938,0.165630508761,0.166249200902,0.167875061002,0.172309532386,0.172327443687,0.171580344162,0.168184616525,0.16713135853,0.166450983467,0.16686679512,0.167569207886,0.166840388766,0.166310655031,0.16570470269,0.165581590042,0.165481301792,0.165481301792,0.165481301792,0.165481301792,0.165481301792)
trans=0.5
age=(0:(55-1))* -1
plot(age,age,type = 'n', ylim = c(0, 0.440742180386), xlim = c(-57.75,2.75), ylab = 'Speciation rate', xlab = 'Ma',main='canid' )
polygon(c(age, rev(age)), c(L_hpd_M95, rev(L_hpd_m95)), col = alpha("#4c4cec",trans), border = NA)
lines(rev(age), rev(L_mean), col = "#4c4cec", lwd=3)
plot(age,age,type = 'n', ylim = c(0, 1.60490068433), xlim = c(-57.75,2.75), ylab = 'Extinction rate', xlab = 'Ma' )
polygon(c(age, rev(age)), c(M_hpd_M95, rev(M_hpd_m95)), col = alpha("#e34a33",trans), border = NA)
lines(rev(age), rev(M_mean), col = "#e34a33", lwd=3)
plot(age,age,type = 'n', ylim = c(-1.33266654248, 0.390946722758), xlim = c(-57.75,2.75), ylab = 'Net diversification rate', xlab = 'Ma' )
abline(h=0,lty=2,col="darkred")
polygon(c(age, rev(age)), c(R_hpd_M95, rev(R_hpd_m95)), col = alpha("#504A4B",trans), border = NA)
lines(rev(age), rev(R_mean), col = "#504A4B", lwd=3)
plot(age,age,type = 'n', ylim = c(0, max(1/M_mean)), xlim = c(-57.75,2.75), ylab = 'Longevity (Myr)', xlab = 'Ma' )
lines(rev(age), rev(1/M_mean), col = "#504A4B", lwd=3)
n <- dev.off()