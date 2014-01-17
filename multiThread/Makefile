# Makefile

CC     := gcc
CFLAGS := -lpthread
FILES  := head.o \
          body/body.o

all: human

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

human: $(FILES)
	$(CC) $(CFLAGS) $< -o $@

clean: $(FILES)
	rm -rf $<

distclean: clean
	rm -rf human
