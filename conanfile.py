from conans import ConanFile, tools, os

class BoostSignals2Conan(ConanFile):
    name = "Boost.Signals2"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/signals2"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "signals2"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Multi_Index/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Parameter/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Variant/1.64.0@bincrafters/testing"

                      #assert1 bind3 config0 core2 function5 iterator5 mpl5 multi_index12 optional5 parameter10 predef0 preprocessor0 smart_ptr4 throw_exception2 tuple4 type_traits3 variant9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()