def testfunc():
    from bme590lecture03 import lec03script
    assert lec03script(1)(1) == 2
    assert lec03script(-2)(1) == 0
    assert lec03script(0)(0) == 0
    assert lec03script(2.5)(3.2) ==5.7

