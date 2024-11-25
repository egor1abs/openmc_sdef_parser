import pytest
import numpy as np

import openmc_sdef_parser as parse

def test_make_openmc_source():
    source = parse.make_openmc_source('../notebooks/data/sdef_template.i')
    assert source.space.mesh.origin == np.array([0.0, 0.0, 0.0])
    assert source.space.mesh.r_grid == [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0, 48.0, 52.0, 56.0, 60.0, 64.0, 68.0, 72.0, 76.0, 80.0, 84.0, 88.0, 92.0]
    assert source.space.mesh.z_grid == [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0, 48.0, 52.0, 56.0, 60.0, 64.0, 68.0, 72.0, 76.0, 80.0, 84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 108.0, 112.0, 116.0, 120.0, 124.0, 128.0, 132.0, 136.0, 140.0]
    assert source.space.strengths == [
       1.38269106e-06, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.36061541e-08,
       1.07231247e-07, 2.65819195e-07, 2.39311230e-07, 1.00479962e-07,
       1.24849793e-08, 3.17848082e-10, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       1.17471358e-09, 1.36358918e-07, 1.58337879e-06, 3.32645049e-06,
       4.07403007e-06, 3.60745085e-06, 2.59426422e-06, 1.45453865e-06,
       4.25051083e-07, 4.14124861e-08, 1.53397919e-10, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.00298602e-07,
       3.08233737e-06, 5.54814663e-06, 5.61639231e-06, 5.62090581e-06,
       5.04339526e-06, 4.23956782e-06, 3.06734209e-06, 2.22481905e-06,
       1.10541212e-06, 2.28026101e-07, 2.71663238e-09, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 4.36564257e-08, 2.84178567e-06, 6.52047474e-06,
       7.34027227e-06, 8.41013935e-06, 9.39757829e-06, 9.15221976e-06,
       8.04341017e-06, 5.81567760e-06, 3.93989916e-06, 2.29664985e-06,
       1.31842358e-06, 4.21776080e-07, 1.65733301e-08, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.04983386e-09,
       1.22121348e-06, 6.26416332e-06, 8.58733121e-06, 1.12745419e-05,
       1.48304282e-05, 1.85432500e-05, 1.97673464e-05, 1.84956657e-05,
       1.38169256e-05, 9.27553605e-06, 5.03568182e-06, 2.55836956e-06,
       1.29211294e-06, 4.56704832e-07, 1.67753412e-08, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 7.62828681e-08, 4.28682918e-06,
       8.15624764e-06, 1.26820029e-05, 1.94540681e-05, 2.90686302e-05,
       4.03335525e-05, 4.69044362e-05, 4.69324851e-05, 3.67795821e-05,
       2.52770740e-05, 1.35256815e-05, 6.37902544e-06, 2.70478074e-06,
       1.13416222e-06, 3.68366675e-07, 5.24034973e-09, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.10290649e-06, 6.58711057e-06, 1.11522824e-05,
       2.04220803e-05, 3.59389060e-05, 5.99844961e-05, 9.11177605e-05,
       1.14531461e-04, 1.22161348e-04, 1.00832350e-04, 7.20098590e-05,
       3.91658106e-05, 1.81403536e-05, 7.08372382e-06, 2.45650079e-06,
       8.66259898e-07, 2.47665746e-07, 5.36536673e-10, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.62567333e-08,
       3.20786301e-06, 8.16506724e-06, 1.63338875e-05, 3.44507156e-05,
       6.80742264e-05, 1.24637747e-04, 2.04267715e-04, 2.74555038e-04,
       3.10145505e-04, 2.69110198e-04, 2.00621559e-04, 1.12453276e-04,
       5.26865341e-05, 2.00721705e-05, 6.35108323e-06, 1.79516755e-06,
       6.85694273e-07, 1.33916394e-07, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 3.28225277e-07, 4.98305067e-06,
       1.07298801e-05, 2.51433480e-05, 5.99254354e-05, 1.30687218e-04,
       2.58860704e-04, 4.52938776e-04, 6.45943880e-04, 7.69052766e-04,
       7.00013027e-04, 5.45450882e-04, 3.17109330e-04, 1.52521490e-04,
       5.84617581e-05, 1.78741263e-05, 4.49396322e-06, 1.30066982e-06,
       5.15356611e-07, 1.36544199e-08, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.30938275e-06, 6.10628963e-06, 1.44312947e-05,
       3.84421694e-05, 1.00895460e-04, 2.37617434e-04, 5.00540089e-04,
       9.22578880e-04, 1.38047875e-03, 1.71723118e-03, 1.62832217e-03,
       1.31952874e-03, 7.94125893e-04, 3.93356051e-04, 1.53696778e-04,
       4.68624419e-05, 1.12193528e-05, 2.78845923e-06, 9.13986443e-07,
       2.42182289e-07, 0.00000000e+00, 0.00000000e+00, 7.14702144e-09,
       2.52267342e-06, 7.16942103e-06, 1.94640926e-05, 5.75056273e-05,
       1.62848711e-04, 4.07332885e-04, 9.00874581e-04, 1.73122204e-03,
       2.69496364e-03, 3.47762603e-03, 3.41449631e-03, 2.86199272e-03,
       1.77561235e-03, 9.04038969e-04, 3.61237915e-04, 1.11269495e-04,
       2.62270815e-05, 6.03458722e-06, 1.60729539e-06, 5.52331745e-07,
       0.00000000e+00, 0.00000000e+00, 8.45317067e-08, 3.59625401e-06,
       8.49464153e-06, 2.57747934e-05, 8.26058156e-05, 2.48092701e-04,
       6.50180841e-04, 1.49388905e-03, 2.96787525e-03, 4.77158783e-03,
       6.34957412e-03, 6.42047655e-03, 5.53593945e-03, 3.52167462e-03,
       1.83459993e-03, 7.48264994e-04, 2.33700467e-04, 5.50656714e-05,
       1.22147718e-05, 2.89162181e-06, 8.87382480e-07, 2.08940915e-09,
       0.00000000e+00, 4.69191520e-07, 4.54669214e-06, 9.96643715e-06,
       3.29687671e-05, 1.12427301e-04, 3.52991348e-04, 9.58386628e-04,
       2.26738618e-03, 4.62344829e-03, 7.62935346e-03, 1.04165228e-02,
       1.07993110e-02, 9.52956603e-03, 6.17770563e-03, 3.27263023e-03,
       1.35608808e-03, 4.28985036e-04, 1.01607052e-04, 2.21804880e-05,
       4.91455413e-06, 1.24823522e-06, 5.76243412e-09, 0.00000000e+00,
       1.51994882e-06, 5.05504641e-06, 1.14137196e-05, 4.02488725e-05,
       1.43618639e-04, 4.65698249e-04, 1.29739087e-03, 3.13632257e-03,
       6.52176064e-03, 1.09834854e-02, 1.53177676e-02, 1.62246746e-02,
       1.45844771e-02, 9.56988135e-03, 5.11765565e-03, 2.14154351e-03,
       6.83777468e-04, 1.62877056e-04, 3.53239245e-05, 7.54310514e-06,
       1.71006292e-06, 8.88769121e-09, 0.00000000e+00, 3.23675137e-06,
       5.35519111e-06, 1.26264483e-05, 4.65083446e-05, 1.71120759e-04,
       5.67036566e-04, 1.60739811e-03, 3.94254602e-03, 8.30906463e-03,
       1.42002372e-02, 2.01329694e-02, 2.17224716e-02, 1.98153456e-02,
       1.30585294e-02, 6.99538961e-03, 2.93825800e-03, 9.42758269e-04,
       2.25382593e-04, 4.87327488e-05, 1.01967935e-05, 2.16549172e-06,
       1.19300066e-08, 0.00000000e+00, 4.84206557e-06, 5.57111214e-06,
       1.34038170e-05, 5.06139593e-05, 1.89508673e-04, 6.35673449e-04,
       1.81930539e-03, 4.49799278e-03, 9.54933851e-03, 1.64535298e-02,
       2.35675740e-02, 2.57832377e-02, 2.37962119e-02, 1.56126561e-02,
       8.32549890e-03, 3.49362574e-03, 1.12185232e-03, 2.68297373e-04,
       5.78614727e-05, 1.19771465e-05, 2.46366905e-06, 1.28475703e-08,
       0.00000000e+00, 5.17212380e-06, 5.61503135e-06, 1.35760805e-05,
       5.15833640e-05, 1.93974766e-04, 6.52571909e-04, 1.87113655e-03,
       4.63160024e-03, 9.83899254e-03, 1.69606811e-02, 2.43088940e-02,
       2.66351729e-02, 2.46138761e-02, 1.60613393e-02, 8.52999891e-03,
       3.56805403e-03, 1.14226874e-03, 2.72332855e-04, 5.85201275e-05,
       1.20684041e-05, 2.47192569e-06, 1.28509282e-08, 0.00000000e+00,
       4.01226328e-06, 5.47520079e-06, 1.31291355e-05, 4.92994645e-05,
       1.83882899e-04, 6.14812591e-04, 1.75293622e-03, 4.31522077e-03,
       9.11331676e-03, 1.55932984e-02, 2.21364888e-02, 2.39217405e-02,
       2.17831125e-02, 1.42274959e-02, 7.54702409e-03, 3.14139507e-03,
       9.99353789e-04, 2.36671278e-04, 5.06355292e-05, 1.04722255e-05,
       2.19457762e-06, 1.19274881e-08, 0.00000000e+00, 2.24678112e-06,
       5.21289047e-06, 1.21667431e-05, 4.43460429e-05, 1.61997171e-04,
       5.33408631e-04, 1.50106521e-03, 3.65041106e-03, 7.61543569e-03,
       1.28456937e-02, 1.79214539e-02, 1.89621264e-02, 1.69526812e-02,
       1.10041468e-02, 5.80734195e-03, 2.39687520e-03, 7.54656977e-04,
       1.76983468e-04, 3.77050963e-05, 7.89287067e-06, 1.74858765e-06,
       8.98675115e-09, 0.00000000e+00, 8.73825194e-07, 4.91473388e-06,
       1.08653641e-05, 3.77217775e-05, 1.33143964e-04, 4.27536865e-04,
       1.17795797e-03, 2.81078574e-03, 5.75641151e-03, 9.51197622e-03,
       1.29718544e-02, 1.33941480e-02, 1.17166080e-02, 7.49616081e-03,
       3.90726765e-03, 1.58984978e-03, 4.93319281e-04, 1.14298379e-04,
       2.43186123e-05, 5.23345800e-06, 1.28484591e-06, 5.93620876e-09,
       0.00000000e+00, 2.18672097e-07, 4.10183697e-06, 9.43100979e-06,
       3.05610180e-05, 1.02676959e-04, 3.18046498e-04, 8.50362902e-04,
       1.97641465e-03, 3.94807679e-03, 6.35389997e-03, 8.43042540e-03,
       8.46662228e-03, 7.21475355e-03, 4.51703441e-03, 2.30764224e-03,
       9.19995223e-04, 2.80252910e-04, 6.41339519e-05, 1.37408479e-05,
       3.12457760e-06, 9.14591864e-07, 2.44829155e-09, 0.00000000e+00,
       3.05729783e-08, 3.22562170e-06, 8.04870391e-06, 2.38185325e-05,
       7.49046214e-05, 2.21026030e-04, 5.67725047e-04, 1.27471276e-03,
       2.46668134e-03, 3.84292313e-03, 4.93644411e-03, 4.80123668e-03,
       3.96508389e-03, 2.41322058e-03, 1.20013436e-03, 4.66314535e-04,
       1.39176941e-04, 3.15905401e-05, 6.94129676e-06, 1.75048688e-06,
       5.94496909e-07, 0.00000000e+00, 0.00000000e+00, 1.79660259e-09,
       2.17782632e-06, 6.85293293e-06, 1.80938656e-05, 5.22682898e-05,
       1.44796494e-04, 3.53131395e-04, 7.58785298e-04, 1.41121597e-03,
       2.11372970e-03, 2.61364165e-03, 2.44903228e-03, 1.94896230e-03,
       1.14626076e-03, 5.51863606e-04, 2.08328086e-04, 6.10503533e-05,
       1.39186818e-05, 3.25294565e-06, 9.89315452e-07, 2.51414715e-07,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 9.77006539e-07,
       5.88718248e-06, 1.35221260e-05, 3.50550701e-05, 8.94860863e-05,
       2.04069398e-04, 4.14558433e-04, 7.33679776e-04, 1.04729959e-03,
       1.23734652e-03, 1.10956118e-03, 8.45434596e-04, 4.77809635e-04,
       2.21908285e-04, 8.14610462e-05, 2.36762931e-05, 5.58425462e-06,
       1.49067824e-06, 5.55003895e-07, 2.15235616e-08, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 2.28626880e-07, 4.73976618e-06,
       1.03172357e-05, 2.35933513e-05, 5.46606910e-05, 1.15096784e-04,
       2.18861032e-04, 3.65726723e-04, 4.94466125e-04, 5.55581069e-04,
       4.75113388e-04, 3.45836712e-04, 1.87784260e-04, 8.44121039e-05,
       3.04610791e-05, 8.99823736e-06, 2.31533593e-06, 7.80448116e-07,
       1.75397126e-07, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.57838036e-08, 3.15195291e-06, 8.13072712e-06,
       1.60786822e-05, 3.31856619e-05, 6.34584086e-05, 1.11442134e-04,
       1.73938782e-04, 2.20758479e-04, 2.34324654e-04, 1.90184217e-04,
       1.31942800e-04, 6.89538154e-05, 3.02591272e-05, 1.09760387e-05,
       3.45330252e-06, 1.06636295e-06, 3.66065680e-07, 5.61010304e-09,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       4.60326297e-10, 1.32486791e-06, 6.76331479e-06, 1.13658291e-05,
       2.05327943e-05, 3.50555639e-05, 5.60400735e-05, 8.07564663e-05,
       9.53393138e-05, 9.50098383e-05, 7.29755699e-05, 4.83378917e-05,
       2.45298282e-05, 1.07359640e-05, 4.09474080e-06, 1.49325103e-06,
       5.35510321e-07, 4.68646344e-08, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       1.65821299e-07, 5.02829430e-06, 8.53699138e-06, 1.33136557e-05,
       1.99913424e-05, 2.87000837e-05, 3.77567102e-05, 4.11331825e-05,
       3.83388626e-05, 2.79036932e-05, 1.78123200e-05, 8.96921073e-06,
       4.08530295e-06, 1.77561235e-06, 7.60586747e-07, 8.72339788e-08,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 6.64037381e-09,
       2.38219102e-06, 6.93933137e-06, 9.30172817e-06, 1.21668912e-05,
       1.55322427e-05, 1.85062729e-05, 1.85232208e-05, 1.61710855e-05,
       1.12573669e-05, 7.08312136e-06, 3.68974072e-06, 1.88283214e-06,
       9.29832083e-07, 1.29869455e-07, 6.99240695e-11, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 3.29693300e-07,
       5.14369962e-06, 7.16669516e-06, 8.15835131e-06, 9.24255887e-06,
       9.96379028e-06, 9.19407580e-06, 7.59968486e-06, 5.17447438e-06,
       3.34520373e-06, 1.93118485e-06, 9.98326647e-07, 9.72308352e-08,
       1.98924997e-10, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 1.03802865e-08, 1.53192589e-06,
       5.88241220e-06, 6.16474783e-06, 6.24427232e-06, 6.14605780e-06,
       5.30634360e-06, 4.25574530e-06, 2.94987261e-06, 2.06447627e-06,
       7.71463587e-07, 3.87793880e-08, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 8.95939362e-08, 2.16084687e-06,
       4.94023663e-06, 4.94084897e-06, 4.54841557e-06, 3.78565997e-06,
       2.92474714e-06, 1.60161945e-06, 3.73254488e-07, 3.49201590e-09,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 2.93260872e-09, 1.28649724e-07, 1.10643729e-06,
       2.37757480e-06, 2.29920585e-06, 1.59592177e-06, 5.21750570e-07,
       3.21915169e-08, 1.66100010e-10, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 4.24908863e-09, 3.76518627e-08, 8.90140948e-08,
       7.57583937e-08, 1.98828999e-08, 1.31350515e-09, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 8.33154324e-10, 1.21027343e-09, 4.48917516e-10,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]
    