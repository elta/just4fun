# Makefile

CC     := gcc
CFLAGS := -lpthread -I./include
FILES  := head.o body/body.o

all: human

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

human: $(FILES)
	$(CC) $(CFLAGS) $(FILES) -o $@

clean:
	rm -rf $(FILES)

distclean: clean
	rm -rf human
