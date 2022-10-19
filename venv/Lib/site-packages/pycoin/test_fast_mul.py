#!/usr/bin/env python3

from pycoin.ecdsa import Point, generator_secp256k1


from pycoin.ecdsa.native.library import load_library, make_inverse_mod_f, make_fast_mul_f
library = load_library()
inverse_mod = make_inverse_mod_f(library)
fast_mul = make_fast_mul_f(library)

BignumType = library.BignumType


def test_bignum():
    def check(n):
        bn = BignumType(n)
        n1 = bn.to_int()
        print (hex(n), hex(n1))
        assert n == n1

    check(1)
    check(0xf)
    check(0xff)
    check(0xfff)
    check(0xffff)
    check(0xfffff)
    check(0xffffff)
    check(0xfffffff)
    check(0xffffffff)
    check(0xfffffffff)
    check(0xffffffffff)
    check(0xfffffffffff)
    check(0xffffffffffff)
    check(0xfffffffffffff)
    check(0xffffffffffffff)
    check(0xfffffffffffffff)
    check(0xfffffff0ffffffff)
    check(0x10000000000000000)
    check(0xfffffff1fffffffff)
    check(0xfffffff2ffffffffff)
    check(0xfffffff3ffffffffffff)


def test_mod_inverse():
    def check(a, n):
        m = inverse_mod(a, n)
        print(a, m)
        assert (a * m) % n == 1

    for a in range(5, 100):
        check(a, 115792089237316195423570985008687907853269984665640564039457584007908834671663)


def test_generate():
    P = 10718280 * generator_secp256k1

    for i in range(1,1000):
        n = inverse_mod(i, 115792089237316195423570985008687907853269984665640564039457584007908834671663)
        print(P * n)


def start(f):
    f()
    return
    t = threading.Thread(target=f)
    t.start()

import thread, threading
start(test_bignum)
start(test_mod_inverse)
start(test_generate)
start(test_bignum)
start(test_mod_inverse)
start(test_generate)
