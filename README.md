# openmp-src-analysis
This is a repository of analyzing openmp source code

# compiler gcc & openmp from source code

- download gcc source code package http://mirror.linux-ia64.org/gnu/gcc/releases/
- wget http://mirror.linux-ia64.org/gnu/gcc/releases/gcc-12.2.0/gcc-12.2.0.tar.gz
- tar -zvxf gcc-12.2.0.tar.gz
- mkdir temp && mkdir install
- cd gcc-12.2.0
- ./contrib/download_prerequisites
- cd ../temp
- ../gcc-12.2.0/configure --prefix=/root/test/install --enable-threads=p
osix --disable-checking --disable-multilib --disable-bootstrap --enable-openmp -
-enable-languages=c,c++
- make -j32 (about a few minutes)
- make install
- cd .. && mkdir openmp && cd openmp
- ../gcc-12.2.0/libgomp/configure --prefix=/root/test/install --disable-multilib CFLAGS=-g CXXFLAGS=-g FCFLAGS=-g
- make -j32
- make install