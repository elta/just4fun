#! /bin/bash

# Check debhelper exist

# Check dh-make exist

# create a tmp dir, do all thins in it.
mkdir -pv tmp
cd tmp

# create atest-0.1 dir, and touch files in it.
mkdir -pv atest-0.1
cd atest-0.1
cat > Makefile << EOF
# Makefile

all:

install:
	mkdir -pv \$(DESTDIR)/usr/bin
	cp a.sh \$(DESTDIR)/usr/bin/a.sh
	mkdir -pv \$(DESTDIR)/bin
	cp a.sh \$(DESTDIR)/bin/a.sh

clean:

destclean:
	rm \$(DESTDIR)/usr/bin/a.sh

EOF

cat > a.sh << EOF
#! /bin/bash

echo "Hello deb"

EOF

chmod +x a.sh

cd ..

# tar
tar cvf atest-0.1.tar.gz atest-0.1

# Begin build deb
cd atest-0.1
echo "" | dh_make -s -e "Name Family facker@fake.com" -f ../atest-0.1.tar.gz

dpkg-buildpackage -rfakeroot -b -us -uc

cd ..

cp *.deb ../
