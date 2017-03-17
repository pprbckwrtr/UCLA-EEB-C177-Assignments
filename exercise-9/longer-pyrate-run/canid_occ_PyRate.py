#!/usr/bin/env python
from numpy import * 


data_1=[array([14.567503,14.39824,15.280193,6.469604,15.195549,9.898476,15.253307,15.883754,15.765829,15.952136,14.548176,11.071276,11.094711]),
array([18.481165,19.332424,14.776782,14.707638,15.433265,13.74338,15.95757,15.251709,13.730881,15.536175,14.125198]),
array([13.989419,21.264114,15.421413,15.292984,12.202915,11.52699,14.051556,15.125243,15.570489,15.438573,4.966976,13.420324,15.07657,14.240767,15.013664,12.77472,15.851194,14.286347,15.655989,15.344354,10.721852,10.828792,13.897918,11.111042,14.743532,13.927799,12.408251,13.526454,18.28418,13.838178,15.583492,14.441662,14.511178,15.210536,13.602981,15.44574,11.159586,14.547351,13.899469,15.013641,15.836635,9.601095,13.69882,11.069152,5.934519,7.706722,15.531222,14.529789,11.58995,21.10308,13.706545]),
array([14.538744,15.332107,13.9332,17.0973,15.57024,15.846133,15.607663,14.418997,15.94665]),
array([15.877734]),
array([12.417191,15.644926,11.987505,10.560904,11.402209,13.569878,11.561725,14.758197,14.21641]),
array([12.850245,13.27909,12.940095,10.827635,11.821111,10.356317,9.158636,20.902362,10.66219,10.352809,12.619684,12.930071,10.66384,21.540454,10.460914,12.81694,11.095333,9.897942,9.096186,12.09147,22.907058,10.654304,12.351445,11.305441,10.385781,11.616366,11.655695,13.021842,11.769438,13.159939,11.933306,8.328182,10.804712,16.895136,12.171962,13.228485,12.184511,13.123644,6.429895,10.770797,13.087651,11.123168,5.463001,12.142973,6.078555,11.472131,11.961466,12.144917,11.237664,11.421065,12.067086,10.890038,11.174866,7.514525,10.542132,13.859979,12.346778,12.301954,13.475961,13.18677,12.894739,12.737691]),
array([16.281607]),
array([4.760507]),
array([1.517845,0.903468,0.02986,0.120157,0.102038,0.044175,0.004816,0.124278,0.002908,0.011461,0.010427]),
array([29.18435]),
array([31.249017,31.2974,30.750477,21.821616,30.017972,30.730623,21.377412,29.988237,30.570248,29.250685,26.259644,21.964065,27.018477,27.836375,28.481442,29.716956,27.321757,28.263729,27.712273,30.154027,26.356432,26.68631,29.743257,29.37989,28.035154,24.108759,26.996117]),
array([33.043869,31.103275,33.202599,31.058989,30.879015,32.388297,32.936255,29.437975,27.170375]),
array([23.312543,22.617023,23.173067,19.132539,16.295422,15.389838,15.827619,11.490905,10.616058,12.73205,13.997227,12.089189,15.422189,12.538156,14.699275,12.762414,11.393425,12.800719,8.623347,10.48724,17.186719,14.677413,15.794163,13.293467,19.065378,14.781713,14.672173,13.284225,11.638523,11.37116,7.977694,12.700598,11.844854,17.522555,16.749275,20.10937,6.475703,16.370465,20.205202,18.600064,20.148749,20.40561,19.633139,17.149213,5.568049,15.952308,15.045876,12.281342,11.670107,11.402032,12.802445,11.289643,13.503571,12.867663,15.192231,13.770569,15.082449,18.287417]),
array([9.226208,9.944552,9.390523,7.624615,9.718871,10.293305,8.764767,8.750627,8.024506,9.90181,7.295298,5.573548,7.09983,8.544389,15.342735,6.402226,8.011278,9.00813,7.337214,5.381386,8.092272,10.012454,3.01151,2.119574,3.479582,3.016498,3.282587,3.634214,3.498266,2.103175,3.4408,3.653798,5.329036]),
array([2.630205,3.422152,2.447514,1.834418,2.240551,2.618058,3.899509,4.155805,3.740021,2.893123,3.608062,2.733273,4.818268,4.324662,2.391328,3.588618,2.133128,2.705738,3.785508,4.153238,4.030305,2.776062,4.789417,4.694607,3.264473,4.38011,3.501713,1.80912]),
array([4.793086]),
array([7.830775,9.223682,9.539427,9.475742,16.695952,5.526308,10.514307,3.878601,5.736373,1.83564,4.025774,3.962441,4.84587,3.789581,2.169407,1.994491]),
array([12.007135,22.480444,12.963051,11.910493,10.857338,12.968813,21.823999,11.846522]),
array([9.791568,8.874343,4.072945]),
array([9.284327,7.304526,7.266806]),
array([10.120331,7.758717,15.314471,6.040506,7.964757,8.614309,9.167756,11.469195,16.037425,8.359568,14.198387,6.75367,12.278931,8.098609,5.605888,6.187006,12.995295,11.229245]),
array([8.627449,18.779339,5.3791,10.277976,7.067018,7.583344,9.312607,6.970145,9.58288,10.085712,9.785891,8.507114,17.077036,7.524691,6.533623,6.60979,10.189777,5.589865,14.481448,18.047209,12.18108,6.70581,5.370569,6.460815,6.258602,5.744532,9.455164,9.489638,5.027731]),
array([22.292057]),
array([36.196881,34.800657,35.114204,33.551847,32.456099,20.869022,26.247466,30.557762,28.119124,29.561296,29.948991,26.147302,25.955235,22.066853,22.583576,29.305103,20.598265,18.697101,17.773252,17.580473,11.631364,11.766924,9.708909,10.020353,8.214047,13.364406,13.160596,6.932417,18.106465,11.690794,14.652165,14.220836,8.420756,15.026551,19.572987,6.22035,14.32607,13.869882,15.533817,19.556598,14.354396,22.379829,13.960605,16.169067,13.867031,10.023944,6.768639,3.698212,4.458925,4.230278,3.768219,3.462692,4.866324,3.369541,4.760007,3.240129,2.251298,0.652849,1.172655,0.51625,1.559003,0.437547,0.406419,0.95737,3.778073,9.453606,6.821757,13.14754,2.839405,1.164399,0.260345,3.459867,2.824573,1.593117,0.822141,1.739503,1.858745,2.475652,0.77481,3.255162,1.047425,0.356919,15.054992,3.201,16.702088,2.837397,17.494495,6.041767,0.735859,2.518603,4.557421,2.799782,23.234459,2.80595,4.47259,8.488992,3.882652,0.276437,17.237959,0.492381,7.254686,0.767287,2.68525,4.346268,0.073943,0.114534,0.036272,1.679834,0.028586,0.116134,0.047958,0.021035,0.051977,6.481569,0.734118,3.334772,0.051683,0.016037,0.066861,26.956949,23.530701,21.586797,28.32545,10.345723,0.939528]),
array([25.759759,6.248536,17.648823,10.745879,11.02338,13.129474,11.13602,5.413438,13.718546,9.247969,11.382919,12.96637,12.302228,6.602335,10.428969,5.600596,7.720555,10.541692,12.007623,13.111134,10.566877,12.686898,11.228952,11.388599,11.637048,3.552187,0.110694,0.02363,0.784989]),
array([4.999582,5.379897,8.632921,2.948313,2.437474,2.872744,4.100203,4.846279,2.952914,3.357397]),
array([5.844177,8.415511,9.858892,2.242595,3.890369,2.38214,4.176864,2.502088,4.198915,3.576014,0.59065,0.953333,1.744875,0.776644,1.229585,0.567466,0.756799,1.262556,0.280058,0.454299,1.514545,0.932425,0.519488,0.063659,2.681116,2.812837,2.980087,3.449375,1.910065,3.00137,2.763074,3.211387,4.141376,2.646248,2.946222,2.418397,0.008953,1.34467,2.228887,12.936592,4.58876,1.66542,0.004363,0.010684,0.007012,0.720497,0.005712,0.006684,0.00508,0.232946,0.323243,4.10384,1.02645,1.861871,0.005854,0.00891,0.004105,0.005696,2.309727,0.007883,2.42776,2.264923,0.001223,2.636261,2.080347,3.625445,0.069928,3.09225,4.010224,2.571722,1.278513,1.213082,1.593678,2.175227,1.783394,0.208252,0.401742,0.555227,4.035604,0.061071,0.559343,3.397473,4.884555,1.710005,1.717924,0.801819,0.731148,2.32706,1.973661,2.460145,2.516491,1.016618,1.66197,1.365553,1.770854,1.491965,1.165567,0.972629,1.091815,2.314617,1.987312,0.547806,3.197701,0.422503,0.191297,3.113665,1.036312,2.865365,2.701549,2.834444,3.021871,1.481929,1.31522,2.465806,2.448508,0.668575,0.218468,4.61728,4.094789,2.453676,1.351816,1.191173,0.90484,0.718291,0.845189,0.086803,0.332643,2.420981,0.26426,3.154061,4.378385,0.845664,1.905455,4.681973,3.730964,3.363221,3.284274,1.159165,0.793053,2.130815,0.316805,3.933124,0.411099,7.750723,4.258751,2.255202,1.981313,0.865331,1.776706,1.14745,1.490394,0.156373,0.966263,0.35228,0.14357,0.528306,0.270104,0.749583,0.161876,0.334763,0.594835,0.343913,1.504677,1.4812,2.009702,2.565013,3.145991,2.873871,2.471636,2.118959,2.505416,1.166268,1.643009,0.182233,0.243079,0.661624,0.678008,0.675765,0.685957,0.516802,0.133734,0.532,5.037036,3.76605,1.88821,1.069351,2.235927,1.621612,1.86765,0.268102,1.802744,0.793711,4.612826,4.713709,4.653288,3.639167,4.04291,3.540624,2.694643,4.616515,4.490547,2.073612,2.445417,1.098525,4.537128,0.046268,0.077773,0.041155,1.502632,0.482945,0.086081,0.030955,0.008125,0.057675,1.589675,2.830482,2.669768,0.893998,2.300571,1.501706,0.121935,0.034788,0.017304,0.116172,0.120334,0.066686,0.62254,2.075613,10.664403,3.556997,0.067254,0.125967,1.105828,0.121787,5.918709,0.057023,0.010992,0.698349,0.692281,0.005779,0.009737,0.007765,0.005486,9.794386]),
array([0.19257,0.528162,0.529925,0.101111,0.033689,0.098751,0.588226]),
array([0.004157,0.005282,0.058093,0.383526,2.944949,0.709502,2.118575,0.168316,0]),
array([0.614617,0.094437,0]),
array([2.061694]),
array([2.07867,1.656228,0.349286,1.674838,0.8122,1.174942,1.031176,1.657875,0.720123,1.126841,1.065804,1.729476,0.62701,0.072996,1.02838,1.657928,0.060433,1.462224]),
array([0.006905,0.747186,0.329339,1.203265,2.492715,0.003437,2.365043,1.482282,2.561932,3.386004,0.091656,0.176166,0.472965,0.00344,0]),
array([0.366475]),
array([0.487185,1.145361,1.575009,0.883618,1.220266,1.110317,0.955347,0.441552,1.170595,0.09412,1.537377,0.166397,0.524749,1.640785,0.533032,0.06399,0.04846,0.072087,0.027928,0.029845,0.052712,0.088032,0.15483,0.096385,0.050958,0.091269,0.039985,0.06368,0.095715,1.051681,0.257706,1.670043,0.068865,0.062744,0.064651,0.120714,0.068991,0.962593,0.114707,0.01629,0.036059,0.123741,0.866489,0.113457,0.266675,0.081206,0.028797,0.054348,0.110637,0.073245,2.305325,0.0672,0.096141,0.036097,0.091838,0.026181,0.07804,0.072856,0.071876,0.230275,0.052833,0.034367,0.080969,0.019191,0.050582,0.07905,0.018579,0.120306,0.013371,0.512356,0.564301]),
array([3.269625,4.88213,1.479932,0.405034,1.609615,0.992983,3.776271,1.042254,1.086004,0.440219,1.587321,1.212556,3.159578,1.414278,1.781874,1.546372,1.183656,0.50013,3.572948,3.761248,3.055236,3.007047,1.34236,0.356422,1.017379,1.283858,1.198158,1.713865,1.196227,21.867442,4.136487]),
array([0.005608,2.014176,0.003354,0.011564,0.003135,0.011498,0.005047,0.00212,0.009982,0.028084,0.008766,0.007538,0.011414,0.001475,0.001771,0.005526,0]),
array([8.952918,9.179563,7.36518,8.871743,2.417828,4.034023,2.986825,3.965131,3.912504,3.904166,2.733014,3.024589,9.180168,8.671387,9.050966,9.348919,3.619476]),
array([2.886412,3.746619,3.395665,2.193873,2.530922,3.268904,2.336626,4.266861,2.953333,2.086942,1.707838,1.409693,0.820395,1.713598,0.487444,1.586479,1.661876,0.908449,1.26176,1.18217,0.327108,0.665623,1.070635,1.072577,0.701052,0.658397,1.3413,1.734057,0.921534,0.868586,0.046888,1.724541,1.512905,1.406426,1.772401,0.804585,1.348567,0.406173,0.118923,0.472256,0.982943,0.648205,0.987484,1.407449,1.741498,0.054281,0.031324,0.072833,0.099296,0.12002,0.113333,0.106916,0.116448,0.042102,0.064147,0.094626,0.014357,0.034346,0.098981,0.056835,0.006827,0.071405,0.027791,0.067728,0.003825,1.780971,0.089039,0.092208,0.022043,0.055796,0.091073,0.108328,0.056594,0.112582,0.02739,0.0638,0.067657,0.047683,0.041574,0.052153,0.086281,0.113483,0.082666,0.223817,0.11861,0.124444,0.076084,0.080681,0.094127,0.438198,1.163499,1.592349,1.214543,0.313627,0.007258,0]),
array([8.301641,4.035254,3.604771,3.921725,3.840435,4.084787,2.089133,3.195016,2.709015,4.113396,3.914313,4.666528,4.002594,2.730302,2.12977,4.218088,2.613582,3.033481,2.402768,2.029852,1.908368,1.996699,3.480151,4.630862,3.034088,4.573542,4.706891,2.690186,4.098906,2.026408,4.10908,2.684211,2.742533,3.507393,2.074006,0.039236]),
array([0.957101,1.413369,0.899983,1.065974,0.036072,0.053321,0.111922,0.109196,0.08968,0.016384,1.111342,0.521192,0.230531,0.652546,3.196556,2.375505,0.705352,0.223122,0.652008,1.490132,0.36351,0.247286,0.215208,0.827865,1.856928,1.307334,0.201194,0.421608,0.394341,0.293543,0.099271,0.024584,0.032389,0.047999,0.045235,1.052574,0.591124,0.271996,0.422915,0.644057,0.394623,2.165746,0.287277,0.0681,0.300664,0.144894,0.451726,1.804718,0.090313,0.331473,0.495163,0.309565,0.188403,0.149342,0.353381,0.309048,0.459672,0.247275,0.163637,0.677269,2.4312,0.563405,0.0033,0.011455,2.017056,0.310554,2.798355,0.072423,0.107381,0.10801,0.02641,0.053678,0.09656,0.052198,0.044392,0.044212,0.056724,0.018334,0.07879,0.114689,1.514841,0.110755,0.081307,0.01772,0.080792,0.113737,0.096794,0.118308,0.11159,0.057753,0.254998,0.06438,0.03175,0.062387,0.006924,0.007237,0.011284,2.418961,0.037394,0]),
array([1.705442,3.649953,4.516635,0.001661,0.007521,2.975882,2.150866,1.443631,3.305747,2.439019,2.558335,0.001532,0.839467,2.411559,0.006136,1.062072,1.192579,0.953613,2.505273,0.292136,0.185516,0.136006,1.492311,2.50738,3.820104,2.495852,1.655959,1.102657,0.276812,1.054026,2.9965,2.037872,2.438389,2.414046,2.337905,0.50088,1.574858,1.910529,1.987202,3.429381,0.988505,2.549987,0.003065,0.034598,0.053739,1.031729,0.979675,0.083609,0.016348,0.349027,1.950408,1.826091,0]),
array([1.829808]),
array([4.312165,3.059851,4.685618,1.718954,1.657016,0.392994,0.078429,0]),
array([4.664265]),
array([15.396812,21.143053,14.072231]),
array([12.397916,13.515038,14.673063,15.762739,13.724639,15.15478,14.814752,15.475021,15.285792,15.803143,11.989163,14.988136,14.645669,15.345058,9.583093,15.291686,15.869358]),
array([7.923339,5.527282,10.21867]),
array([12.110898,12.112257,13.567696,10.359579,12.921982,13.012054,11.711887,10.453496,12.189207,9.993657,16.907521,12.378001]),
array([12.578074,12.418945,13.112651,11.445725,12.497175,11.318213,11.790939,13.256799,9.297554,14.603038,15.54355]),
array([4.258651,2.981915]),
array([7.501112,3.29904]),
array([0.004185,0.119357,0.053566]),
array([40.835091]),
array([1.359463]),
array([1.382673,0.288451]),
array([2.264355,2.355282]),
array([29.487688]),
array([28.019743,20.678319,20.723836,28.743124,22.387932,22.405313,22.675596,24.34409,25.536192,25.721407]),
array([30.721454,25.850211,24.741876,23.678444,22.489161]),
array([2.088199]),
array([0.73887,0.687405,0.188743,0.549715,0.774243,0.57405,0.466247,0.458298,0.59577,0.520391,0.645003,0.113924,0.207896]),
array([1.215207,0.204036,0.103718]),
array([21.537312,22.863796,21.510665,21.373785,22.686277,20.631087,19.615231,19.980279,17.870633,17.137273,19.538059,19.503946,18.937637,16.883513,20.381777,17.629127,18.222265,18.165475,16.125167,19.934106,19.060626,16.608465,19.829503,16.598219,18.939398,17.291959,19.157419,19.500301,15.374174,18.766954,16.420246,17.132851,19.149433,18.154499,17.534405,16.267742,19.847374,16.528091,18.427278,18.26983,16.217694,19.816591,13.733843,14.64412,15.407498,15.252128,22.323066]),
array([16.244622,18.664771]),
array([11.438483,19.920405]),
array([22.657191]),
array([30.45285,20.797286,24.044477,28.412345,26.491925,24.782548]),
array([21.408864,20.737023,23.52207,30.766546]),
array([25.630671,26.918017,27.543208,29.477816,27.253176,27.316549,29.936798,27.124921,28.637307]),
array([16.270552,17.114905]),
array([10.409382,14.187026,11.406399]),
array([11.739117,10.669095,15.391904,11.695356,12.450947,13.298704,12.426252,11.064987,11.763916,12.664198,9.389587,11.874923,11.848957,10.643527,10.320965,10.907718]),
array([15.056379,14.584736,14.897569]),
array([14.250561,18.723227]),
array([15.380865,13.61666,13.641341,15.381905,14.978819,15.663268,15.277509]),
array([10.667132,13.339258,12.151454]),
array([15.55776]),
array([24.176496]),
array([31.619662,31.819699,33.295548,30.824092,31.303483,32.4867,30.996563,32.676497,27.946843,29.539087,22.44154,25.551082,30.169819,26.756127]),
array([30.376087,31.583705,29.314092,47.204814,35.119704,36.94596,34.217995,49.17264,33.88346]),
array([33.919729,36.358833,37.026985,36.018477,34.152721]),
array([0.141028,0.031821,0.650133,0.667974,0.082096,2.172663]),
array([0.103933,0.480505,0.803573,0.477772]),
array([24.649476]),
array([18.659836,18.358147,16.717226,17.409099,17.015319,18.580652,16.139544,19.257759]),
array([21.854989,22.694168,22.682815,24.393642,24.289201,24.073671,22.920107,22.035079,22.4076,21.829306,24.641545,20.48884,24.336185,21.037942,21.115682,24.491653,23.43955,23.751956,22.914513,24.333381,22.641026,16.390721,16.464916,17.79019,19.754025,20.002509,18.668885,16.78747,16.504461,17.884893,29.423772,19.117549,16.413031]),
array([0.005471,0.008912,0.098147,1.741737,0.006708,0.004721,2.107395,0.054627]),
array([0.054908,0.553376,0.372647,0.022678,0.027232,0.031234,0.457444]),
array([0.600787]),
array([0.258192]),
array([31.952238,21.345702]),
array([24.45796]),
array([20.305699,16.304842,19.208013]),
array([31.895263,23.882048,20.662053,22.774609,22.863765,25.438552]),
array([22.412738]),
array([24.666588,24.757305,25.313827,30.59629,23.270762,22.002316,22.348609,22.228764]),
array([28.542214,21.558047,25.018803,26.172598,25.204866,26.709437,28.480173,23.918351,23.166644,26.053152]),
array([30.243318,27.365789]),
array([6.308216,9.996937,10.620326,5.24924,7.96752]),
array([9.311131]),
array([16.697139,9.207468,7.752484,7.263168,6.646118,5.083311,6.705537,13.452151,13.53101,10.59002,22.720155,9.120575,7.577391,11.430784,11.997391,11.150864,6.037073,11.133515,6.457349,10.666221,13.302422,12.756933,9.674806,7.125507,8.488939,12.869814,12.541116,22.060331,9.864318,7.995949,11.751577,20.371109,10.449133,12.714694,11.461691,8.557402,11.494418,8.455815,14.426973,10.254654,9.283576,4.9215,11.114847,8.700133,9.658581,9.921146,10.933714,7.499707,16.784053,6.812319,11.624691,13.400858,10.072095,9.115172,11.144551,12.027446,5.703849,12.678377,7.232721,6.594477,14.456348,18.437496,13.131003,11.194224,14.156474,8.256786,13.451006]),
array([11.162778,10.260565,9.673496,11.189443,13.288975,12.733904,12.729804,13.268188,9.986671,11.019545,10.494621,11.156171,11.74218,10.526461,11.019762,12.25001,12.757083,11.914796,10.420207,11.394488,11.725661,11.559108,12.208313,12.200648,12.928976,13.120364,13.113596,7.457033,4.987064,21.68795,7.587839,10.692962,11.06897,16.48933,11.169969,9.406584,13.212403,11.572747,12.88023,7.880958,13.433864,12.135579,12.82338,13.291061,15.975933,7.008304,14.056972,12.091435,11.447372,10.581399,13.195613,10.590849,10.965796,7.657928,12.148083,14.527741,14.63953,15.064581,15.942284,14.806459,14.916771,10.527701,19.144394,10.996631,5.642431,18.000918,12.202581,12.488213,5.095821,11.830293,12.246712,11.861239,11.67165,14.548306,7.098021,5.72529]),
array([6.129465,4.109489,5.526062]),
array([5.929185,9.936147,7.452667,7.756557,8.457621,9.991422,8.905718,7.040816,10.095959,13.942234,6.302457,7.811451,7.832783,4.927959,5.190164,8.181021,6.132389,4.175123,5.238024,6.670231,7.806324,9.842608,5.079713,7.67681,7.591029,10.182151,5.888073,9.504952]),
array([11.424243]),
array([14.656724,18.661797,18.337535,14.319452,15.608451,14.401954]),
array([17.177038]),
array([10.032386,13.667055]),
array([41.616835,35.864092,35.922144,36.538218,36.424837,34.306381,34.996455,34.63722,35.790043,34.231105,36.747995,34.37137,35.520528,34.305492,33.97168,36.45665,34.078365,33.604589,33.349102,33.643445,33.75216,33.47076,33.77302,33.883277,33.723296,33.491118,33.4165,28.632881,32.853766,32.976719,32.863019,32.902537,31.492324,21.360909]),
array([33.667741,33.352067]),
array([39.67822,37.14027,33.986279,35.142513,35.602502,36.409404,35.509858,33.972567,34.813419,35.869858,34.533205,34.624789,37.123824,34.667546,36.55804,34.732957,35.933541,36.817162,35.417646,34.69407,35.326597,36.398588,37.168084,35.238925,34.828939,35.305367,35.127159,36.816639,34.653737,34.372621,36.025566,34.404494,35.71539,36.023572,35.508353,36.12989,35.041298,35.572242,33.315805,33.865013,33.846864,33.609818,33.470695,33.82407,33.389882,33.600843,33.422889,33.651757,33.476961,33.46165,33.584255,33.497735,33.343511,33.768567,33.560541,33.714496,33.377777,33.72987,33.548878,33.884604,33.453412,33.594701,33.774524,33.547235,33.361836,33.484055,33.743067,33.403719,33.426191,33.333115,33.878904,33.740443,33.48923,33.638911,33.366417,33.547578,33.893401,33.842267,33.885,33.639693,33.650896,33.899502,33.562924,33.434992,33.694866,33.412318,33.450995,33.80672,33.572368,33.563325,33.430119,33.385165,33.681088,33.733755,33.698023,33.496466,33.548353,33.521039,33.720439,33.508826,33.881561,33.619889,33.631229,33.460364,33.485877,33.614049,33.442948,33.396634,33.890522,33.888792,33.622548,33.416143,33.805147,33.817722,33.707135,33.761191,33.759668,33.445416,33.321597,33.890548,33.361753,33.707992,33.866857,31.813231,31.293547,32.163646,32.377636,30.848068,32.01354,31.680407,35.690533,36.863025,33.657018]),
array([29.443177,22.794091]),
array([21.861775,23.412398,13.700657,11.163325,15.55722,12.343115,11.059759,20.496833,13.649719,11.798373,7.335245,25.742858,15.776823]),
array([22.957095]),
array([30.042069,28.866915,21.058552,28.798577,22.033004]),
array([20.544779,21.253494,23.687632,23.300973,20.763911,21.419448]),
array([13.635588,18.159659,18.177841,19.844642,20.307167,20.962515,17.823084,17.96051,19.54938,16.727209,20.313789,16.996173,17.565595,18.756218,13.856361,13.946244,15.066875,14.317654,14.116511,15.893731,15.15643,13.706958,14.89977,14.171508]),
array([12.716693,11.858462,12.230998,11.662334,13.135659,10.826773,12.386002,13.100049,11.29503,11.167312,11.387979,12.815652,13.288652,13.207737,11.653536,11.60024,11.624883,10.817948]),
array([22.721977]),
array([10.469729]),
array([14.998844,15.608568,7.247011,10.856281,13.696711,14.597611,12.701807,15.394788,14.082806,13.994936,14.826609,15.115632,13.619623,15.340983,14.935919,14.465541,13.886208,12.34158,14.34439,13.793835,14.40063,10.692485,15.600922,12.161535,12.593794,11.859377,11.315168,10.87893,12.658376,13.75828,14.922654,14.908097,15.219459,14.94493,14.172983,11.088453,12.354331,10.971072,10.820841,13.30064,15.272765,11.004695,15.431176,22.748594,21.454303,21.055632,11.548171,7.853171,7.11103,13.935625,12.952078]),
array([22.256454,17.263366,29.344444,19.897161,19.060851,24.958243]),
array([0.929413,0.987669,1.737237,2.805103,1.588492,0.240561,3.137392]),
array([0.007548,2.079654,0.782667,0.751416,0.012328,0.977484,2.279221,0.559626,2.469207,0.106136]),
array([26.320721]),
array([27.166527,24.534386,22.607593,26.009788,26.361709]),
array([29.069403,25.446611]),
array([33.776728,32.721712,33.222509,32.853727,32.494464,33.115251,31.850796,32.376409,31.671182,30.80168,30.993302,31.169278,32.862087,32.571797,27.639733,29.26973,28.636073,28.206753,27.53743,24.784757,22.150354]),
array([6.6754]),
array([10.969696,15.146814,12.475383]),
array([7.253381,6.812851,17.8645,10.062413,11.842874,19.452783]),
array([12.534478]),
array([16.304413,16.914263,19.367563,16.808881,20.01919,18.04446,16.152502,18.680335,18.365436,19.664345,20.094484,17.754736,17.957771,19.450519,19.774585,17.792888,19.545926,18.877124,20.137635,18.909236,19.74466,13.579219,16.8852,19.985708,17.693551]),
array([19.312961,13.905011,19.7942,16.338429,20.285391,16.036391,16.917432,17.615976,14.23498,18.688184,16.606921,15.717328,14.174938,9.915735,14.721735,20.117022,14.875399,14.830509,15.09935,21.931784,14.184693,15.405221,14.952985,15.488298,14.912918,15.036468,17.921951,14.982309,15.305157,13.634961,14.910232,15.768642,15.337791,15.282911]),
array([43.940323]),
array([3.855648,3.645547,3.215837,3.403977,2.942697,2.626226,2.750959,1.908486,5.018568,3.848833,4.154411,2.962977,1.243066,3.619059,4.608915,4.151799,1.928093,3.612073,7.178119,3.404095,5.266648,3.715759,1.217921,2.621509,2.194275,2.18632,1.881846,2.325357,2.722399,1.93977,3.720439,2.431291,1.706012,4.584861,3.177962,4.777275,1.021472,1.752946]),
array([2.897863,3.426835]),
array([0.327333,0.066638,0.08735]),
array([23.43808,18.948449]),
array([13.932874,16.633603,16.084735,17.527015,17.468222,19.922269,17.60854,17.454517,19.289564,15.322944,14.011822,15.850218,14.896458,15.714698]),
array([16.407271,17.78899,16.12742,17.03656]),
array([33.450363,31.766141]),
array([20.129404,16.700241,19.863227]),
array([30.909333,31.635984,23.18039]),
array([29.431556]),
array([23.905477,29.067606,25.888072,27.350462,30.467747,29.276658]),
array([33.842498,33.8385]),
array([2.559466,0.691842,3.369655,0.961266,1.922189]),
array([0.004401,0.011447,0.147614,2.475581,0.167459,0.059959,0.040763]),
array([31.681243,31.607976]),
array([31.795427,31.362155,31.871557,32.326247]),
array([17.677122,20.284407,16.559858,18.279414,18.034993,15.752033,16.807858,18.061252,18.046026,20.303112,13.780109,15.337856,19.845911,18.738067,15.332568,19.446161,14.332802,14.510279]),
array([16.169272,20.077001,18.096748,14.555403,16.142482]),
array([21.967406,24.706819,25.278482,27.518311,27.972864,24.25365,29.043033,27.676926,24.592607,23.880539,21.186465,26.295362]),
array([22.069812,23.961727]),
array([20.505918,21.006452,21.544669,24.118986,20.744975,23.284822,30.3318,24.363504]),
array([11.665652,12.490766,13.180761,11.570541,11.088439,15.276381,11.942688,13.033604,11.36752,10.578675,13.286398,13.064309,12.175855,11.602909,13.094962,13.243224,11.348788,7.099028,10.954527,11.267647,13.74222,11.19414,12.406242,11.512549,10.484319,11.460003]),
array([14.892558,15.189785,15.314908,15.440717,15.362928,15.032548,14.868019,14.637555,14.225962,14.134793,15.733697,14.562657,15.715852,14.908227,15.243529,8.1475,13.660184,15.83207,22.603491,14.700198,14.672133,15.620516,15.284743,15.70441,14.26975,17.055038,14.741278,14.674564,15.752332,14.235513,15.273034,13.788212,12.684057,14.536658,15.054954,20.705694,16.755951,15.284153,14.595379,14.834463,14.653096,14.685386,14.205965,14.464879]),
array([28.935,30.54297,26.584398,28.822843,27.379579,30.133914,30.55557,24.47352]),
array([23.594554,23.601274,18.991517,17.048874,20.496978,17.579048,16.118027,16.42459,23.662909]),
array([21.717085]),
array([24.159574,21.8866,23.242884,22.914681,21.634872,24.484887,20.642435,24.167976]),
array([33.260959,22.97421,29.58777]),
array([22.387306,22.96492,18.01559,16.654964,16.193173,18.416095,19.13862,16.640041,17.282213]),
array([19.268726]),
array([16.349702,19.073346,18.814811,20.073073,17.171586]),
array([29.135195,26.047449,22.474768,20.731804,24.413112,22.897399,21.265917,23.040193,23.402458,24.615876,21.155776,16.623045]),
array([24.496475]),
array([22.989788,27.088362,30.282974,23.097173]),
array([16.233633]),
array([33.465115]),
array([15.677754,14.158908,14.25204,15.162544,15.650472]),
array([1.618605,1.676164,2.230913,1.380757,0.947266,0.121287,0.050466]),
array([0.554245]),
array([2.471628]),
array([0.471311,0.12594,0.050183,0.01639,0.87263,0.361973,0.031742,0.058334]),
array([16.014421,18.13782,16.286006,16.851377,19.652593,19.789028,16.624828,17.249573,15.997624,17.036828,17.383329,16.97971,18.255074,18.053944,19.056587,18.650621,17.731251,19.156136,18.996022,17.490334,14.718035,20.186466,18.821132,20.530943,15.371355,15.938341,10.127566]),
array([14.298152,19.442881,16.621769,13.733161]),
array([0.003039,2.276526,0.316142,0.394101,0]),
array([21.142411,30.150319,25.226005]),
array([0.12515]),
array([0.006077]),
array([26.91192,30.071918,27.642526,27.788352,27.37187]),
array([15.951906,13.955286,7.252816]),
array([0.07223,1.825923,0.278523]),
array([2.893127,2.445449]),
array([15.617134,14.662712,10.360248,15.838039,11.23466]),
array([19.545874,18.437303,20.409786,16.067884,15.945748,18.902688,16.87835,16.742689,16.807124,19.696854,18.602406,15.178616,21.433552,21.592213,20.482787,15.049581,14.855325,20.374329,17.903923,13.982358]),
array([16.121743,19.167473,16.282124,13.874167,18.882131,18.358687,19.73927,19.550239,18.452026,16.442896,19.205115,14.424759,19.300939,20.29371,18.960523,18.764833,15.123241,15.179164,15.347353,13.758569,15.356716,13.920207,14.59482,15.62348,14.130407,15.622479,15.845914,15.351029,14.29867,13.761687,14.336126,15.377004,13.87365,5.482278,15.199798]),
array([2.112911,1.586027,1.275676,0.594657,0.103376,0.043933,0.106247,0.083142,0.242599,13.513566]),
array([3.446273,0.764676,1.146792,1.267366,0.915868,1.377725,0.991754,0.090313,0.580952,0.028728,0.114307,0.036372,0.069399,0.12579,1.682413,0.114209,0.719634,0.102458,0.100333,0.06813,0.110865,1.493007,0.033391,0.070381,0.329094,0.093399,0.009888,0.099157,0.047387,0.03147,0.044196,0.092727,0.054086,0.064117]),
array([3.160036]),
array([2.922152,3.531504,1.926939,3.03666,2.238547]),
array([0.326815,0.982794]),
array([1.918591]),
array([7.279605]),
array([8.636733,5.211057,7.700362,7.239605,2.538322,1.654502,1.641161,1.29751,1.538998,0.342547,1.37312,1.381463,0.314144,0.301265,0.125809,0.328931,4.775664,4.46318,1.230664,1.200828,0.426367,3.297844,1.705136,4.213473,3.597016,3.678446,2.981277,1.629145,0.966165,1.748695,0.17336,1.375894,3.430938,1.665453,2.701525,2.947603,0.763108,1.406276,2.312112,2.028768,1.18414,2.037542,3.742471,2.330675,0.38124,1.039211,2.843432,1.909051,2.741726,3.029248,3.089282,3.163266,2.689703,0.622267,1.738903,1.888122,1.533241,2.460318,0.352775,0.567524,1.726184,1.828847,0.847195,2.102845,2.176102,3.426479,0.090284,2.011586,0.419643,1.417296,1.011776,1.94167,2.710358,8.25862,4.839782,2.4251,1.150074,0.547474,5.01337,0.017894,0.013801,0.097258,0.313923,0.207121,0.88907,0.459801,0.237229,2.06687,1.433652,3.117887,2.037531,0.835565,0.754669,0.68394,0.162487,2.405462,0.634732,3.432139,2.676584,0.485365,1.02666,0.076641,0.115574,0.045554,3.840533,2.300584,5.479488,0.124034,0.019436,0.024891,1.054476,4.814917,2.458692,1.073725,0.107074,0.003818]),
array([0.090025]),
array([0.005986,0.643169,0.008913,0.139342,0.008649,0.006518,0.011056,0.352949,0.002314,0.001548,0.007779,1.879773,0.060115,2.303089,1.766493,1.665091,0.118819,2.241073,1.957726,1.22903]),
array([12.719661]),
array([4.350489]),
array([6.914068,10.114302,7.158511,8.665214,6.04299,8.099285,8.387527,10.110107,5.714292,6.695368,7.27122,1.616529,8.452634,6.143334,4.975681,10.233803,7.60935,8.68885,7.454713,8.523334,15.374304]),
array([2.882364,0.765653,0.641919,0.855699,0.448053,0.517449,0.990838,1.545798,1.610681,0.026095,0.045772,0.109329,0.110469,0.023233,0.098166]),
array([0.887958,0.388368,1.13721,1.324692,0.123005,0.054714,0.116278,0.140818,0.292772,1.7863,0.105616,0.135925,0.587588,0.155145,0.106071,0.743979,1.910347,0.555755,0.747919,3.065874,0.930963,0.09257,0.462601,0.771222,0.024255,0.333627,2.348323,0.224788,0.114451,0.221515,0.618364,0.385584,0.489894,0.877291,1.352371,0.042965,0.105513,0.226996,0.625021,0.358858,1.386483,0.675352,0.012584,0.107189,2.058862,0.024726,0.077969,0.124422,0.04015,0.079327,0.125055,0.046952,0.103801,0.077342,0.09007,0.054339,0.062424,0.02886,0.040216,0.658696,0.086381,0.008227,0.009036,0.00889,0.074167,0.19013,0.0644]),
array([0.039139]),
array([0.040078]),
array([0.537576,1.831716,0.457032]),
array([1.485076,1.786297,0.589915,0.928754,0.707992,1.981465,0.771118,1.046937,0.281267]),
array([1.623748])
]

d=[data_1]
names=[ 'canid_occ_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aelurodon','Aelurodon_asthenostylus','Aelurodon_ferox','Aelurodon_mcgrewi','Aelurodon_montanensis','Aelurodon_stirtoni','Aelurodon_taxoides','Aelurodon_wheelerianus','Alopex','Alopex_lagopus','Archaeocyon_falkenbachi','Archaeocyon_leptodus','Archaeocyon_pavidus','Borophaginae','Borophagus','Borophagus_diversidens','Borophagus_dudleyi','Borophagus_hilli','Borophagus_littoralis','Borophagus_orc','Borophagus_parvus','Borophagus_pugnator','Borophagus_secundus','Caedocyon_tedfordi','Canidae','Caninae','Canini','Canis','Canis_(Pseudalopex)','Canis_adustus','Canis_anthus','Canis_apolloniensis','Canis_armbrusteri','Canis_aureus','Canis_cedazoensis','Canis_dirus','Canis_edwardii','Canis_familiaris','Canis_ferox','Canis_latrans','Canis_lepophagus','Canis_lupus','Canis_mesomelas','Canis_proplatensis','Canis_rufus','Canis_thooides','Carpocyon','Carpocyon_compressus','Carpocyon_limosus','Carpocyon_robustus','Carpocyon_webbi','Cerdocyon_avius','Cerdocyon_texanus','Cerdocyon_thous','Chailicyon_crassidens','Chrysocyon','Chrysocyon_brachyurus','Chrysocyon_nearcticus','Cormocyon','Cormocyon_copei','Cormocyon_haydeni','Cubacyon_transversidens','Cuon','Cuon_alpinus','Cynarctoides_acridens','Cynarctoides_emryi','Cynarctoides_gawnae','Cynarctoides_harlowi','Cynarctoides_lemur','Cynarctoides_luskensis','Cynarctoides_roii','Cynarctoides_whistleri','Cynarctus','Cynarctus_crucidens','Cynarctus_galushai','Cynarctus_marylandica','Cynarctus_saxatilis','Cynarctus_voorhiesi','Cynarctus_wangi','Cynodesmus_martini','Cynodesmus_thooides','Cynodictis','Cynodictis_lacustris','Cynotherium','Cynotherium_sardous','Desmocyon','Desmocyon_matthewi','Desmocyon_thomsoni','Dusicyon','Dusicyon_avus','Dusicyon_culpaeus','Dusicyon_sechurae','Ectopocynus_antiquus','Ectopocynus_intermedius','Ectopocynus_simplicidens','Enhydrocyon','Enhydrocyon_basilatus','Enhydrocyon_crassidens','Enhydrocyon_pahinsintewakpa','Enhydrocyon_stenocephalus','Epicyon','Epicyon_aelurodontoides','Epicyon_haydeni','Epicyon_saevus','Eucyon','Eucyon_davisi','Eucyon_skinneri','Euoplocyon_brachygnathus','Euoplocyon_spissidens','Gobicyon','Hesperocyon','Hesperocyon_coloradensis','Hesperocyon_gregarius','Hesperocyoninae','Leptocyon','Leptocyon_delicatus','Leptocyon_douglassi','Leptocyon_gregorii','Leptocyon_leidyi','Leptocyon_matthewi','Leptocyon_mollis','Leptocyon_tejonensis','Leptocyon_vafer','Leptocyon_vulpinus','Lycaon','Lycaon_pictus','Mesocyon','Mesocyon_brachyops','Mesocyon_coryphaeus','Mesocyon_temnodon','Metalopex_bakeri','Metalopex_macconnelli','Metalopex_merriami','Metatomarctus','Metatomarctus_canavus','Microtomarctus_conferta','Neovulpavus_washakius','Nyctereutes','Nyctereutes_abdeslami','Nyctereutes_procyonoides','Osbornodon_brachypus','Osbornodon_fricki','Osbornodon_iamonensis','Osbornodon_renjiei','Osbornodon_scitulus','Osbornodon_sesnoni','Osbornodon_wangi','Otarocyon_cooki','Otarocyon_macdonaldi','Otocyon','Otocyon_megalotis','Oxetocyon','Oxetocyon_cuspidatus','Paracynarctus_kelloggi','Paracynarctus_sinclairi','Paraenhydrocyon_josephi','Paraenhydrocyon_robustus','Paraenhydrocyon_wallovianus','Paratomarctus_euthos','Paratomarctus_temerarius','Philotrox_condoni','Phlaocyon','Phlaocyon_achoros','Phlaocyon_annectens','Phlaocyon_latidens','Phlaocyon_leucosteus','Phlaocyon_mariae','Phlaocyon_marslandensis','Phlaocyon_minor','Phlaocyon_multicuspus','Phlaocyon_taylori','Phlaocyon_yatkolai','Protemnocyon_inflatus','Protepicyon_raki','Protocyon','Protocyon_orcesi','Protocyon_tarijensis','Protocyon_troglodytes','Protomarctus_optatus','Psalidocyon_marianae','Pseudalopex_gymnocercus','Rhizocyon_oregonensis','Speothos','Speothos_venaticus','Sunkahetanka_geringensis','Tephrocyon_rurestris','Theriodictis','Theriodictis_floridanus','Tomarctus','Tomarctus_brevirostris','Tomarctus_hippophaga','Urocyon','Urocyon_cinereoargenteus','Urocyon_citrinus','Urocyon_galushai','Urocyon_minicephalus','Urocyon_progressus','Urocyon_webbi','Vulpes','Vulpes_cascadensis','Vulpes_chama','Vulpes_kernensis','Vulpes_mathisoni','Vulpes_stenognathus','Vulpes_velox','Vulpes_vulpes','Vulpes_vulpes_macroura','Vulpini','Xenocyon','Xenocyon_lycaonoides','Xenocyon_texanus']
def get_taxa_names(): return taxa_names