#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostSignals2Conan(base.BoostBaseConan):
    name = "boost_signals2"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_signals2"
    lib_short_names = ["signals2"]
    header_only_libs = ["signals2"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_iterator",
        "boost_mpl",
        "boost_multi_index",
        "boost_optional",
        "boost_parameter",
        "boost_predef",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_variant"
    ]


