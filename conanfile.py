from conans import ConanFile, tools, os

class BoostSignals2Conan(ConanFile):
    name = "Boost.Signals2"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-signals2"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["signals2"]
    requires =  "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Bind/1.65.1@bincrafters/stable", \
                      "Boost.Concept_Check/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Function/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Multi_Index/1.65.1@bincrafters/stable", \
                      "Boost.Optional/1.65.1@bincrafters/stable", \
                      "Boost.Parameter/1.65.1@bincrafters/stable", \
                      "Boost.Predef/1.65.1@bincrafters/stable", \
                      "Boost.Preprocessor/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Tuple/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable", \
                      "Boost.Variant/1.65.1@bincrafters/stable"

                      #assert1 bind3 config0 core2 function5 iterator5 mpl5 multi_index12 optional5 parameter10 predef0 preprocessor0 smart_ptr4 throw_exception2 tuple4 type_traits3 variant9
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()